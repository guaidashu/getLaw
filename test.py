# noinspection PyBroadException
import json
import urllib.parse

from bs4 import BeautifulSoup

from tool.function import curlData, debug


# noinspection PyBroadException
def getConstitutionData(url):
    # 经过浏览。很明显，具体的宪法数据源url为如下的url,包含两个get类型参数  flfgID zlsxid keyword 前两个是必须的，通过列表传递的js数据拿到
    flag = False
    # url = "http://210.82.32.100:8081/FLFG/flfgByID.action"
    # get = dict()
    # get['flfgID'] = flfgID
    # get['showDetailType'] = showDetailType
    # get['zlsxid'] = zlsxid
    # get['keyword'] = ""
    # get = urlencode(get)
    # url = url + "?" + get
    while True:
        try:
            data = curlData(url=url, value=url)
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
    type_data['province'] = ""
    if flag:
        type_data['is_get_error'] = 1
    else:
        type_data['is_get_error'] = 0
    return json.dumps(type_data)


if __name__ == "__main__":
    url = "http://law.npc.gov.cn:8081/FLFG/flfgByID.action?flfgID=37416210&keyword=&showDetailType=QW&zlsxid=01"
    data = curlData("http://api.tan90.club/ws_api/createParam.html?url=" + urllib.parse.quote(url))
    # data = curlData("http://127.0.0.1:8000/ws_api/createParam.html?url=" + urllib.parse.quote(url))
    # data = curlData(url, referer=url)
    debug(data)
