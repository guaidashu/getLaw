# coding=utf-8
import json
from time import sleep

from tool import phoenix_db
from tool.function import curlData, debug, getNowTimeStamp
from getLaw import thread_config


# noinspection PyBroadException
class GetProxyIp(object):
    def __init__(self):
        self.proxy_ip = ""
        self.ip_over = 0
        self.config = thread_config.config
        # 数据库连接全局变量
        self.ws_db = phoenix_db.DBConfig()

    def __del__(self):
        self.ws_db.closeDB()

    def setProxyIp(self):
        """
        进行proxy ip获取，并且存到数据库(law_proxy_ip)提供调用
        :return:
        """
        url = self.config['proxy_ip_url']
        try:
            data = curlData(url, timeout=5)
        except:
            data = ""
        try:
            data = json.loads(data)
            if str(data['ERRORCODE']) == "10032":
                debug("proxy ip 今日提取量已达上限，结束程序", True)
                self.ip_over = 1
                return 1
            for k, v in enumerate(data['RESULT']):
                v['id'] = "NEXT VALUE FOR LAW_PROXY_IP_SEQUENCE"
                v['table'] = "proxy_ip"
                # 获取时间戳，表示ip获取时间
                v['time_stamp'] = str(getNowTimeStamp())
                tmp = k + 1
                try:
                    # 加锁
                    self.ws_db.insert(v, is_close_db=False)
                    # 解锁
                    debug("第" + str(tmp) + "条ip插入成功")
                except Exception as e:
                    debug(e, True)
                    debug("第" + str(tmp) + "条ip插入失败")
        except Exception as e:
            debug("proxy ip 获取出错,睡眠5秒 %s" % (e.__str__()), True)
            sleep(5)

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
        data = self.ws_db.select(selectArr, is_close_db=False)
        # 解锁
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
            debug("\n代理ip暂无，删除库存并进行动态获取")
            # 如果没有结果表示已经用完了，那么就进行删除数据并且重新获取
            # 加锁
            self.ws_db.delete({"table": "proxy_ip"}, is_close_db=False)
            # 解锁
            self.setProxyIp()
            data = self.getSingleProxyIp()
        return data

    def getProxyIp(self):
        self.proxy_ip = self.getSingleProxyIp()
        return self.proxy_ip

