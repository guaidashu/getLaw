import threading
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from tool.function import curlData, debug
from tool.db import DBConfig

rv = 0
mylock = threading.RLock()


# noinspection PyPep8Naming,PyBroadException
class ConstitutionThread(threading.Thread):
    def __init__(self, flfgID, zlsxid, showDetailType, province, index):
        threading.Thread.__init__(self)
        self.count = 0
        self.flfgID = flfgID
        self.zlsxid = zlsxid
        self.showDetailType = showDetailType
        self.province = province
        self.index = index
        self.rv = 0
        self.db = DBConfig()

    def __del__(self):
        self.db.closeDB()

    def run(self):
        debug("线程" + str(self.index) + "开始", True)
        global rv
        try:
            result = self.getConstitutionData(self.flfgID, self.zlsxid, self.showDetailType, self.province)
            if result != 1:
                tmp = "第" + str(self.index) + "条获取失败"
            else:
                tmp = "第" + str(self.index) + "条获取成功"
                mylock.acquire()
                rv = rv + 1
                mylock.release()
        except:
            tmp = "第" + str(self.index) + "条获取失败"
        print(tmp)

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
                mylock.acquire()
                sql = self.db.getInsertSql(type_data, "constitutions")
                result = self.db.insert(sql, is_close_db=False)
                mylock.release()
                break
            except Exception as e:
                debug(e)
        return result

    def getRv(self):
        global rv
        return rv

    def reset(self):
        global rv
        rv = 0

