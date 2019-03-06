from GetProxyIp import GetProxyIp
from GetWs import GetWs
from GetWsList import GetWsList
from tool.function import debug
from GetLaw import GetLaw
from bs4 import BeautifulSoup
from tool.function import curlData
from urllib.parse import urlencode
from tool.function import replace_html
import re
from tool.db import DBConfig
from time import sleep
import json
from GetContitutionList import GetConstitutionList

"""
获取法律法规信息库的首页信息
"""


def getStatuteIndexData():
    url = "http://210.82.32.100:8081/FLFG/"
    getLaw = GetLaw()
    data = getLaw.getDataSelenium(url, 1, True, "origin_data/statute.txt")
    return data


"""
获取宪法的列表
"""


# noinspection PyPep8Naming,PyBroadException
def getConstitutionListData():
    # url = "http://law.npc.gov.cn:8081/FLFG/index/xianfamore.jsp"
    # getLaw = GetLaw()
    # data = getLaw.getDataSelenium(url, sleep_time=2, is_save_file=True)
    with open("data.txt", "rb") as f:
        data = f.read().decode("utf-8")
        f.close()
    data = re.findall(r'<a href="javascript:showLocation([\w\W]*?);"', data)
    result_list = list()
    for k, v in enumerate(data):
        data[k] = tuple(v.split("'"))
        try:
            result = getConstitutionData(data[k][1], data[k][5])
            if result != 1:
                tmp = "第" + str(k + 1) + "条获取失败"
            else:
                tmp = "第" + str(k + 1) + "条获取成功"
        except:
            tmp = "第" + str(k + 1) + "条获取失败"
        result_list.append(tmp)
        print(tmp)
        sleep(3)
    return result_list


# noinspection PyBroadException
def getConstitutionData(flfgID, zlsxid, province):
    # 经过浏览。很明显，具体的宪法数据源url为如下的url,包含两个get类型参数  flfgID zlsxid keyword 前两个是必须的，通过列表传递的js数据拿到
    flag = False
    url = "http://law.npc.gov.cn:8081/FLFG/flfgByID.action"
    get = dict()
    get['flfgID'] = flfgID
    get['zlsxid'] = zlsxid
    get['keyword'] = ""
    get = urlencode(get)
    url = url + "?" + get
    data = curlData(url, get, url)
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
    columns_list = ['type', "department_type", 'office', 'reference_num', 'issue_date', 'execute_date', 'timeliness']
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
    DB = DBConfig()
    sql = DB.getInsertSql(type_data, "constitutions")
    result = DB.insert(sql)
    return result


# noinspection PyPep8Naming
# 得到 裁判文书网 的详情页数据
# noinspection PyBroadException
def getWenShuDetailData():
    getLaw = GetLaw()
    return getLaw.getWenShuDetailData("f08d44ee-b647-11e3-84e9-5cf3fc0c2c18")


# noinspection PyBroadException
def getWenshuPlace():
    getLaw = GetLaw()
    data = getLaw.getWenshuPlace()
    return data


def getConstitutionPlace():
    getLaw = GetLaw()
    data = getLaw.getConstitutionPlace()
    return data


# noinspection PyBroadException
def getAllConstitution(data, province):
    data = re.findall(r'<a href="javascript:showLocation([\w\W]*?);"', data)
    old1 = ""
    old5 = ""
    i = 0
    for k, v in enumerate(data):
        data[k] = tuple(v.split("'"))
        try:
            if data[k][1] == old1 and data[k][5] == old5:
                continue
            result = getConstitutionData(data[k][1], data[k][5], province)
            old1 = data[k][1]
            old5 = data[k][5]
            i = i + 1
            if result != 1:
                tmp = "第" + str(i) + "条获取失败"
            else:
                tmp = "第" + str(i) + "条获取成功"
        except:
            tmp = "第" + str(i) + "条获取失败"
        print(tmp)
        sleep(3)
    return 1


def getAllConstitutionStart():
    getLaw = GetLaw()
    getLaw.getAllConstitution(getAllConstitution)


def getCaseReason():
    getLaw = GetLaw()
    debug(getLaw.getCaseReason())


def getWenShuList():
    getWsList = GetWsList()
    getWsList.getWenShuList()
    debug("主线程完成")


def getProxyIp():
    getLaw = GetLaw()
    return getLaw.getProxyIp()


def getSingleProxyIp():
    getLaw = GetLaw()
    return getLaw.getSingleProxyIp()


def getWenShuListOver():
    getWsList = GetWsList()
    debug("启动主线程")
    return getWsList.getWenShuListOver()
    # return getWsList.getCourtOver()


def getWenShuListOverCaseType():
    getWsList = GetWsList(1)
    debug("启动主线程")
    return getWsList.getWenShuListOverCaseType()
    # return getWsList.getCourtOver()


def getWenShuDetailAll():
    getWs = GetWs()
    getWs.getWenShuDetailAll()
    return "执行完毕"
    # getLaw.setProxyIp()
    # return getLaw.getDataSeleniumChrome("https://nl.tan90.club/test/testHeader.html")


def getConstitutionList():
    getConstitutionListDemo = GetConstitutionList()
    return getConstitutionListDemo.getAllConstitutionStart()


def handleWsData():
    from HandleWsData import HandleWsData
    handle = HandleWsData("线程1")
    handle.start()

