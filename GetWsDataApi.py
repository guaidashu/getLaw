import json
from time import sleep

import thread_config
from GetProxyIp import GetProxyIp
from tool.function import debug, getCookie, curlData
from tool import phoenix_db


# noinspection PyBroadException
class GetWsDataApi(object):
    def __init__(self):
        self.ws_db = phoenix_db.DBConfig()
        self.proxy_ip = ""
        self.config = thread_config.config
        self.page = 1
        self.param = ""

    def __del__(self):
        self.ws_db.closeDB()

    def init(self, param):
        """
        :return:
        """
        self.param = param
        debug(self.getData(), True)

    def getNumAndGuid(self):
        """
        :return:
        """
        try:
            header_1 = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                "Origin": "http://wenshu.court.gov.cn/"
            }
            guid = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
            guid = json.loads(guid)
            guid = guid['guid']
            num_flag = 0
            try:
                number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", value={"guid": guid},
                                  referer="http://wenshu.court.gov.cn", header=header_1,
                                  proxy_ip=self.proxy_ip, timeout=5)
            except Exception as e:
                number = "remind"
            while number.find("remind") != -1 or number.find("html") != -1 or number.find("服务不可用") != -1:
                if num_flag > 3:
                    self.resetProxyIp()
                    num_flag = 0
                else:
                    num_flag = num_flag + 1
                debug("number获取出错，继续获取", True)
                try:
                    number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", value={"guid": guid},
                                      referer="http://wenshu.court.gov.cn",
                                      header=header_1,
                                      proxy_ip=self.proxy_ip, timeout=5)
                except Exception as e:
                    debug(e, True)
                sleep(0.5)
        except Exception as e:
            debug("guid获取出错")
            return self.getNumAndGuid()
        return {"guid": guid, "number": number}

    def decrypt(self, result_data):
        """
        :param result_data:
        :return:
        """
        try:
            result_data = json.loads(result_data.replace("\n", "\/n"))
            result_data = json.loads(result_data)
        except Exception as e:
            if str(result_data).find("remind") != -1:
                debug("接口数据返回出错，返回数据为：" + str(result_data), True)
            result_data = list()
        post = dict()
        try:
            runEval = result_data[0]['RunEval']
            # 本条件总共文书条数
            try:
                count = int(result_data[0]['Count'])
            except:
                debug(result_data, True)
                return 2
        except Exception as e:
            debug(result_data, True)
            debug(e, True)
            debug("RunEval获取出错", True)
            return 2
        length = len(result_data)
        docId = ""
        insertList = list()
        for i in range(1, length):
            insertArr = dict()
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
            # return result_data
        except Exception as e:
            debug(e, True)
            return 2
        for k, v in enumerate(result_data):
            insertList[k]['table'] = "ws_docid"
            insertList[k]['docid'] = v
        return insertList

    def getData(self):
        """
        :return: a json
        """
        self.resetProxyIp()
        numAndGuid = self.getNumAndGuid()
        url = "http://wenshu.court.gov.cn/list/list/?sorttype=1" + "&number=" + numAndGuid['number'] + "&guid=" + \
              numAndGuid['guid']
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        cookie_get_num = 0
        while True:
            try:
                cookie = getCookie(url, header=header, referer="http://wenshu.court.gov.cn", proxy_ip=self.proxy_ip,
                                   timeout=5)
                break
            except:
                if cookie_get_num > 1:
                    self.resetProxyIp()
                    cookie_get_num = 0
                cookie_get_num = cookie_get_num + 1
                debug("cookie获取失败，继续获取", True)
        # noinspection PyBroadException
        try:
            vjkl5 = cookie['vjkl5']
        except Exception as e:
            debug("vjk5获取失败，终止", True)
            return self.getData()
        try:
            post = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=" + vjkl5)
        except Exception as e:
            post = "{}"
            debug("post参数获取出错", True)
        post = json.loads(post)
        post['Order'] = "法院层级"
        post['Page'] = 10
        post['number'] = numAndGuid['number']
        post['Direction'] = "asc"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Origin": "http://wenshu.court.gov.cn"
        }
        page = "1"
        param = {
            "vjkl5": vjkl5,
            "post": post,
            "header": header,
            "cookie_all": cookie,
            "url": url
        }
        param['post']['Param'] = self.param
        # 抓取数据
        is_get_new_proxy_ip = 0
        while True:
            try:
                param['post']['Index'] = page
                resultData = curlData("http://wenshu.court.gov.cn/List/ListContent", value=param['post'],
                                      referer=param['url'],
                                      cookie=param['cookie_all'], header=param['header'],
                                      proxy_ip=self.proxy_ip, timeout=5)
                break
            except Exception as e:
                if is_get_new_proxy_ip > 0:
                    debug("重新获取代理ip", True)
                    self.resetProxyIp()
                    is_get_new_proxy_ip = 0
                else:
                    debug("第" + str(page) + "页列表获取出错，尝试重新获取,尝试次数：" + str(is_get_new_proxy_ip), True)
                    is_get_new_proxy_ip = is_get_new_proxy_ip + 1
                debug(e, True)
                if e.__str__().find("latin-1") != -1:
                    debug(param, True)
        resultData = self.decrypt(resultData)
        return resultData

    def resetProxyIp(self):
        getProxyIp = GetProxyIp()
        self.proxy_ip = getProxyIp.getProxyIp()
