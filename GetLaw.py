from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver import DesiredCapabilities
from tool.function import curlData
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from tool.function import virtualIp
from tool.function import debug
from bs4 import BeautifulSoup
from tool.db import DBConfig
from tool import phoenix_db
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import re
import json
from tool.function import getTimeStamp


# noinspection PyMethodMayBeStatic,PyBroadException
class GetLaw(object):
    def __init__(self):
        # 数据库连接全局变量
        self.ws_db = phoenix_db.DBConfig()
        # 全局代理IP
        self.proxy_ip = ""

    def __del__(self):
        self.ws_db.closeDB()

    def setProxyIp(self):
        self.proxy_ip = self.getSingleProxyIp()

    """
    自定义的抓取函数，这个可以针对一般的页面进行抓取，效率高
    但是有js加载数据的页面不能抓取到所有数据，需要获取js加载的数据的时候建议使用getDataSelenium函数进行抓取
    is_save_file 是否存储抓取到的数据到文件(可以加快处理效率，不然每次处理都需要进行抓取，调试的时候消耗时间和资源)，默认为False
    有参数 url 要抓取的页面的url连接地址，必须
    """

    def getData(self, url, is_save_file=False):
        """
        :param url:
        :param is_save_file:
        :return:
        """
        data = curlData(url, referer=url)
        data = data.encode("utf-8")
        if is_save_file:
            with open("origin_data/data.txt", "wb") as f:
                f.write(data)
                f.close()
        return data.decode("utf-8")

    """
    通过phantomjs获取数据
    有参数 url 要抓取的页面的url连接地址，必须
    sleep_time 睡眠时间，默认为0，这个参数是考虑到有的网站ajax异步加载数据，所以可能会延迟几秒再获取数据(例如裁判文书网)
    is_save_file 是否存储抓取到的数据到文件(可以加快处理效率，不然每次处理都需要进行抓取，调试的时候消耗时间和资源)，默认为False
    """

    def getDataSelenium(self, url, sleep_time=0, is_save_file=False, file_name="1"):
        """
        :param url: the url which you want to get data of page
        :param sleep_time: default is 0
        :param is_save_file: default is False
        :param file_name: default file is origin_data/data.txt
        :return:
        """
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.referer'] = url
        dcap['phantomjs.page.customHeaders.User-Agent'] = "baiduspider"
        # ip = virtualIp()
        service_args = [
            '--proxy=%s' % self.proxy_ip,
            '--proxy-type=http',
            '--load-images=no',
            '--disk-cache=yes',
            '--ignore-ssl-errors=true'
        ]
        # dcap['phantomjs.page.customHeaders.X-FORWARDED-FOR'] = ip
        # dcap['phantomjs.page.customHeaders.CLIENT-IP'] = ip
        driver = webdriver.PhantomJS(
            desired_capabilities=dcap, service_args=service_args)
        driver.get(url)
        sleep(sleep_time)
        data = driver.page_source
        try:
            data = data.encode("utf-8")
        except:
            pass
        if is_save_file:
            if file_name == "1":
                file_name = "origin_data/data.txt"
            with open(file_name, "wb") as f:
                f.write(data)
                f.close()
        driver.quit()
        try:
            data = data.decode("utf-8")
        except:
            pass
        return data

    """
    待更新，有时间就切换掉，切换为最新的用Firefox跑
    暂时弃用
    """

    def getDataSeleniumNew(self, url, is_save_file=False):
        """
        :param url:
        :param is_save_file:
        :return:
        """
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(firefox_options=firefox_options)
        driver.get(url)
        data = driver.page_source.encode("utf-8")
        if is_save_file:
            with open("origin_data/data.txt", "wb") as f:
                f.write(data)
                f.close()
        driver.quit()
        return data.decode("utf-8")

    def getDataSeleniumChrome(self, url, sleep_time=0, is_save_file=False, file_name="1"):
        """
        :param url: the url which you want to get data of page
        :param sleep_time: default is 0
        :param is_save_file: default is False
        :param file_name: default file is origin_data/data.txt
        :return:
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"')
        chrome_options.add_argument('Referer="www"')
        # debug("本次的代理ip为：" + self.proxy_ip)
        x_for = '--proxy-server=' + self.proxy_ip
        debug(x_for)
        # 设置代理
        chrome_options.add_argument(x_for)
        debug("开始启动chrome")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        debug("启动成功")
        try:
            debug("开始打开url")
            driver.get(url)
        except Exception as e:
            driver.quit()
            debug(e)
            return ""
        debug("打开成功，开始等待加载数据")
        # driver.implicitly_wait(15)
        sleep(sleep_time)
        data = driver.page_source
        debug("等待完毕")
        debug("关闭浏览器")
        driver.quit()
        debug("返回数据")
        return data

    def getWenshuPlace(self):
        """
        获取所有法院名称
        :return: None
        """
        url = "http://wenshu.court.gov.cn/"
        # url = "http://wenshu.court.gov.cn/content/content?DocID=532bd8ed-4ba8-48b7-ad70-0063f64ede05"
        dcap = dict(DesiredCapabilities.FIREFOX)
        ip = virtualIp()
        dcap['phantomjs.page.customHeaders.X-FORWARDED-FOR'] = ip
        dcap['phantomjs.page.customHeaders.CLIENT-IP'] = ip
        # driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ssl-protocol=any'])
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(firefox_options=firefox_options, desired_capabilities=dcap)
        driver.get(url)
        driver_list = driver.find_elements_by_class_name("map_p")
        length = len(driver_list)
        debug("开始")
        result = list()
        DB = DBConfig()
        oldProvince = ""
        is_click = False
        self_top = 18
        for k in range(length):
            if self_top == 18:
                k = self_top
                self_top = self_top + 1
            else:
                break
            tmp = dict()
            i = 0
            try:
                driver.execute_script("var q = document.getElementsByClassName('map_p map_p_xianggang')[0].style.display='none';")
                sleep(2)
                if not is_click:
                    driver_list[k].click()
                else:
                    driver.find_element_by_id("btCourt").click()
            except Exception as e:
                debug(e.__str__())
                debug("获取出错")
                continue
            for wait_time in range(30):
                debug("等第%s秒" % str(wait_time), True)
                sleep(1)
            initScroll = 1193
            driver.execute_script("var q = document.documentElement.scrollTop=" + str(
                initScroll) + ";document.getElementById('bottom').style.display='none';document.getElementsByClassName('region')[0].style.overflow='visible'")
            sleep(1)
            data = driver.page_source
            handleData = BeautifulSoup(data, "html.parser")
            # 获取省份
            try:
                provinceName = handleData.find_all("div", attrs={"class": "area"})[0]
                # 新疆比较特殊,有兵团和新疆两个区域,所以要判断一下是否是新疆，是的话特殊处理
                provinceName = "".join(provinceName.getText().strip().split())
                if provinceName.find("新疆") != -1:
                    if is_click:
                        provinceName = "".join(
                            handleData.find_all("a", attrs={"id": "btCourt"})[0].getText().strip().split())
                        is_click = False
                    else:
                        provinceName = "新疆"
                        is_click = True
            except:
                debug("省份获取出错")
                continue
            if provinceName == oldProvince and not is_click:
                # 获取当前点击了的省份名字
                try:
                    provinceName = "".join(
                        handleData.find("div", attrs={"class": "map_p"})[k].getText().strip().split())
                except:
                    provinceName = "省份获取出错"
                tmp['name'] = provinceName
                debug("\n" + provinceName + "：")
                tmp['court_type'] = 1
                first_id = DB.insertLastId(DB.getInsertSql(tmp, "court"), False)
                continue
            else:
                oldProvince = provinceName
            tmp['name'] = provinceName
            debug("\n" + provinceName + "：")
            tmp['court_type'] = 1
            first_id = DB.insertLastId(DB.getInsertSql(tmp, "court"), False)
            i = i + 1
            if first_id != 0:
                result_remind = "第" + str(i) + "条数据获取成功" + "：" + tmp['name']
            else:
                result_remind = "第" + str(i) + "条数据获取失败"
            result.append(result_remind)
            debug(result_remind)
            # 获取省份对应的所有法院大类名
            secondLists = driver.find_element_by_class_name("region")
            secondLists = secondLists.find_elements_by_class_name("index_divchildcourt_arrow")
            secondLength = len(secondLists)
            try:
                secData = handleData.find_all("div", attrs={"class": "region"})[0]
                secData = secData.find_all("a")
                for key, v in enumerate(secData):
                    secData[key] = v.getText().strip()
            except:
                secData = list()
            for sk in range(secondLength):
                tmpSec = dict()
                try:
                    tmpSec['name'] = secData[sk]
                except:
                    tmpSec['name'] = "法院名字获取错误"
                tmpSec['court_type'] = 2
                tmpSec['parent_id'] = first_id
                second_id = DB.insertLastId(DB.getInsertSql(tmpSec, "court"), False)
                i = i + 1
                if second_id != 0:
                    result_remind = "\n第" + str(i) + "条数据获取成功" + "：" + tmpSec['name'] + "\n"
                else:
                    result_remind = "\n第" + str(i) + "条数据获取失败\n"
                result.append(result_remind)
                debug(result_remind)
                if tmpSec['name'].find("高级人民法院") != -1 or tmpSec['name'].find("最高人民法院") != -1:
                    continue
                # 判断div里的滚动条高度，用递归判断，防止出错
                # self.getWenShuPlaceCheckScroll(driver, element=secondLists[sk])
                # sleep(2)
                try:
                    ActionChains(driver).move_to_element(secondLists[sk]).perform()
                    sleep(1)
                except Exception as e:
                    flag = True
                    if isinstance(e, MoveTargetOutOfBoundsException):
                        debug("超出可视范围，尝试拉动滚动条")
                        initScroll = initScroll + 600
                        driver.execute_script("var q = document.documentElement.scrollTop=" + str(initScroll))
                        sleep(1)
                        while flag:
                            try:
                                ActionChains(driver).move_to_element(secondLists[sk]).perform()
                                flag = False
                                debug("拉动滚动条成功")
                                break
                            except Exception as e:
                                if isinstance(e, MoveTargetOutOfBoundsException):
                                    debug("超出可视范围，尝试拉动滚动条")
                                    initScroll = initScroll + 600
                                    driver.execute_script(
                                        "var q = document.documentElement.scrollTop=" + str(initScroll))
                                    debug(initScroll)
                                    sleep(1)
                newData = driver.page_source
                newData = BeautifulSoup(newData, "html.parser")
                newData = newData.find_all("div", attrs={"class": "index_divchildcourt_center"})[0]
                newData = newData.find_all("a")
                for key, value in enumerate(newData):
                    # sleep(2)
                    tmpThird = dict()
                    tmpThird['name'] = newData[key].getText()
                    tmpThird['court_type'] = 3
                    tmpThird['parent_id'] = second_id
                    tmpThird['first_parent_id'] = first_id
                    result_id = DB.insertLastId(DB.getInsertSql(tmpThird, "court"), False)
                    i = i + 1
                    if result_id != 0:
                        result_remind = "第" + str(i) + "条数据获取成功" + "：" + tmpThird['name']
                    else:
                        result_remind = "第" + str(i) + "条数据获取失败"
                    result.append(result_remind)
                    debug(result_remind)
            # sleep(1)
        try:
            driver.quit()
            DB.closeDB()
        except:
            pass

        return result

    def getConstitutionPlace(self):
        """
        获取所有法律法规的行政区划
        :return: None
        """
        url = "http://202.108.98.30/map"
        # url = "http://wenshu.court.gov.cn/content/content?DocID=532bd8ed-4ba8-48b7-ad70-0063f64ede05"
        dcap = dict(DesiredCapabilities.FIREFOX)
        ip = virtualIp()
        dcap['phantomjs.page.customHeaders.X-FORWARDED-FOR'] = ip
        dcap['phantomjs.page.customHeaders.CLIENT-IP'] = ip
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument('--disable-gpu')
        driver = webdriver.Firefox(firefox_options=firefox_options, desired_capabilities=dcap)
        driver.get(url)
        # 首先拿到省级下拉列表(driver对象)
        shengji = driver.find_element_by_name("shengji")
        # 获取一共有多少个省
        shengjiLength = len(shengji.find_elements_by_tag_name("option"))
        shengji = Select(shengji)
        sleep(2)
        data = driver.page_source
        handleData = BeautifulSoup(data, "html.parser")
        shengjiData = handleData.find_all("select", attrs={"name": "shengji"})
        try:
            shengjiData = shengjiData[0].find_all("option")
        except:
            return "异常，未知"
        DB = DBConfig()
        result = list()
        for k in range(shengjiLength):
            if k == 0:
                continue
            # i为计数器
            i = 0
            try:
                shengji.select_by_index(k)
                sleep(2)
            except:
                debug("数据获取出错")
                continue
            tmp = dict()
            try:
                tmp['name'] = "".join(shengjiData[k].getText().strip().split())
            except:
                debug("省获取出错")
                continue
            tmp['type'] = 1
            # 省级插入
            first_id = DB.insertLastId(DB.getInsertSql(tmp, "place"), False)
            i = i + 1
            if first_id == 0:
                result_remind = "第" + str(i) + "条数据获取失败"
            else:
                result_remind = "第" + str(i) + "条数据获取成功" + "：" + tmp['name']
            debug(result_remind)
            result.append(result_remind)
            diji = driver.find_element_by_name("diji")
            diji = Select(diji)
            data = driver.page_source
            handleData = BeautifulSoup(data, "html.parser")
            dijiData = handleData.find_all("select", attrs={"name": "diji"})
            try:
                dijiData = dijiData[0].find_all("option")
            except:
                continue
            dijiLength = len(dijiData)
            for dk in range(dijiLength):
                if dk == 0 and dijiLength > 1:
                    continue
                try:
                    diji.select_by_index(dk)
                    sleep(2)
                except:
                    debug("数据获取出错")
                    continue
                tmpDiji = dict()
                try:
                    tmpDiji['name'] = "".join(dijiData[dk].getText().strip().split())
                except:
                    debug("地级市获取出错")
                    continue
                tmpDiji['type'] = 2
                tmpDiji['parent_id'] = first_id
                second_id = DB.insertLastId(DB.getInsertSql(tmpDiji, "place"), False)
                i = i + 1
                if second_id == 0:
                    result_remind = "第" + str(i) + "条数据获取失败"
                else:
                    result_remind = "第" + str(i) + "条数据获取成功" + "：" + tmpDiji['name']
                debug(result_remind)
                result.append(result_remind)
                data = driver.page_source
                handleData = BeautifulSoup(data, "html.parser")
                xianjiData = handleData.find_all("select", attrs={"name": "xianji"})
                try:
                    xianjiData = xianjiData[0].find_all("option")
                except:
                    continue
                xianjiLength = len(xianjiData)
                for xk in range(xianjiLength):
                    if xk == 0 and xianjiLength > 1:
                        continue
                    tmpXianji = dict()
                    try:
                        tmpXianji['name'] = "".join(xianjiData[xk].getText().strip().split())
                    except:
                        debug("县级获取出错")
                        continue
                    tmpXianji['type'] = 3
                    tmpXianji['parent_id'] = second_id
                    result_id = DB.insertLastId(DB.getInsertSql(tmpXianji, "place"), False)
                    i = i + 1
                    if result_id == 0:
                        result_remind = "第" + str(i) + "条数据获取失败"
                    else:
                        result_remind = "第" + str(i) + "条数据获取成功" + "：" + tmpXianji['name']
                    debug(result_remind)
                    result.append(result_remind)
                    sleep(1)
        sleep(1)
        try:
            DB.closeDB()
            driver.close()
        except:
            pass
        return result

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

    def getCaseReason(self):
        """
        获取案由
        :return:
        """
        url = "http://wenshu.court.gov.cn/"
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
        data = ""
        DB = phoenix_db.DBConfig()
        try:
            # 首先点击高级检索
            driver.find_element_by_id("head_maxsearch_btn").click()
            sleep(1)
            # 点击案由，打开选择列表
            driver.find_element_by_id("selectTree2_input").click()
            sleep(1)
            list_reason = driver.find_element_by_id("selectTree2_container").find_elements_by_tag_name("li")
            reason_parent_id_sql = "select current value for law_case_reason_sequence"
            reason_insert_dict = {
                "id": r" NEXT VALUE FOR LAW_CASE_REASON_SEQUENCE",
                # "case_type": 1,
                # "parent_id": 0
            }
            for k, reason in enumerate(list_reason):
                # 第一个为请选择，直接跳过，continue
                if k == 0:
                    continue
                try:
                    # 获取第一级
                    reason_1_span = reason.find_elements_by_tag_name("span")
                    reason_insert_dict['table'] = "case_reason"
                    reason_insert_dict['case_name'] = reason_1_span[2].text
                    reason_insert_dict['case_type'] = 1
                    reason_insert_dict['parent_id'] = 0
                    # 进行存储
                    result = DB.insert(reason_insert_dict, False)
                    reason_1_parent_id = DB.free(reason_parent_id_sql, False)[0][0]
                    debug(reason_1_parent_id)
                    if result == 0:
                        debug("第" + str(reason_1_parent_id) + "条插入失败")
                        continue
                    else:
                        debug("第" + str(reason_1_parent_id) + "条插入成功")
                    # debug(reason_1_dict)
                    reason_1_span[0].click()
                    sleep(1)
                    # 获取第二级
                    reason_2_ul = reason.find_element_by_tag_name("ul")
                    reason_2_li = reason_2_ul.find_elements_by_tag_name("li")
                    for k2, reason_2 in enumerate(reason_2_li):
                        reason_insert_dict['table'] = "case_reason"
                        reason_insert_dict['case_name'] = reason_2.text
                        reason_insert_dict['case_type'] = 2
                        reason_insert_dict['parent_id'] = reason_1_parent_id
                        result = DB.insert(reason_insert_dict, False)
                        reason_2_parent_id = DB.free(reason_parent_id_sql, False)[0][0]
                        if result == 0:
                            debug("第" + str(reason_2_parent_id) + "条插入失败")
                            continue
                        else:
                            debug("第" + str(reason_2_parent_id) + "条插入成功")
                        reason_2_span = reason_2.find_elements_by_tag_name("span")
                        reason_2_span[0].click()
                        sleep(1)
                        # 获取第三级
                        reason_3_ul = reason_2.find_element_by_tag_name("ul")
                        reason_3_li = reason_3_ul.find_elements_by_tag_name("li")
                        for k3, reason_3 in enumerate(reason_3_li):
                            reason_insert_dict['table'] = "case_reason"
                            reason_insert_dict['case_name'] = reason_3.text
                            reason_insert_dict['case_type'] = 3
                            reason_insert_dict['parent_id'] = reason_2_parent_id
                            result = DB.insert(reason_insert_dict, False)
                            reason_3_parent_id = DB.free(reason_parent_id_sql, False)[0][0]
                            if result == 0:
                                debug("第" + str(reason_3_parent_id) + "条插入失败")
                                continue
                            else:
                                debug("第" + str(reason_3_parent_id) + "条插入成功")
                            reason_3_span = reason_3.find_elements_by_tag_name("span")
                            reason_3_span[0].click()
                            sleep(1)
                            # 获取第四级
                            try:
                                reason_4_ul = reason_3.find_element_by_tag_name("ul")
                                reason_4_li = reason_4_ul.find_elements_by_tag_name("li")
                            except:
                                reason_4_li = list()
                            for k4, reason_4 in enumerate(reason_4_li):
                                reason_insert_dict['table'] = "case_reason"
                                reason_insert_dict['case_name'] = reason_4.text
                                reason_insert_dict['case_type'] = 4
                                reason_insert_dict['parent_id'] = reason_3_parent_id
                                result = DB.insert(reason_insert_dict, False)
                                reason_3_parent_id = reason_3_parent_id + 1
                                if result == 0:
                                    debug("第" + str(reason_3_parent_id) + "条插入失败")
                                    continue
                                else:
                                    debug("第" + str(reason_3_parent_id) + "条插入成功")
                                sleep(1)
                except Exception as e:
                    debug(e)
        except Exception as e:
            debug(e)
        finally:
            DB.closeDB()
            driver.quit()
        return data

    def judgeCourtLevel(self, s):
        if s.find("最高人民法院") != -1:
            return 1
        elif s.find("高级人民法院") != -1:
            return 2
        elif s.find("中级人民法院") != -1:
            return 3
        else:
            return 4

    # noinspection PyPep8Naming
    # 得到 裁判文书网 的详情页数据
    # noinspection PyBroadException
    def getWenShuDetailData(self, docid, cp_reason=""):
        """
        :param docid:
        :param cp_reason: the list page's reason
        :return:
        """
        # url = "http://wenshu.court.gov.cn/content/content?DocID=532bd8ed-4ba8-48b7-ad70-0063f64ede05"
        # url = "http://wenshu.court.gov.cn/content/content?DocID=77fc1e61-27d9-43d0-b96f-ca67225008b9"
        # url = "http://wenshu.court.gov.cn/content/content?DocID=57d363d0-3294-4d5b-92b2-cc2b6f6ca80f"
        # 刑事的url 1
        # url = "http://wenshu.court.gov.cn/content/content?DocID=eff7f53c-b647-11e3-84e9-5cf3fc0c2c18&KeyWord="
        # 刑事的url 2
        url = "http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=" + docid
        debug("开始获取文书 => " + docid)
        data = curlData(url, referer="http://wenshu.court.gov.cn/content/content?DocID=" + docid + "&KeyWord=", proxy_ip=self.proxy_ip)
        debug(data)
        debug("数据获取成功，开始处理")
        dataFlag = re.findall('\$\("#DivContent"\)\.html\(jsonHtml\)', data)
        try:
            unusedData = dataFlag[0]
        except:
            return 3
        debug(dataFlag)
        insertArr = {
            "id": " NEXT VALUE FOR LAW_WS_ORIGIN_CONTENT_SEQUENCE",
            "table": "ws_origin_content",
            "content": data
        }
        insertResult = self.ws_db.insert(insertArr, is_close_db=False)
        if insertResult == 1:
            debug("文书 " + docid + " => 插入成功\n")
        else:
            debug("文书 " + docid + " => 插入失败\n")
            return 3
        return 1
        # with open("wenshu.txt", "rb") as f:
        #     data = f.read().decode("utf-8")
        #     f.close()
        handleData = BeautifulSoup(data, "html.parser")
        caseInfo = handleData.find_all("input", attrs={"id": "hidCaseInfo"})
        caseInfoFinal = dict()
        # 文书内容(供全文搜索用)
        try:
            caseInfoFinal['content'] = handleData.find("div", id="DivContent").getText()
        except Exception as e:
            caseInfoFinal['content'] = ""
        # 裁判理由
        caseInfoFinal['cp_reason'] = cp_reason
        # id键值
        caseInfoFinal['id'] = " NEXT VALUE FOR LAW_WS_CONTENT_SEQUENCE"
        # 表名
        caseInfoFinal['table'] = "ws_content"
        try:
            try:
                caseInfo = caseInfo[0].attrs['value']
                caseInfo = json.loads(caseInfo)
            except Exception as e:
                caseInfo = dict()
            try:
                caseInfo['上传日期'] = re.findall("(\d+)", caseInfo['上传日期'])[0]
            except Exception as e:
                pass
            try:
                sjy = re.findall("<div[\w\W]*?>书　记　员([\w\W]*?)<\/div>", data)[0].strip()
                sjy = "".join(sjy.split())
                caseInfo['书记员'] = sjy
            except Exception as e:
                caseInfo['书记员'] = ""
            # 获取案由
            try:
                lawsuitReason = handleData.find_all("div", id="divTool_Summary")[0]
                lawsuitReason = re.findall("案由：<\/th><td><a[\w\W]*?>([\w\W]*?)<\/a>", str(lawsuitReason))[0]
                caseInfo['案由'] = lawsuitReason
            except:
                caseInfo['案由'] = ""
            # 获取诉讼费
            try:
                ssf = re.findall("<div[\w\W]*?>诉讼费([\w\W]*?)[，|。]", data)[0].strip()
                caseInfo['诉讼费'] = "".join(ssf.split())
            except:
                caseInfo['诉讼费'] = ""
            caseInfoK = [
                "案件名称",
                "法院名称",
                "案件类型",
                "案由",
                "文书类型",
                "案号",
                "审判程序",
                "书记员",
                "上传日期",
                "诉讼费",
                "文书ID",
                "法院省份",
                "法院区县",
                "法院区域",
                "法院地市"
            ]
            caseInfoV = [
                "title",
                "court_name",
                "case_type",
                "case_reason",
                "ws_type",
                "case_num",
                "spcx",
                "sjy",
                "ws_update_time",
                "ssf",
                "docid",
                "province",
                "county",
                "court_area",
                "city"
            ]
            try:
                for k, v in caseInfo.items():
                    if k in caseInfoK:
                        if v is None:
                            v = ""
                        caseInfoFinal[caseInfoV[caseInfoK.index(k)]] = v
                if caseInfoFinal['docid'] == "":
                    debug("内容获取出错, 文书id打印：" + caseInfoFinal['docid'])
                    return 2
            except Exception as e:
                debug("内容获取出错：" + e.__str__())
                return 2
            # 获取法院层级
            try:
                caseInfoFinal['court_level'] = self.judgeCourtLevel(caseInfoFinal['court_name'])
            except Exception as e:
                caseInfoFinal['court_level'] = None
            # 获取法律依据
            try:
                flyj = handleData.find_all("div", attrs={"class": "relateinfo"})
                flyjContent = handleData.find("div", attrs={"class": "content_lawitems_body"})
                flyjContent = flyjContent.find_all("tr")
                # 获取裁判日期
                try:
                    cp_date = re.findall('裁判日期：[\w\W]*?<\/th>[\w\W]*?<td>([\w\W]*?)<\/td>', str(flyj[0]))[0]
                    cp_date = getTimeStamp(cp_date, "%Y-%m-%d")
                except Exception as e:
                    cp_date = ""
                caseInfoFinal['cp_date'] = cp_date
                flyj = flyj[1]
                flyj = flyj.find_all("tr")
                tmpFlyj = ""
                tmpFlyjContent = ""
                tmpFlyjFlag = True
                for k1, v1 in enumerate(flyj):
                    tmpV = str(v1)
                    if tmpV.find("<a") != -1:
                        if tmpFlyjFlag:
                            tmpFlyjFlag = False
                            tmpFlyj = tmpFlyj + "".join(v1.getText()).strip()
                            tmpFlyjContent = tmpFlyjContent + "".join(flyjContent[k1].getText()).strip()
                        else:
                            tmpFlyj = tmpFlyj + "," + "".join(v1.getText()).strip()
                            tmpFlyjContent = tmpFlyjContent + "->" + "".join(flyjContent[k1].getText()).strip()
                    else:
                        tmpFlyjFlag = True
                        if k1 == 0:
                            tmpFlyj = tmpFlyj + "".join(v1.getText()).strip() + "=>"
                            tmpFlyjContent = tmpFlyjContent + "".join(flyjContent[k1].getText()).strip() + "=>"
                        else:
                            tmpFlyj = tmpFlyj + "|" + "".join(v1.getText()).strip() + "=>"
                            tmpFlyjContent = tmpFlyjContent + "|" + "".join(flyjContent[k1].getText()).strip() + "=>"
            except Exception as e:
                tmpFlyj = ""
            caseInfoFinal['legislative_authority'] = tmpFlyj
            caseInfoFinal['legislative_authority_content'] = tmpFlyjContent
            # 诉讼当事人
            try:
                litigant = re.findall('当事人：[\w\W]*?<\/th>[\w\W]*?<td>([\w\W]*?)<\/td>', data)[0]
            except Exception as e:
                litigant = ""
            caseInfoFinal['litigant'] = litigant
            litigant2 = ""
            # 获取首部
            try:
                head = re.findall('<a type="dir" name="WBSB">([\w\W]*?)<a',
                                  data)[0]
            except Exception as e:
                head = ""
            try:
                head = head + re.findall('<a type="dir" name="DSRXX">([\w\W]*?)<a', data)[0]
                head = head.replace("</a>", "")
            except Exception as e:
                head = head + ""
            caseInfoFinal['head'] = head
            litigant2 = litigant2 + head
            # 获取事实
            try:
                fact1 = re.findall('<a type="dir" name="SSJL">([\w\W]*?)<a', data)[0]
                fact1 = fact1.replace("</a>", "")
            except Exception as e:
                fact1 = ""
            caseInfoFinal['fact1'] = fact1
            caseInfoFinal['litigant2'] = litigant2 + fact1

            # 获取律师事务所
            try:
                lssws = re.findall('委托代理人：([\w\W]*?)，([\w\W]*?)律师。', caseInfoFinal['litigant2'])
                lssws = lssws + re.findall('辩护人([\w\W]*?)，([\w\W]*?)律师。', caseInfoFinal['litigant2'])
            except Exception as e:
                lssws = list()
            law_office = ""
            lawyer = ""
            try:
                for k, v in enumerate(lssws):
                    if v[0].find("<div") != -1:
                        law_office = caseInfoFinal['litigant2']
                        lawyer = caseInfoFinal['litigant2']
                        break
                    if k == 0:
                        law_office = law_office + v[1]
                        lawyer = lawyer + v[0]
                    else:
                        law_office = law_office + "," + v[1]
                        lawyer = lawyer + "," + v[0]
            except Exception as e:
                pass
            caseInfoFinal['law_office'] = law_office
            caseInfoFinal['lawyer'] = lawyer

            try:
                fact2 = re.findall('<a type="dir" name="AJJBQK">([\w\W]*?)<a', data)[0]
                fact2 = fact2.replace("</a>", "")
            except Exception as e:
                fact2 = ""
            caseInfoFinal['fact2'] = fact2
            # 获取事由
            try:
                reason = re.findall('<a type="dir" name="CPYZ">([\w\W]*?)<a', data)[0]
                reason = reason.replace("</a>", "")
            except Exception as e:
                reason = ""
            caseInfoFinal['reason'] = reason
            # 获取裁判结果
            try:
                result = re.findall('<a type="dir" name="PJJG">([\w\W]*?)<a', data)[0]
                result = result.replace("</a>", "")
            except Exception as e:
                result = ""
            caseInfoFinal['result'] = result
            try:
                crime = re.findall('以([\w\W]*?)罪', result)[0]
                crime = crime + "罪"
            except Exception as e:
                crime = ""
            caseInfoFinal['crime'] = crime
            # 获取底部
            try:
                tail = re.findall('<a type="dir" name="WBWB">([\w\W]*?)<a', data)[0]
                tail = tail.replace("</a>", "")
            except Exception as e:
                tail = ""
            caseInfoFinal['tail'] = tail
            try:
                spry = re.findall('([\w\W]*?)年[\w\W]*?月[\w\W]*?日', tail)[0]
            except Exception as e:
                spry = ""
            caseInfoFinal['spry'] = spry
            try:
                docid = caseInfoFinal['docid']
                del docid
            except:
                caseInfoFinal['flag'] = 1
        except Exception as e:
            caseInfoFinal['flag'] = 1
        debug("开始插入数据")
        insertResult = self.ws_db.insert(caseInfoFinal, is_close_db=False)
        if insertResult == 1:
            debug("文书" + caseInfoFinal['docid'] + " => 插入成功\n")
        else:
            debug("文书 " + caseInfoFinal['docid'] + " => 插入失败\n")
            return 3
        return 1

    def getDataChrome(self, url, sleep_time=0, is_save_file=False, file_name="1"):
        """
        获取文书列表
        :param url:
        :param sleep_time:
        :param is_save_file:
        :param file_name:
        :return: web source
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        debug("本次的代理ip为：" + self.proxy_ip)
        x_for = '--proxy-server=' + self.proxy_ip
        # 设置代理
        # chrome_options.add_argument(x_for)
        debug("开始启动chrome")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        debug("启动成功,开始打开url")
        try:
            driver.get(url)
        except Exception as e:
            driver.quit()
            debug(e)
            return ""
        debug("打开成功，开始等待加载数据")
        sleep(sleep_time)
        data = driver.page_source
        debug("等待完毕")
        if is_save_file:
            if file_name == "1":
                file_name = "origin_data/data.txt"
            with open(file_name, "wb") as f:
                try:
                    data = data.encode("utf-8")
                except:
                    pass
                f.write(data)
                try:
                    data = data.decode("utf-8")
                except:
                    pass
                f.close()
        try:
            all_cookie = driver.get_cookies()
            vjkl5 = driver.get_cookie("vjkl5")['value']
            result = self.getWenShuListContent(all_cookie, vjkl5, url)
            if result == 0:
                debug("本次条件的docid抓取终止(可能遇到空数据)，退出本次抓取并重新构造条件和获取cookie")
        except Exception as e:
            debug(e)
        debug("关闭浏览器")
        driver.quit()
        return "执行完毕"

    def getWenShuListContent(self, all_cookie, vjkl5, url):
        """
        :param all_cookie:
        :param vjkl5:
        :param url:
        :return:
        """
        cookie_all = ""
        cookie_len = len(all_cookie)
        cookie_len = cookie_len + 1
        for k, v in enumerate(all_cookie):
            if k >= cookie_len:
                cookie_all = cookie_all + "%s=%s" % (str(v['name']), str(v['value']))
            else:
                cookie_all = cookie_all + "%s=%s; " % (str(v['name']), str(v['value']))
        try:
            post = curlData("http://ws_api.xiezhi.sc.cn/getParam?vjkl5=" + vjkl5)
        except:
            post = "{}"
            debug("post参数获取出错")
        post = json.loads(post)
        post['Order'] = "法院层级"
        post['Param'] = "案件类型:刑事案件"
        post['Page'] = 20
        post['number'] = "wens"
        post['Direction'] = "asc"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        # 页码index
        index = 1
        # 页码是否变化，如果抓取了10次依旧无数据，则抓取下一页(后期可中断并记录)
        index_is_change = 0
        # 这个变量用来记录抓数据为空的页数，如果连续且达到了5，则终止本次抓取
        is_end = 0
        while True:
            debug(index)
            # 设置抓取页码
            post['index'] = index
            # 抓取数据
            try:
                resultData = curlData("http://wenshu.court.gov.cn/List/ListContent", value=post, referer=url,
                                      cookie=cookie_all, header=header, proxy_ip=self.proxy_ip)
            except Exception as e:
                debug("重新获取代理ip")
                self.setProxyIp()
                self.getWenShuListContent(all_cookie, vjkl5, url)
                return 2
            try:
                # 数据传入插入处理函数
                result = self.insertWenShuList(resultData)
            except Exception as e:
                debug("getWenShuListContent函数出错： insertWenShuList：" + e.__str__())
                return 0
            """
            0表示抓取出错，数据已经存在
            1表示抓取成功
            2表示数据为空
            """
            if result == 0:
                return 0
            elif result == 1:
                debug("第" + str(index) + "页文书id获取成功")
                index = index + 1
            elif result == 2:
                if index_is_change > 10:
                    index = index + 1
                    index_is_change = 0
                    is_end = is_end + 1
                else:
                    index_is_change = index_is_change + 1
            else:
                index = index + 1
            if is_end > 5:
                return 0
            sleep(3)

    def insertWenShuList(self, result_data):
        """
        :param result_data: the docid's json data
        :return:  no return
        """
        selectArr = {
            "table": "ws_docid"
        }
        insertArr = {
            "table": "ws_docid",
            "id": "NEXT VALUE FOR LAW_WS_DOCID_SEQUENCE"
        }
        try:
            result_data = json.loads(result_data)
            result_data = json.loads(result_data)
        except Exception as e:
            debug("接口数据返回出错，返回数据为：" + str(result_data))
            result_data = list()
        post = dict()
        try:
            runEval = result_data[0]['RunEval']
        except Exception as e:
            debug("RunEval获取出错")
            return 2
        length = len(result_data)
        docId = ""
        for i in range(1, length):
            try:
                if i >= length - 1:
                    docId = docId + result_data[i]['文书ID']
                else:
                    docId = docId + result_data[i]['文书ID'] + ","
            except Exception as e:
                debug("文书ID拼接出错，错误未知，暂时判断为无此条目 ：" + e.__str__())
                return 2
        try:
            post['runEval'] = runEval
            post['docId'] = docId
            result_data = curlData("http://ws_api.xiezhi.sc.cn/getDocId", value=post)
            result_data = json.loads(result_data)
            result_data = result_data['data'].split(",")
        except Exception as e:
            debug(e)
            return 2
        for v in result_data:
            # noinspection PyBroadException
            debug("本次处理的文书id => " + v)
            try:
                selectArr['table'] = "ws_docid"
                selectArr['condition'] = ['"docid"=' + "'" + v + "'"]
                selectResult = self.ws_db.select(selectArr, is_close_db=False)
                unused = selectResult[0]['docid']
                debug("本条数据已经存在")
                return 0
            except:
                insertArr['table'] = "ws_docid"
                insertArr['docid'] = v
                insertResult = self.ws_db.insert(insertArr, is_close_db=False)
                if insertResult != 0:
                    debug("本条数据插入成功")
                else:
                    debug("本条数据插入失败")
        return 1

    def getWenShuList(self):
        """
        获取文书列表(同时存入数据库)
        :return:
        """
        # self.setProxyIp()
        url = "http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1++%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6+%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6"
        data = self.getDataChrome(url, 0, is_save_file=False, file_name="origin_data/wenshuList.txt")
        return data

    def getWenShuDetailAll(self):
        """
        获取所有数据库已有的文书ID对应的详细信息
        :return:
        """
        # 首先获取文书的docid(未处理过的)
        # self.setProxyIp()
        docIdList = self.ws_db.select({"table": "ws_docid", "condition": ['"is_handle"=0']}, is_close_db=False)
        for docid in docIdList:
            try:
                while True:
                    if not docid['docid']:
                        break
                    data = self.getWenShuDetailData(docid['docid'])
                    if data == 1:
                        docid['table'] = "ws_docid"
                        docid['is_handle'] = 1
                        self.ws_db.insert(docid, is_close_db=False)
                        break
                    elif data == 2:
                        self.setProxyIp()
                        debug("重新获取ip\n")
                        continue
                    else:
                        break
            except Exception as e:
                debug("ip可能过期，重新获取")
                self.setProxyIp()

    def getProxyIp(self):
        """
        进行proxy ip获取，并且存到数据库(law_proxy_ip)提供调用
        :return:
        """
        url = "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=f7a9a3d793f64124ae793c2da903f65d&orderno=YZ20189253484oI7PrM&returnType=2&count=2"
        data = curlData(url)
        try:
            data = json.loads(data)
            for k, v in enumerate(data['RESULT']):
                v['id'] = "NEXT VALUE FOR LAW_PROXY_IP_SEQUENCE"
                v['table'] = "proxy_ip"
                try:
                    self.ws_db.insert(v, is_close_db=False)
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
            data = data[0]['ip'] + ":" + data[0]['port']
            self.ws_db.insert(updateArr, is_close_db=False)
        except Exception as e:
            debug("\nip暂无，删除库存并进行动态获取")
            # 如果没有结果表示已经用完了，那么就进行删除数据并且重新获取
            self.ws_db.delete({"table": "proxy_ip"}, is_close_db=False)
            self.getProxyIp()
            data = self.getSingleProxyIp()
        return data
