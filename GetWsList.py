# -*- coding: utf-8 -*-
import json
import random
import urllib.parse
from time import sleep

from getLaw.GetProxyIp import GetProxyIp
from tool import phoenix_db
from tool.function import debug, curlData, getCookie, getTimeStamp, getDateTime, getNowTimeStamp, getUserAgent
from getLaw.ExecuteCurl import ExecuteCurl
from tool import db
from getLaw.thread_config import config

page = 1


# noinspection PyBroadException,PyMethodMayBeStatic
class GetWsList(object):
    def __init__(self):
        # 数据库连接全局变量
        self.ws_db = phoenix_db.DBConfig()
        self.config = config
        # 全局代理IP
        self.proxy_ip = ""
        self.is_change_proxy = 0
        self.guid = ""
        self.cookie = ""
        self.ip_over = 0
        self.user_agent_index = int((random.random()) * 1000) % getUserAgent(2)
        self.table_columns = self.ws_db.getColumns({"table": "ws_docid"})

    def __del__(self):
        self.ws_db.closeDB()

    def getCookie(self, url):
        if self.ip_over == 1:
            return 0
        header = {
            "User-Agent": getUserAgent(index=self.user_agent_index)
        }
        try:
            cookie = getCookie(url, referer="http://wenshu.court.gov.cn", header=header, proxy_ip=self.proxy_ip,
                               timeout=5)
            return cookie
        except Exception as e:
            if self.is_change_proxy > 4:
                self.setProxyIp()
                self.is_change_proxy = 0
            else:
                self.is_change_proxy = self.is_change_proxy + 1
            if e.__str__().find("HTTPConnectionPool") != -1:
                debug("cookie获取出错，HttpConnect错误，重新获取ip并重新获取")
                return self.getCookie(url)
            else:
                return 0

        # try:
        #     selectArr = {
        #         "table": "ws_docid_cookie"
        #     }
        #     data = self.ws_db.select(selectArr, is_close_db=False)
        #     cookie = data[0]['cookie']
        #     cookie = json.loads(cookie)
        # except Exception as e:
        #     debug("cookie获取出错,错误信息: %s" % e.__str__(), True)
        #     return self.getCookie(url)
        # return cookie

    def getWenShuListContent(self):
        """
        :return:
        """
        # 启动多线程
        thread_num = self.config['thread_num']
        court = self.getCourt()
        # updateArr = {
        #     "table": "court",
        #     "set": ['is_handle=0']
        # }
        insertRecordArr = {
            "id": 1
        }
        start_date_record = self.ws_db.select({"table": "ws_docid_record"})
        start_date_record_i = 0
        for docid_i, docid in enumerate(court):
            # 跳到上一次处理的法院
            try:
                if docid_i < start_date_record[0]['court_num']:
                    continue
            except:
                debug("上一次记录获取出错，直接停止")
                break
            while True:
                try:
                    year = self.getYear(docid['name'])
                    break
                except Exception as e:
                    debug(e, True)
                    debug("年份获取出错，终止程序，联系技术人员，程序继续执行，若要停止请按ctrl + C， 睡眠3秒")
                    sleep(3)
            # 开始时间
            # start_date = self.config['ws_start_get_date']
            # 转化为时间戳
            for y in year:
                if start_date_record[0]['court_year'] != str(y['Key']) and start_date_record_i == 0:
                    continue
                start_record = str(y['Key'])
                start_date = str(y['Key']) + "-01-01"
                if int(y['IntValue']) <= 210:
                    end_date = str(y['Key']) + "-12-31"
                    end_time_stamp = getTimeStamp(end_date, "%Y-%m-%d")
                    self.getWsContentHandle(thread_num, end_time_stamp, end_time_stamp, start_date, end_date, docid,
                                            docid_i, insertRecordArr, start_record)
                else:
                    if start_date_record_i == 0:
                        start_date = start_date_record[0]['start_date']
                    start_time_stamp = getTimeStamp(start_date, "%Y-%m-%d")
                    start_time_stamp = start_time_stamp + self.config['interval_time_stamp']
                    end_date = getDateTime(start_time_stamp, "%Y-%m-%d")
                    end_time_stamp = getTimeStamp(str(y['Key']) + "-12-31", "%Y-%m-%d")
                    self.getWsContentHandle(thread_num, start_time_stamp, end_time_stamp, start_date, end_date, docid,
                                            docid_i, insertRecordArr, start_record)
                start_date_record_i = start_date_record_i + 1
            debug("所有线程执行完毕，开始下一个任务")

    def getWsContentHandle(self, thread_num, start_time_stamp, end_time_stamp, start_date, end_date, docid, docid_i,
                           insertRecordArr, start_record):
        """
        :param thread_num:
        :param start_time_stamp:
        :param end_time_stamp:
        :param start_date:
        :param end_date:
        :param docid:
        :param docid_i:
        :param insertRecordArr:
        :return:
        """
        while True:
            if self.ip_over == 1:
                break
            if start_time_stamp > end_time_stamp:
                break
            else:
                param = self.getUrlAndCookie(docid['name'], start_date, end_date)
                # 将已经处理过的条件存储记录
                insertArr = {
                    "table": "ws_record",
                    "id": "NEXT VALUE FOR LAW_WS_RECORD_SEQUENCE",
                    "start_date": start_date,
                    "end_date": end_date,
                    "court_id": str(docid['name'])
                }
                # self.ws_db.insert(insertArr, False)
                insertRecordArr['table'] = "ws_docid_record"
                insertRecordArr['court_name'] = docid['name']
                insertRecordArr['court_num'] = docid_i
                insertRecordArr['start_date'] = start_date
                insertRecordArr['court_year'] = start_record
                self.ws_db.insert(insertRecordArr)
                start_date = end_date
                start_time_stamp = start_time_stamp + self.config['interval_time_stamp']
                end_date = getDateTime(start_time_stamp, "%Y-%m-%d")
            threads = list()
            for i in range(thread_num):
                tmpK = i + 1
                threads.append(
                    ExecuteCurl("线程" + str(tmpK) + "：" + str(tmpK), param, self.proxy_ip, self.table_columns))
            for i in range(thread_num):
                threads[i].start()
                self.proxy_ip = threads[0].getLastProxyIp()
            for i in range(thread_num):
                threads[i].join()
            try:
                # 重置页码
                threads[0].reset()
            except:
                pass
            try:
                status = threads[0].getStatus()
                if status == 2:
                    debug("代理ip今日提取数已达上线")
                    break
            except:
                pass

    def getWenShuListContentOver(self):
        """
        :return:
        """
        # 启动多线程
        thread_num = self.config['thread_num']
        court = self.getCourtOver()
        # updateArr = {
        #     "table": "court",
        #     "set": ['is_handle=0']
        # }
        judge_i = 0
        for docid in court:
            if judge_i == 0:
                judge_i = judge_i + 1
                continue
            end_time_stamp = getTimeStamp(docid['end_date'], "%Y-%m-%d")
            # 开始时间
            start_date = docid['start_date']
            # 转化为时间戳
            start_time_stamp = getTimeStamp(start_date, "%Y-%m-%d")
            start_time_stamp = start_time_stamp + self.config['interval_time_stamp_over']
            end_date = getDateTime(start_time_stamp, "%Y-%m-%d")
            while True:
                if self.ip_over == 1:
                    break
                if start_time_stamp > end_time_stamp:
                    break
                else:
                    param = self.getUrlAndCookie(docid['court_name'], start_date, end_date)
                    # 将已经处理过的条件存储记录
                    insertArr = {
                        "table": "ws_record",
                        "id": "NEXT VALUE FOR LAW_WS_RECORD_SEQUENCE",
                        "start_date": start_date,
                        "end_date": end_date,
                        "court_id": str(docid['court_name'])
                    }
                    # self.ws_db.insert(insertArr, False)
                    start_date = end_date
                    start_time_stamp = start_time_stamp + self.config['interval_time_stamp_over']
                    end_date = getDateTime(start_time_stamp, "%Y-%m-%d")
                threads = list()
                for i in range(thread_num):
                    tmpK = i + 1
                    threads.append(
                        ExecuteCurl("线程" + str(tmpK) + "：" + str(tmpK), param, self.proxy_ip, self.table_columns))
                for i in range(thread_num):
                    threads[i].start()
                    self.proxy_ip = threads[0].getLastProxyIp()
                for i in range(thread_num):
                    threads[i].join()
                try:
                    # 重置页码
                    threads[0].reset()
                except:
                    pass
                try:
                    status = threads[0].getStatus()
                    if status == 2:
                        debug("代理ip今日提取数已达上线")
                        break
                except:
                    pass
            # DB = db.DBConfig()
            # updateArr['condition'] = ["id=%s" % str(docid['id'])]
            # updateResult = DB.update(updateArr, is_close_db=False)
            # DB.closeDB()
            debug("所有线程执行完毕，开始下一个任务")
            debug("\n等待五秒")
            sleep(5)

    def getWenShuListContentOverCaseType(self):
        """
        :return:
        """
        # 启动多线程
        thread_num = self.config['thread_num']
        court = self.getCourtOver()
        # updateArr = {
        #     "table": "court",
        #     "set": ['is_handle=0']
        # }
        caseList = ["刑事案件", "民事案件", "行政案件", "赔偿案件", "执行案件"]
        for docid in court:
            for time_i in range(2):
                for case_type in caseList:
                    if self.ip_over == 1:
                        break
                    else:
                        if time_i == 0:
                            param = self.getUrlAndCookieCaseType(docid['court_name'], docid['start_date'],
                                                                 docid['start_date'], case_type=case_type)
                        else:
                            param = self.getUrlAndCookieCaseType(docid['court_name'], docid['end_date'],
                                                                 docid['end_date'], case_type=case_type)
                        # 将已经处理过的条件存储记录
                        insertArr = {
                            "table": "ws_record",
                            "id": "NEXT VALUE FOR LAW_WS_RECORD_SEQUENCE",
                            "start_date": str(docid['start_date']),
                            "end_date": str(docid['end_date']),
                            "court_id": str(docid['court_name'])
                        }
                        # self.ws_db.insert(insertArr, False)
                    threads = list()
                    for i in range(thread_num):
                        tmpK = i + 1
                        threads.append(
                            ExecuteCurl("线程" + str(tmpK) + "：" + str(tmpK), param, self.proxy_ip, self.table_columns))
                    for i in range(thread_num):
                        threads[i].start()
                        self.proxy_ip = threads[0].getLastProxyIp()
                    for i in range(thread_num):
                        threads[i].join()
                    try:
                        # 重置页码
                        threads[0].reset()
                    except:
                        pass
                    try:
                        status = threads[0].getStatus()
                        if status == 2:
                            debug("代理ip今日提取数已达上线")
                            break
                    except:
                        pass
            # 删除此次条件的记录
            try:
                docid['table'] = "ws_over_record"
                docid['condition'] = ['"id"=%s' % str(docid['id'])]
                self.ws_db.delete(docid, is_close_db=False)
                debug("删除此条记录数据")
            except Exception as e:
                debug("删除记录失败：%s" % e.__str__())
            # DB = db.DBConfig()
            # updateArr['condition'] = ["id=%s" % str(docid['id'])]
            # updateResult = DB.update(updateArr, is_close_db=False)
            # DB.closeDB()
            debug("所有线程执行完毕，开始下一个任务")
            debug("\n等待五秒")
            sleep(5)

    def getCourt(self):
        selectArr = {
            "table": self.config["court"],
            "condition": ['court_type!=1', "and", "is_handle=0"],
            "columns": ['id', 'name']
        }
        DB = db.DBConfig()
        data = DB.select(selectArr, is_close_db=False)
        DB.closeDB()
        return data

    def getCourtOver(self):
        """
        :return:
        """
        selectArr = {
            "table": "ws_over_record"
        }
        data = self.ws_db.select(selectArr, is_close_db=False)
        return data

    def getWenShuList(self):
        """
        获取文书列表(同时存入数据库)
        :return:
        """
        self.setProxyIp()
        try:
            self.getWenShuListContent()
        except Exception as e:
            debug(e)
            self.getWenShuList()
        return "主线执行完毕"

    def getWenShuListOver(self):
        """
        获取文书列表(同时存入数据库)
        :return:
        """
        self.setProxyIp()
        try:
            self.getWenShuListContentOver()
        except Exception as e:
            debug(e)
            self.getWenShuListOver()
        return "主线执行完毕"

    def getWenShuListOverCaseType(self):
        """
        获取文书列表(同时存入数据库)
        :return:
        """
        self.setProxyIp()
        try:
            self.getWenShuListContentOverCaseType()
        except Exception as e:
            debug(e)
            self.getWenShuListOverCaseType()
        return "主线执行完毕"

    def getProxyIp(self):
        """
        进行proxy ip获取，并且存到数据库(law_proxy_ip)提供调用
        :return:
        """
        url = self.config['proxy_ip_url']
        # url = "https://nl.tan90.club/test/testHeader.html"
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
                v['time_stamp'] = str(getNowTimeStamp())
                tmp = k + 1
                try:
                    # 加锁
                    self.ws_db.insert(v, is_close_db=False)
                    # 解锁
                    debug("第" + str(tmp) + "条ip插入成功")
                except Exception as e:
                    debug("第" + str(tmp) + "条ip插入失败")
        except Exception as e:
            debug(e)
            debug("proxy ip 获取出错,睡眠5秒")
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
            getProxyIpResult = self.getProxyIp()
            if getProxyIpResult == 1:
                return 0
            data = self.getSingleProxyIp()
        return data

    def setProxyIp(self):
        self.proxy_ip = self.getSingleProxyIp()

    def getUrlAndCookie(self, court_name, start_date, end_date):
        """
        拼装url同时得到cookie
        :param court_name:
        :param start_date:
        :param end_date:
        :return: param 包含线程所需所有参数 (dict)
        """
        # 获取guid
        header_1 = {
            "User-Agent": getUserAgent(index=self.user_agent_index),
            "Origin": "http://wenshu.court.gov.cn"
        }
        num_flag = 0
        try:
            guid = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
            guid = json.loads(guid)
            guid = guid['guid']
            try:
                number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                  referer="http://wenshu.court.gov.cn",
                                  proxy_ip=self.proxy_ip, timeout=5)
                # number =
            except:
                number = "remind"
            while number.find("remind") != -1 or number.find("html") != -1 or number.find("服务不可用") != -1:
                if num_flag > 4:
                    self.setProxyIp()
                    num_flag = 0
                else:
                    num_flag = num_flag + 1
                debug("number获取出错，继续获取")
                try:
                    number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                      referer="http://wenshu.court.gov.cn",
                                      proxy_ip=self.proxy_ip, timeout=5)
                except Exception as e:
                    debug(e)
                sleep(0.5)
        except Exception as e:
            debug(e)
            debug("guid获取出错")
            return self.getUrlAndCookie(court_name, start_date, end_date)
        # 拼装url
        url = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=%s&guid=%s&conditions=searchWord+%s+SLFY++%s&conditions=searchWord++CPRQ++%s%%20TO%%20%s" % (
            number, guid, urllib.parse.quote(str(court_name)), urllib.parse.quote("法院名称:%s" % court_name),
            urllib.parse.quote(str(start_date)), urllib.parse.quote(str(end_date)))
        cookie = self.getCookie(url)
        while cookie == 0:
            self.setProxyIp()
            cookie = self.getCookie(url)
        try:
            vjkl5 = cookie['vjkl5']
        except:
            debug("vjk5获取失败，重新获取")
            if self.is_change_proxy > 4:
                self.setProxyIp()
                self.is_change_proxy = 0
            else:
                self.is_change_proxy = self.is_change_proxy + 1
            return self.getUrlAndCookie(court_name, start_date, end_date)
        try:
            post = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=" + vjkl5)
            # post['guid'] = guid
        except:
            post = "{}"
            debug("post参数获取出错")
        post = json.loads(post)
        post['Order'] = "法院层级"
        post['Page'] = 10
        post['guid'] = guid
        post['number'] = number[0:4]
        post['Direction'] = "asc"
        header = {
            "User-Agent": getUserAgent(index=self.user_agent_index),
            "Origin": "http://wenshu.court.gov.cn"
        }
        param = {
            "vjkl5": vjkl5,
            "post": post,
            "header": header,
            "cookie_all": cookie,
            "url": url,
            "court_name": court_name,
            "start_date": start_date,
            "end_date": end_date
        }
        param['post']['Param'] = "法院名称:%s,裁判日期:%s TO %s" % (court_name, start_date, end_date)
        return param

    def getYear(self, court_name):
        """
        拼装url同时得到cookie
        :param court_name:
        :return: 所有有数据的年份
        """
        # 获取guid
        header_1 = {
            "User-Agent": getUserAgent(index=self.user_agent_index),
            "Origin": "http://wenshu.court.gov.cn"
        }
        try:
            guid = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
            guid = json.loads(guid)
            guid = guid['guid']
            # number = ""
            num_flag = 0
            try:
                number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                  referer="http://wenshu.court.gov.cn",
                                  proxy_ip=self.proxy_ip, timeout=5)
            except:
                number = "remind"
            while number.find("remind") != -1 or number.find("html") != -1 or number.find("服务不可用") != -1:
                if num_flag > 4:
                    self.setProxyIp()
                    num_flag = 0
                else:
                    num_flag = num_flag + 1
                debug("number获取出错，继续获取")
                try:
                    number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                      referer="http://wenshu.court.gov.cn",
                                      proxy_ip=self.proxy_ip, timeout=5)
                except Exception as e:
                    debug(e)
                sleep(0.5)
        except Exception as e:
            debug("guid获取出错")
            return self.getYear(court_name)
        # 拼装url
        url = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=%s&guid=%s&conditions=searchWord+%s+SLFY++%s" % (
            number, guid, urllib.parse.quote(str(court_name)), urllib.parse.quote("法院名称:%s" % court_name))
        cookie = self.getCookie(url)
        while cookie == 0:
            self.setProxyIp()
            cookie = self.getCookie(url)
        try:
            vjkl5 = cookie['vjkl5']
        except:
            debug("vjkl5获取失败，重新获取")
            if self.is_change_proxy > 4:
                self.setProxyIp()
                self.is_change_proxy = 0
            else:
                self.is_change_proxy = self.is_change_proxy + 1
            return self.getYear(court_name)
        try:
            post = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=" + vjkl5)
        except:
            post = "{}"
            debug("post参数获取出错")
        post = json.loads(post)
        post['number'] = number
        post['guid'] = guid
        header = {
            "User-Agent": getUserAgent(index=self.user_agent_index),
            "Origin": "http://wenshu.court.gov.cn"
        }
        post['Param'] = "法院名称:%s" % court_name
        year = curlData("http://wenshu.court.gov.cn/List/TreeContent", post, url, cookie, header, self.proxy_ip,
                        timeout=5)
        try:
            year = json.loads(year)
            year = json.loads(year)
        except:
            pass
        return year[4]['Child']

    def getUrlAndCookieCaseType(self, court_name, start_date, end_date, case_type):
        """
        拼装url同时得到cookie
        :param court_name:
        :param start_date:
        :param end_date:
        :param case_type
        :return: param 包含线程所需所有参数 (dict)
        """
        # 获取guid
        header_1 = {
            "User-Agent": getUserAgent(index=self.user_agent_index),
            "Origin": "http://wenshu.court.gov.cn"
        }
        try:
            num_flag = 0
            guid = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
            guid = json.loads(guid)
            guid = guid['guid']
            number = ""
            # try:
            #     number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
            #                       referer="http://wenshu.court.gov.cn",
            #                       proxy_ip=self.proxy_ip, timeout=5)
            # except:
            #     number = "remind"
            # while number.find("remind") != -1 or number.find("html") != -1 or number.find("服务不可用") != -1:
            #     if num_flag > 4:
            #         self.setProxyIp()
            #         num_flag = 0
            #     else:
            #         num_flag = num_flag + 1
            #     debug("number获取出错，继续获取")
            #     try:
            #         number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
            #                           referer="http://wenshu.court.gov.cn",
            #                           proxy_ip=self.proxy_ip, timeout=5)
            #     except Exception as e:
            #         debug(e)
            #     sleep(0.5)
        except:
            debug("guid获取出错")
            return self.getUrlAndCookieCaseType(court_name, start_date, end_date, case_type)
        # 拼装url
        url = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=%s&guid=%s&conditions=searchWord+%s+SLFY++%s&conditions=searchWord++CPRQ++%s%%20TO%%20%s&conditions=searchWord+%s+AJLX++%s" % (
            number, guid, urllib.parse.quote(str(court_name)), urllib.parse.quote("法院名称:%s" % court_name),
            urllib.parse.quote(str(start_date)), urllib.parse.quote(str(end_date)),
            str(self.getCaseTypeIndex(case_type)), urllib.parse.quote(str("案件类型:%s" % case_type)))
        cookie = self.getCookie(url)
        while cookie == 0:
            self.setProxyIp()
            cookie = self.getCookie(url)
        try:
            vjkl5 = cookie['vjkl5']
        except:
            debug("vjk5获取失败，重新获取")
            if self.is_change_proxy > 4:
                self.setProxyIp()
                self.is_change_proxy = 0
            else:
                self.is_change_proxy = self.is_change_proxy + 1
            return self.getUrlAndCookieCaseType(court_name, start_date, end_date, case_type)
        try:
            post = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=" + vjkl5)
        except:
            post = "{}"
            debug("post参数获取出错")
        post = json.loads(post)
        post['Order'] = "法院层级"
        post['Page'] = 20
        post['number'] = "wens"
        post['Direction'] = "asc"
        header = {
            "User-Agent": getUserAgent(index=self.user_agent_index),
            "Origin": "http://wenshu.court.gov.cn"
        }
        param = {
            "vjkl5": vjkl5,
            "post": post,
            "header": header,
            "cookie_all": cookie,
            "url": url,
            "court_name": court_name,
            "start_date": start_date,
            "end_date": end_date
        }
        param['post']['Param'] = "法院名称:%s,裁判日期:%s TO %s,案件类型:%s" % (court_name, start_date, end_date, case_type)
        return param

    def getCaseTypeIndex(self, case_type):
        """
        :param case_type:
        :return:
        """
        caseList = ["刑事案件", "民事案件", "行政案件", "赔偿案件", "执行案件"]
        return caseList.index(case_type) + 1

    def getNumber(self, guid, header_1, proxy_ip, referer="http://wenshu.court.gov.cn", cookie=False):
        num_flag = 0
        try:
            if not cookie:
                number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                  referer=referer,
                                  proxy_ip=proxy_ip, timeout=5)
            else:
                number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                  referer=referer, cookie=cookie,
                                  proxy_ip=proxy_ip, timeout=5)
        except:
            number = "remind"
        while number.find("remind") != -1 or number.find("html") != -1 or number.find("服务不可用") != -1:
            if num_flag > 4:
                proxy_ip = GetProxyIp().getProxyIp()
                num_flag = 0
            else:
                num_flag = num_flag + 1
            debug("number获取出错，继续获取")
            try:
                guidGet = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=0")
                guid = guidGet['guid']
            except:
                pass
            try:
                if not cookie:
                    number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                      referer=referer,
                                      proxy_ip=proxy_ip, timeout=5)
                else:
                    number = curlData("http://wenshu.court.gov.cn/ValiCode/GetCode", {"guid": guid}, header=header_1,
                                      referer=referer, cookie=cookie,
                                      proxy_ip=proxy_ip, timeout=5)
            except Exception as e:
                debug(e)
            sleep(0.5)
