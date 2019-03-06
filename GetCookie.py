import json
from time import sleep

from tool.function import getCookie, debug, curlData, getTimeStamp, getDateTime
from getLaw.GetProxyIp import GetProxyIp
from tool import phoenix_db
import urllib.parse


class GetCookie(object):
    def __init__(self):
        self.ws_db = phoenix_db.DBConfig()
        self.proxy_ip = ""
        self.is_change_proxy = 0

    def __del__(self):
        self.ws_db.closeDB()

    def getCookie(self):
        url = self.getUrl()
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }
        try:
            cookie = getCookie(url, referer="http://wenshu.court.gov.cn", header=header, proxy_ip=self.proxy_ip,
                               timeout=5)
            try:
                vjkl5 = cookie['vjkl5']
            except Exception as e:
                debug("cookie获取出错,重新获取 %s" % e.__str__(), True)
                sleep(3)
                return self.getCookie()
            return cookie
        except Exception as e:
            if self.is_change_proxy > 4:
                self.resetProxyIp()
                self.is_change_proxy = 0
            else:
                self.is_change_proxy = self.is_change_proxy + 1
            if e.__str__().find("HTTPConnectionPool") != -1:
                debug("cookie获取出错，HttpConnect错误，重新获取ip并重新获取")
                return self.getCookie()
            else:
                return 0

    def saveCookie(self):
        cookie = self.getCookie()

        cookie = json.dumps(cookie)
        debug("此次获取到的cookie为: %s" % cookie, True)
        insertArr = {
            "id": 1,
            "table": "ws_docid_cookie",
            "cookie": cookie
        }
        self.ws_db.insert(insertArr, is_close_db=False)

    def getUrl(self):
        start_date = self.ws_db.select({"table": "ws_docid_record"}, is_close_db=False)
        start_date = start_date[0]['start_date']
        start_date = getTimeStamp(start_date, "%Y-%m-%d")
        end_date = start_date + 432000
        end_date = getDateTime(end_date, "%Y-%m-%d")
        court_name = "最高人民法院"
        try:
            guid = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
            guid = json.loads(guid)
            guid = guid['guid']
            number = ""
        except Exception as e:
            debug(e, True)
            debug("guid获取出错")
            return self.getUrl()
        url = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=%s&guid=%s&conditions=searchWord+%s+SLFY++%s&conditions=searchWord++CPRQ++%s%%20TO%%20%s" % (
            number, guid, urllib.parse.quote(str(court_name)), urllib.parse.quote("法院名称:%s" % court_name),
            urllib.parse.quote(str(start_date)), urllib.parse.quote(str(end_date)))
        return url

    def resetProxyIp(self):
        self.proxy_ip = GetProxyIp().getProxyIp()


if __name__ == "__main__":
    while True:
        try:
            debug("开始获取cookie", True)
            GetCookie().saveCookie()
        except Exception as e:
            debug(e, True)
        sleep(120)
