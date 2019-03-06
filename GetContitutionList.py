import re
from time import sleep
from urllib.parse import urlencode

from ConstitutionThread import ConstitutionThread
from bs4 import BeautifulSoup
from tool.db import DBConfig
from selenium import webdriver
from tool.function import virtualIp, debug, curlData
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.options import Options


# noinspection PyBroadException,PyMethodMayBeStatic,PyPep8Naming,PyInterpreter
class GetConstitutionList(object):
    def __init__(self):
        # 数据库连接全局变量
        # self.ws_db = phoenix_db.DBConfig()
        self.count = 0
        self.db = DBConfig()

    def __del__(self):
        self.db.closeDB()
        debug("本次一共获取到了%s条数据" % str(self.count))
        # self.ws_db.closeDB()

    def getAllConstitutionStart(self):
        try:
            record = self.db.select({"table": "constitutions_record", "condition": ['is_over=0']}, is_close_db=False)
            next_page = record[0]['page']
        except:
            next_page = 1
        while True:
            try:
                data = self.getConstitutionList(next_page)
            except:
                debug("内容获取出错，重新获取")
                continue
            # 获取下一页的页码
            try:
                tmpNextPage = re.findall('href="javascript:toUpDownPage\(\'(\d+)\'\);">下一页<\/a>', data)[0]
                debug("当前的页码是：%s" % str(next_page))
                debug("获取到的下一页页码是：%s" % str(tmpNextPage))
            except:
                debug("下一页的页码获取出错")
                break
            self.getAllConstitutionHandle(data, "北京")
            updatetArr = {
                "table": "constitutions_record",
                "condition": ['id=2'],
                "set": {
                    "page": tmpNextPage,
                    "is_over": 0
                }
            }
            self.db.update(updatetArr, is_close_db=False)
            if int(next_page) >= int(tmpNextPage):
                break
            else:
                next_page = tmpNextPage
        debug("本次抓取完毕")
        updatetArr = {
            "table": "constitutions_record",
            "condition": ['id=2'],
            "set": {
                "is_over": 1
            }
        }
        self.db.update(updatetArr, is_close_db=False)

    def getAllConstitution(self, fun):
        """
        获取所有法律法规
        :param fun:
        :return:
        """
        url = "http://210.82.32.100:8081/FLFG/"
        dcap = dict(DesiredCapabilities.FIREFOX)
        ip = virtualIp()
        dcap['phantomjs.page.customHeaders.X-FORWARDED-FOR'] = ip
        dcap['phantomjs.page.customHeaders.CLIENT-IP'] = ip
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(firefox_options=firefox_options, desired_capabilities=dcap)
        driver.get(url)
        sleep(3)
        cloumn = driver.find_elements_by_class_name("cloumn")
        try:
            cloumn = cloumn[3]
        except:
            while True:
                try:
                    cloumn = cloumn[3]
                    break
                except:
                    sleep(1)
        cloumntitle = cloumn.find_elements_by_class_name("threecloumntitle")
        cloumntitleLength = len(cloumntitle)
        current_handle = driver.current_window_handle
        for i in range(cloumntitleLength):
            try:
                list_a = cloumntitle[i].find_elements_by_tag_name("a")
            except:
                list_a = list()
                debug("省份列表获取出错")
            list_a_len = len(list_a)
            for k in range(list_a_len):
                # 获取省份名
                try:
                    province = list_a[k].text
                except:
                    debug("省份获取出错，继续执行，省份标记锚点为" + str(k))
                    province = str(k)
                debug(province + "：")
                try:
                    list_a[k].click()
                except:
                    debug("点击失败")
                sleep(3)
                all_handles = driver.window_handles
                sleep(3)
                for handle in all_handles:
                    if handle != current_handle:
                        driver.switch_to_window(handle)
                        sleep(1)
                        data = driver.page_source
                        htmlData = BeautifulSoup(data, "html.parser")
                        try:
                            url = htmlData.find_all("iframe", attrs={"id": "rightpage"})[0].attrs['src']
                            url = re.sub("(有效)", "有效,已被修正,失效", url)
                            driver.execute_script("location.href='" + url + "'")
                            sleep(3)
                            # 进行点击50篇每页
                            try:
                                driver.find_element_by_id("span_pagesize_50").click()
                                sleep(3)
                            except:
                                pass
                            data = driver.page_source
                            # 获取每一页的text以便稍后判断
                            try:
                                nextPage = re.findall(r'<a[\w\W]*?href="([\w\W]*?)">下一页', data)
                                nextPage = re.findall(r'<a[\w\W]*?href="([\w\W]*?)\)', nextPage[0])
                                nextPage = re.findall("(\d+)", nextPage[1])
                                nextPage = nextPage[0]
                            except:
                                nextPage = 0
                            # 处理数据
                            while True:
                                tmpPage = int(nextPage) - 1
                                debug("第" + str(tmpPage) + "页：")
                                fun(data, province)
                                nextPageElement = driver.find_element_by_class_name("td")
                                try:
                                    nextPageElement = nextPageElement.find_elements_by_tag_name("a")[1]
                                    nextPageElement.click()
                                    sleep(3)
                                    data = driver.page_source
                                    try:
                                        tmpNextPage = re.findall(r'<a[\w\W]*?href="([\w\W]*?)">下一页', data)
                                        tmpNextPage = re.findall(r'<a[\w\W]*?href="([\w\W]*?)\)', tmpNextPage[0])
                                        tmpNextPage = re.findall("(\d+)", tmpNextPage[1])
                                        tmpNextPage = tmpNextPage[0]
                                        if nextPage == tmpNextPage:
                                            break
                                        else:
                                            nextPage = tmpNextPage
                                    except:
                                        break
                                except:
                                    break
                            # 点击下一页
                        except Exception as e:
                            debug(e)
                        debug("")
                        driver.close()
                        sleep(1)
                        driver.switch_to_window(all_handles[0])
                        sleep(2)
        driver.quit()

    def getConstitutionList(self, cur_page):
        url = "http://210.82.32.100:8081/FLFG/flfgGjjsAction.action"
        referer = "http://210.82.32.100:8081/FLFG/flfgGjjsAction.action"
        post = {
            "pagesize": "20",
            "pageCount": "500",
            "curPage": cur_page,
            "resultSearch": "false",
            # "lastStrWhere": "+SFYX:(有效)++^+ZLSX:(01~02~03~04~05~06~08~09~10~11~12~23)+NOT+TXTID=bj+^+SFFB=Y+",
            "lastStrWhere": "  SFYX:(有效~已被修正~失效) ^(ZLSX:1111 ~ZLSX=01)  ^ BMFL:(03)  ^ SFFB=Y ",
            "bt": "",
            "flfgnr": "",
            "sxx": "有效,已被修正,失效",
            # "sxx": "有效",
            "zlsxid": "12",
            "bmflid": "",
            "xldj": "",
            "bbrqbegin": "2018-09-01",
            "bbrqend": "2018-12-17",
            "sxrqbegin": "",
            "sxrqend": "",
            "zdjg": "",
            "bbwh": ""
        }
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
        }
        data = curlData(url=url, value=post, referer=referer, header=header)
        return data

    def getAllConstitutionHandle(self, data, province):
        data = re.findall(r'<a[\w\W]*?href="javascript:showLocation([\w\W]*?);"', data)
        old1 = ""
        old5 = ""
        i = 0
        thread_list = list()
        for k, v in enumerate(data):
            data[k] = tuple(v.split("'"))
            try:
                if data[k][1] == old1 and data[k][7] == old5:
                    continue
                i = i + 1
                thread_list.append(ConstitutionThread(data[k][1], data[k][7], data[k][3], province, i))
                old1 = data[k][1]
                old5 = data[k][7]
            except:
                pass
        i = len(thread_list)
        for m in range(i):
            thread_list[m].start()
        for m in range(i):
            thread_list[m].join()
        i = thread_list[0].getRv()
        # 重置计数器
        thread_list[0].reset()
        self.count = self.count + i
        return 1

    def getConstitutionData(self, flfgID, zlsxid, showDetailType, province):
        # 经过浏览。很明显，具体的宪法数据源url为如下的url,包含两个get类型参数  flfgID zlsxid keyword 前两个是必须的，通过列表传递的js数据拿到
        flag = False
        url = "http://210.82.32.100:8081/FLFG/flfgByID.action"
        get = dict()
        get['flfgID'] = flfgID
        get['showDetailType'] = showDetailType
        get['zlsxid'] = zlsxid
        get['keyword'] = ""
        get = urlencode(get)
        url = url + "?" + get
        while True:
            try:
                data = curlData(url, get, url)
                break
            except:
                pass
        try:
            data = data.decode("utf-8")
        except:
            pass
        # with open("constitution.txt", "wb") as f:
        #     f.write(data.encode("utf-8"))
        #     f.close()
        # with open("constitution.txt", "rb") as f:
        #     data = f.read().decode("utf-8")
        #     f.close()
        handleDataAll = BeautifulSoup(data, "html.parser")
        handleData = handleDataAll.find_all("table")
        columns_list = ['type', "department_type", 'office', 'reference_num', 'issue_date', 'execute_date',
                        'timeliness']
        columns_name_list = ['资料属性：', '部门分类：', '制定机关：', '颁布文号：', '颁布日期：', '施行日期：', '时 效 性：']
        # 获取头部基本信息
        try:
            table_data = handleData[0].find_all("td")
        except:
            table_data = "数据获取出错"
            flag = True
        type_data = dict()
        type_data['url'] = url
        for k, v in enumerate(table_data):
            try:
                if (k + 1) % 2 == 1:
                    type_data[columns_list[columns_name_list.index(table_data[k].getText().strip())]] = table_data[
                        k + 1].getText().strip()
            except:
                type_data[columns_list[columns_name_list.index(table_data[k].getText().strip())]] = "数据获取出错"
        # 接下来获取标题和内容
        try:
            type_data['title'] = handleDataAll.find_all("div", attrs={"class": "bt"})[0].getText().strip()
        except:
            type_data['title'] = "标题获取出错"
            flag = True
        # 进行内容获取
        try:
            type_data['content'] = str(handleDataAll.find_all("div", attrs={"id": "content"})[0])
        except:
            flag = True
        type_data['province'] = province
        if flag:
            type_data['is_get_error'] = 1
        else:
            type_data['is_get_error'] = 0
        while True:
            try:
                sql = self.db.getInsertSql(type_data, "constitutions")
                result = self.db.insert(sql, is_close_db=False)
                break
            except Exception as e:
                debug(e)
        return result
