import json
import re
import threading

from tool.function import debug, curlData, getNowTimeStamp
from tool import phoenix_db
import thread_config
from concurrent.futures import ThreadPoolExecutor, as_completed

lock_flag = 0
mylock = threading.RLock()
get_num_count = 0


# noinspection PyBroadException
class GetWs(object):
    def __init__(self):
        debug("启动主线程", True)
        # 数据库连接全局变量
        self.ws_db = phoenix_db.DBConfig()
        # 全局代理IP
        self.proxy_ip = ""
        self.proxy_ip_time = 0
        self.config = thread_config.config

    def __del__(self):
        self.ws_db.closeDB()

    def getWenShuDetailAll(self):
        """
        获取所有数据库已有的文书ID对应的详细信息
        :return:
        """
        # 首先获取文书的docid(未处理过的)
        debug("获取ip")
        self.setProxyIp()
        debug("ip获取成功")
        # 加锁
        start_id_list = self.ws_db.select({"table": "ws_content_id_record", "limit": [0, 1]}, is_close_db=False)
        try:
            start_id = start_id_list[0]['docid_id']
            end_id = start_id + 100
        except:
            exit(1)
        docIdList = self.ws_db.select(
            {"table": "ws_docid", "columns": ["id", "docid"],
             "condition": ['"is_handle"=0 and "id">=%s and "id"<%s' % (str(start_id), str(end_id))]},
            is_close_db=False)
        debug(str(start_id) + " - " + str(end_id))
        start_id_list[0]['table'] = "ws_content_id_record"
        start_id_list[0]['docid_id'] = end_id
        self.ws_db.insert(start_id_list[0], is_close_db=False)
        for docid in docIdList:
            try:
                docid['table'] = "ws_docid"
                docid['is_handle'] = 1
                self.ws_db.insert(docid, is_close_db=False)
            except:
                pass
        # 实例化线程池
        thread_pool = ThreadPoolExecutor(max_workers=15)
        task_list = list()
        for docid in docIdList:
            task = thread_pool.submit(self.getWenShuDetailData, docid['docid'])
            task_list.append(task)
        debug("线程数量：" + str(len(task_list)), True)
        for i in as_completed(task_list):
            debug(i.result())
        debug("处理了 " + str(lock_flag) + "个", True)
        return 1

    # noinspection PyPep8Naming
    # 得到 裁判文书网 的详情页数据
    # noinspection PyBroadException
    def getWenShuDetailData(self, docid):
        global mylock
        global lock_flag
        global get_num_count
        mylock.acquire()
        if get_num_count > 15:
            self.setProxyIp()
            get_num_count = 0
        get_num_count = get_num_count + 1
        mylock.release()
        url = "http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=" + docid
        referer = "http://wenshu.court.gov.cn/content/content?DocID=" + docid + "&KeyWord="
        # debug("开始获取文书 => " + docid)
        header_1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        try:
            data = curlData(url, referer=referer, header=header_1, proxy_ip=self.proxy_ip, timeout=5)
        except Exception as e:
            debug("数据获取出错,重新获取", True)
            return self.getWenShuDetailData(docid)
        # 判断乱码
        if data.find("�") != -1:
            debug("出现乱码，重新获取", True)
            return self.getWenShuDetailData(docid)
        # debug("数据获取成功，开始处理")
        dataFlag = re.findall('\$\("#DivContent"\)\.html\(jsonHtml\)', data)
        try:
            unusedData = dataFlag[0]
        except:
            return self.getWenShuDetailData(docid)
        insertArr = {
            "id": " NEXT VALUE FOR LAW_WS_ORIGIN_CONTENT_SEQUENCE",
            "table": "ws_origin_content",
            "content": data
        }
        # 加锁
        mylock.acquire()
        insertResult = self.ws_db.insert(insertArr, is_close_db=False)
        if insertResult == 1:
            lock_flag = lock_flag + 1
            debug("文书 " + docid + " => 插入成功\n", True)
            mylock.release()
        else:
            debug("文书 " + docid + " => 插入失败\n", True)
            # 解锁
            mylock.release()
            return 3
        return 1

    def getProxyIp(self):
        """
        进行proxy ip获取，并且存到数据库(law_proxy_ip)提供调用
        :return:
        """
        url = self.config['proxy_ip_url']
        data = curlData(url)
        try:
            data = json.loads(data)
            for k, v in enumerate(data['RESULT']):
                v['id'] = "NEXT VALUE FOR LAW_PROXY_IP_SEQUENCE"
                v['table'] = "proxy_ip"
                # 获取时间戳，表示ip获取时间
                v['time_stamp'] = getNowTimeStamp()
                try:
                    # 加锁
                    self.ws_db.insert(v, is_close_db=False)
                    # 解锁
                    debug("第" + str(k) + "条ip插入成功")
                except Exception as e:
                    debug("第" + str(k) + "条ip插入失败")
        except Exception as e:
            debug("proxy ip 获取出错")

    def getSingleProxyIp(self):
        """
        获取单个ip并返回
        :return:
        """
        selectArr = {
            "table": "proxy_ip",
            "condition": ['"is_used"=0'],
            "limit": [0, 1]
        }
        data = self.ws_db.select(selectArr, is_close_db=False)
        try:
            # 若果存在，就返回拼接好的proxy和端口
            updateArr = data[0]
            updateArr['table'] = "proxy_ip"
            updateArr['is_used'] = 1
            # 加锁
            self.ws_db.insert(updateArr, is_close_db=False)
            overtime = getNowTimeStamp() - updateArr['time_stamp']
            if overtime > 120:
                debug("超时间")
                data = self.getSingleProxyIp()
            else:
                data = data[0]['ip'] + ":" + str(data[0]['port'])
            # 解锁
        except Exception as e:
            debug("\nip暂无，删除库存并进行动态获取")
            # 如果没有结果表示已经用完了，那么就进行删除数据并且重新获取
            # 加锁
            self.ws_db.delete({"table": "proxy_ip"}, is_close_db=False)
            # 解锁
            self.getProxyIp()
            data = self.getSingleProxyIp()
        return data

    def setProxyIp(self):
        global mylock
        mylock.acquire()
        self.proxy_ip = self.getSingleProxyIp()
        mylock.release()
