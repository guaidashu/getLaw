import json

from tool.function import debug, curlData


# noinspection PyBroadException,PyPep8Naming
def analysis(result_data):
    try:
        result_data = json.loads(result_data.replace("\n", "\/n"))
    except Exception as e:
        result_data = ""
    post = dict()
    try:
        runEval = result_data[0]['RunEval']
        # 本条件总共文书条数
        try:
            count = int(result_data[0]['Count'])
            # if count > 210:
            #     return 5
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
        result_data = curlData("http://www.wsapi.com/getDocId", value=post)
        result_data = json.loads(result_data)
        result_data = result_data['data'].split(",")
    except Exception as e:
        debug(e, True)
        return 2
    return result_data
