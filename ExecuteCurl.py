# -*- coding: utf-8 -*-
import json
import threading
from time import sleep

from tool import phoenix_db
from tool.function import debug, curlData, getNowTimeStamp
from getLaw import thread_config

# 页码
index = 1
# 线程锁
mylock = threading.RLock()
# 判断proxy_ip 是否达到日提取上限
stop_thread = False
# status为状态值，
status = 0
page_stop_thread = False
stop_page = 0


# noinspection PyBroadException,PyMethodMayBeStatic,PyPep8Naming,PyIncorrectDocstring
class ExecuteCurl(threading.Thread):
    def __init__(self, name, param, proxy_ip, table_columns):
        threading.Thread.__init__(self, name=name)
        self.param = param
        # debug(name)
        self.config = thread_config.config
        # 数据库连接全局变量
        self.ws_db = phoenix_db.DBConfig()
        # 全局代理IP
        self.proxy_ip = proxy_ip
        self.table_columns = table_columns
        self.is_set_proxy = 0

    def __del__(self):
        self.ws_db.closeDB()

    def run(self):
        global index
        global stop_thread
        global page_stop_thread
        global stop_page
        data_is_get = True
        page = None
        # 页码是否变化，如果抓取了5次依旧无数据，则抓取下一页(后期可中断并记录)
        index_is_change = 0
        # 这个变量用来记录抓数据为空的页数，如果连续且达到了3，则终止本次抓取
        is_end = 0
        # 抓取数据
        while True:
            mylock.acquire()
            if stop_thread:
                mylock.release()
                break
            if index > self.config['over_index']:
                mylock.release()
                break
            if data_is_get:
                page = index
                debug(self.name + "取得index为：" + str(index), True)
                index = index + 1
                data_is_get = False
            else:
                debug(self.name + "继续取得index为%s的列表页" % str(page), True)
            if page_stop_thread and page > stop_page:
                debug("此条件文书已经获取完毕，停止%s" % self.name, True)
                mylock.release()
                break
            mylock.release()
            is_get_new_proxy_ip = 0
            while True:
                try:
                    try:
                        guid = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
                        guid = json.loads(guid)
                        self.param['post']['guid'] = guid['guid']
                    except:
                        pass
                    self.param['post']['Index'] = page

                    resultData = curlData("http://wenshu.court.gov.cn/List/ListContent", value=self.param['post'],
                                          referer=self.param['url'],
                                          cookie=self.param['cookie_all'], header=self.param['header'],
                                          proxy_ip=self.proxy_ip, timeout=10)
                    debug(self.param['post'])
                    break
                except Exception as e:
                    if is_get_new_proxy_ip > 0:
                        debug("重新获取代理ip")
                        self.setProxyIp()
                        is_get_new_proxy_ip = 0
                    else:
                        debug("第" + str(page) + "页列表获取出错，尝试重新获取,尝试次数：" + str(is_get_new_proxy_ip), True)
                        is_get_new_proxy_ip = is_get_new_proxy_ip + 1
                    debug(e)
                    if e.__str__().find("latin-1") != -1:
                        debug(self.param, True)
            try:
                # 数据传入插入处理函数
                result = self.insertWenShuList(resultData, table_columns=self.table_columns)
            except Exception as e:
                debug("getWenShuListContent函数出错： insertWenShuList：" + e.__str__())
                break
            """
            0表示抓取出错，数据已经存在
            1表示抓取成功
            2表示数据为空
            """
            mylock.acquire()
            if result == 0:
                debug("数据已经存在，退出本次", True)
                mylock.release()
                break
            elif result == 1:
                data_is_get = True
                debug("第" + str(page) + "页文书id获取成功", True)
            elif result == 2:
                if index_is_change > self.config['index_is_change']:
                    index_is_change = 0
                    is_end = is_end + 1
                else:
                    index_is_change = index_is_change + 1
            elif result == 3:
                debug("返回文书结果为空，结束本次抓取", True)
                mylock.release()
                break
            elif result == 4:
                debug("本条件文书第%s页抓取完毕，结束本次抓取" % page, True)
                page_stop_thread = True
                stop_page = page
                mylock.release()
                break
            elif result == 5:
                if stop_thread:
                    debug("数据超过210条，且已经存入待重新处理数据库，直接结束")
                    mylock.release()
                    break
                debug("数据超过210条，存入待重新处理数据库")
                insertArr = {
                    "table": "ws_over_record",
                    "court_name": self.param['court_name'],
                    "start_date": self.param['start_date'],
                    "end_date": self.param['end_date'],
                    "id": "NEXT VALUE FOR LAW_WS_OVER_RECORD_SEQUENCE"
                }
                self.ws_db.insert(insertArr)
                stop_thread = True
                mylock.release()
                break
            if is_end > self.config['is_end']:
                debug("本次条件的docid抓取终止(可能遇到空数据)，退出本次抓取并重新构造条件和获取cookie", True)
                mylock.release()
                break
            if index > self.config['over_index']:
                debug("已经到了第 " + str(index) + " 页，此线程停止", True)
                mylock.release()
                break
            mylock.release()

    def insertWenShuList(self, result_data, table_columns=False):
        """
        :param result_data: the docid's json data
        :return:  no return
        """
        selectArr = {
            "table": "ws_docid"
        }
        try:
            result_data = json.loads(result_data.replace("\n", "\/n"))
            debug(result_data)
            result_data = json.loads(result_data)
        except Exception as e:
            if str(result_data).find("remind") != -1:
                debug("接口数据返回出错，返回数据为：" + str(result_data), True)
                if self.is_set_proxy > 5:
                    self.is_set_proxy = 0
                    self.setProxyIp()
                else:
                    self.is_set_proxy = self.is_set_proxy + 1
                    return 2
            result_data = list()
        post = dict()
        try:
            runEval = result_data[0]['RunEval']
            # 本条件总共文书条数
            try:
                count = int(result_data[0]['Count'])
                if count > 210:
                    return 5
                # 如果条数为0，自然直接返回
                if count == 0:
                    debug(result_data)
                    return 3
            except:
                debug(result_data)
                return 2
        except Exception as e:
            debug("RunEval获取出错", True)
            return 2
        length = len(result_data)
        docId = ""
        insertList = list()
        for i in range(1, length):
            insertArr = dict()
            insertArr['table'] = "ws_docid"
            insertArr['id'] = "NEXT VALUE FOR LAW_WS_DOCID_SEQUENCE"
            try:
                try:
                    insertArr['title'] = result_data[i]['案件名称']
                except:
                    insertArr['title'] = ""
                try:
                    insertArr['case_type'] = result_data[i]['案件类型']
                except:
                    insertArr['case_type'] = ""
                try:
                    insertArr['cp_date'] = result_data[i]['裁判日期']
                except:
                    insertArr['cp_date'] = ""
                try:
                    insertArr['court_name'] = result_data[i]['法院名称']
                except:
                    insertArr['court_name'] = ""
                try:
                    insertArr['case_num'] = result_data[i]['案号']
                except:
                    insertArr['case_num'] = ""
                try:
                    insertArr['content'] = result_data[i]['裁判要旨段原文']
                except:
                    insertArr['content'] = ""
                insertList.append(insertArr)
            except:
                pass
            try:
                if i >= length - 1:
                    docId = docId + result_data[i]['文书ID']
                else:
                    docId = docId + result_data[i]['文书ID'] + ","
            except Exception as e:
                debug("文书ID拼接出错，错误未知，暂时判断为无此条目 ：" + e.__str__(), True)
                return 2
        if docId.strip() == "" and count != 0:
            return 4
        try:
            post['runEval'] = runEval
            post['docId'] = docId
            result_data = curlData(self.config['get_docid_api_url'], value=post)
            result_data = json.loads(result_data)
            result_data = result_data['data'].split(",")
        except Exception as e:
            debug(e, True)
            return 2
        mylock.acquire()
        for k, v in enumerate(result_data):
            # noinspection PyBroadException
            # debug("本次处理的文书id => " + v)
            # try:
            #     selectArr['table'] = "ws_docid"
            #     selectArr['condition'] = ['"docid"=' + "'" + v + "'"]
            #     selectResult = self.ws_db.select(selectArr, is_close_db=False)
            #     unused = selectResult[0]['docid']
            #     debug("文书已经存在 => " + v, True)
            #     continue
            # except:
            #     insertList[k]['table'] = "ws_docid"
            #     insertList[k]['docid'] = v
            #     insertResult = self.ws_db.insert(insertList[k], is_close_db=False)
            #     try:
            #         if insertResult != 0:
            #             debug("文书插入成功 => " + v, True)
            #         else:
            #             debug("文书插入失败 => " + v, True)
            #     except:
            #         debug("文书插入出现异常 => " + v, True)
            insertList[k]['table'] = "ws_docid"
            insertList[k]['docid'] = v
            insertResult = self.ws_db.insert(insertList[k], is_close_db=False, table_columns=table_columns)
            try:
                if insertResult != 0:
                    debug("文书插入成功 => " + v, True)
                else:
                    debug("文书插入失败 => " + v, True)
            except:
                debug("文书插入出现异常 => " + v, True)
        self.ws_db.closeDB()
        mylock.release()
        return 1

    def getProxyIp(self):
        """
        进行proxy ip获取，并且存到数据库(law_proxy_ip)提供调用
        :return:
        """
        mylock.acquire()
        url = self.config['proxy_ip_url']
        try:
            data = curlData(url, timeout=5)
        except:
            data = ""
        try:
            data = json.loads(data)
            if str(data['ERRORCODE']) == "10032":
                debug("proxy ip 今日提取量已达上限，结束线程", True)
                global stop_thread
                global status
                mylock.release()
                status = 2
                stop_thread = True
                return 0
            for k, v in enumerate(data['RESULT']):
                v['id'] = "NEXT VALUE FOR LAW_PROXY_IP_SEQUENCE"
                v['table'] = "proxy_ip"
                v['time_stamp'] = str(getNowTimeStamp())
                tmpK = 1 + k
                try:
                    self.ws_db.insert(v, is_close_db=False)
                    debug("第" + str(tmpK) + "条ip插入成功")
                except Exception as e:
                    debug("第" + str(tmpK) + "条ip插入失败")
                sleep(1)
        except Exception as e:
            debug("proxy ip 获取出错,睡眠5秒")
            sleep(5)
        mylock.release()

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
        # 加锁
        mylock.acquire()
        data = self.ws_db.select(selectArr, is_close_db=False)
        # 解锁
        try:
            # 若果存在，就返回拼接好的proxy和端口
            updateArr = data[0]
            updateArr['table'] = "proxy_ip"
            updateArr['is_used'] = 1
            # 加锁
            mylock.acquire()
            self.ws_db.insert(updateArr, is_close_db=False)
            overtime = getNowTimeStamp() - updateArr['time_stamp']
            if overtime > 120:
                debug("超时间")
                data = self.getSingleProxyIp()
            else:
                data = data[0]['ip'] + ":" + str(data[0]['port'])
            # 解锁
            mylock.release()
        except Exception as e:
            debug("\nip暂无，删除库存并进行动态获取")
            # 如果没有结果表示已经用完了，那么就进行删除数据并且重新获取
            # 加锁
            mylock.acquire()
            self.ws_db.delete({"table": "proxy_ip"}, is_close_db=False)
            # 解锁
            mylock.release()
            self.getProxyIp()
            data = self.getSingleProxyIp()
        self.ws_db.closeDB()
        mylock.release()
        return data

    def setProxyIp(self):
        self.proxy_ip = self.getSingleProxyIp()

    def reset(self):
        global index
        global stop_thread
        global page_stop_thread
        global stop_page
        page_stop_thread = False
        stop_page = 0
        stop_thread = False
        index = 1

    def getStatus(self):
        global status
        return status

    def getLastProxyIp(self):
        return self.proxy_ip

