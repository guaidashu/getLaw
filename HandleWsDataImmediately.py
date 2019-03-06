import json
import re

from GetProxyIp import GetProxyIp
from tool.function import debug, curlData, getTimeStamp


# noinspection PyBroadException,PyMethodMayBeStatic
class HandleWsDataImmediately(object):
    def __init__(self):
        self.proxy_ip = ""

    def __del__(self):
        pass

    def getData(self, docid):
        self.resetProxy()
        url = "http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=" + docid
        referer = "http://wenshu.court.gov.cn/content/content?DocID=" + docid + "&KeyWord="
        header_1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        while True:
            try:
                data = curlData(url, referer=referer, header=header_1, proxy_ip=self.proxy_ip, timeout=5)
                break
            except Exception as e:
                debug("数据获取出错,重新获取", True)
                self.resetProxy()
        tmp = data
        tmp = re.findall("dirData = ([\w\W]*?)};", tmp)
        tmp = tmp[0] + "}"
        tmp = curlData("http://127.0.0.1:3000/handleFlfg", {"data": tmp})
        tmp = json.loads(tmp)
        # noinspection PyBroadException
        try:
            tmp['legislative_authority'] = json.dumps(tmp['legislative_authority'])
        except:
            tmp['legislative_authority'] = ""
        return self.handleWsData(data, tmp)

    def handleWsData(self, data, api_data):
        try:
            caseInfo = re.findall("JSON.stringify\(([\w\W]*?)\);", data)
        except:
            debug("caseInfo获取出错")
        data = re.findall("jsonHtmlData = ([\w\W]*?)}\";", data)
        data = data[0] + "}\""
        data = json.loads(data)
        data = json.loads(data)
        data = data['Html']
        caseInfoFinal = api_data
        try:
            caseInfoFinal['cp_date'] = getTimeStamp(caseInfoFinal['cp_date'], "%Y-%m-%d")
        except:
            pass
        # 文书内容(供全文搜索用)
        try:
            caseInfoFinal['content'] = data
        except Exception as e:
            caseInfoFinal['content'] = ""
        # 裁判理由
        caseInfoFinal['cp_reason'] = ""
        try:
            try:
                caseInfo = json.loads(caseInfo[0])
            except Exception as e:
                caseInfo = dict()
            try:
                caseInfo['上传日期'] = re.findall("(\d+)", caseInfo['上传日期'])[0]
            except Exception as e:
                pass
            try:
                sjy = re.findall("<div[\w\W]*?>书 记 员([\w\W]*?)<\/div>", data)[0].strip()
                sjy = "".join(sjy.split())
                caseInfo['书记员'] = sjy
            except Exception as e:
                caseInfo['书记员'] = ""
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
            try:
                caseInfoFinal['ws_update_time'] = int(int(caseInfoFinal['ws_update_time']) / 1000)
            except:
                pass
            # 获取法院层级
            try:
                caseInfoFinal['court_level'] = self.judgeCourtLevel(caseInfoFinal['court_name'])
            except Exception as e:
                caseInfoFinal['court_level'] = None
            litigant2 = ""
            # 获取首部
            try:
                head = re.findall('<a type=["|\']dir["|\'] name=["|\']WBSB["|\']>([\w\W]*?)<a',
                                  data)[0]
            except Exception as e:
                head = ""
            try:
                head = head + re.findall('<a type=["|\']dir["|\'] name=["|\']DSRXX["|\']>([\w\W]*?)<a', data)[0]
                head = head.replace("</a>", "")
            except Exception as e:
                head = head + ""
            caseInfoFinal['head'] = head
            litigant2 = litigant2 + head
            # 获取事实
            try:
                fact1 = re.findall('<a type=["|\']dir["|\'] name=["|\']SSJL["|\']>([\w\W]*?)<a', data)[0]
                fact1 = fact1.replace("</a>", "")
            except Exception as e:
                fact1 = ""
            caseInfoFinal['fact1'] = fact1
            caseInfoFinal['litigant2'] = litigant2 + fact1

            # 获取律师事务所
            try:
                lssws = re.findall('委托代理人：([\w\W]*?)，([\w\W]*?)律师。', caseInfoFinal['litigant2'])
                lssws = lssws + re.findall('辩护人([\w\W]*?)，([\w\W]*?)律师。', caseInfoFinal['litigant2'])
                lssws = lssws + re.findall('委托诉讼代理人：([\w\W]*?)，([\w\W]*?)律师。', caseInfoFinal['litigant2'])
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
                fact2 = re.findall('<a type=["|\']dir["|\'] name=["|\']AJJBQK["|\']>([\w\W]*?)<a', data)[0]
                fact2 = fact2.replace("</a>", "")
            except Exception as e:
                fact2 = ""
            caseInfoFinal['fact2'] = fact2
            # 获取事由
            try:
                reason = re.findall('<a type=["|\']dir["|\'] name=["|\']CPYZ["|\']>([\w\W]*?)<a', data)[0]
                reason = reason.replace("</a>", "")
            except Exception as e:
                reason = ""
            caseInfoFinal['reason'] = reason
            # 获取裁判结果
            try:
                result = re.findall('<a type=["|\']dir["|\'] name=["|\']PJJG["|\']>([\w\W]*?)<a', data)[0]
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
                tail = re.findall("<a type='dir' name='WBWB'>([\w\W].*)", data)[0]
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
        # debug(caseInfoFinal)
        # debug("开始插入数据")
        # insertResult = self.ws_db.insert(caseInfoFinal, is_close_db=False)
        # if insertResult == 1:
        #     debug("文书" + caseInfoFinal['docid'] + " => 插入成功\n")
        # else:
        #     debug("文书 " + caseInfoFinal['docid'] + " => 插入失败\n")
        #     return 3
        return caseInfoFinal

    def judgeCourtLevel(self, s):
        if s.find("最高人民法院") != -1:
            return 1
        elif s.find("高级人民法院") != -1:
            return 2
        elif s.find("中级人民法院") != -1:
            return 3
        else:
            return 4

    def resetProxy(self):
        getProxyIp = GetProxyIp()
        self.proxy_ip = getProxyIp.getProxyIp()
