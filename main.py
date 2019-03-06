# -*- coding: utf-8 -*-
import sys
import os

import requests

import GetWsDataApi
from GetProxyIp import GetProxyIp
from HandleWsDataImmediately import HandleWsDataImmediately

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import datetime
import random
import re

from getLaw import handle
from tool.function import debug, js_arr, getTimeStamp, getDateTime, getNowTimeStamp, getUserAgent
import json
from tool.db import DBConfig
import html
import base64
from time import sleep
import time
from tool.function import md5
from tool.function import sha1
from tool.function import curlData
import urllib.parse
from tool import phoenix_db
from tool.function import getCookie
from getLaw.GetContitutionList import GetConstitutionList

if __name__ == "__main__":
    # data = curlData()
    # s = "《<go('ty',88839,0)>关于防止和惩处侵害应受国际保护人员包括外交代表的罪行的公约</go('ty',88839,0)>"
    # s = html.escape(s)
    # debug(s)
    # data = {
    #     "username": "奕弈",
    #     "password": s,
    #     "email": "1023767856@qq.com"
    # }
    # DB = DBConfig()
    # result = DB.getInsertSql(data, "user")
    # result = DB.insert(DB.getInsertSql(data, "user"))
    # debug(handle.getWenShuDetailData())
    # debug(handle.getConstitutionListData())
    # 获取文书的法院
    # debug(handle.getWenshuPlace())
    # 获取法律法规的行政区划
    # debug(handle.getConstitutionPlace())
    # 获取所有法律法规
    # handle.getAllConstitutionStart()
    # 获取裁判文书的案由
    # debug(handle.getWenShuDetailData())

    debug(handle.getWenShuList())

    # debug(GetConstitutionList().getConstitutionList(1))

    # handle = HandleWsDataImmediately()
    # debug(handle.getData("9b7a597f-7c9a-46ac-a9f0-a99e0120e6b2"), True)

    # url = "http://wenshu.court.gov.cn/ValiCode/GetCode"
    # header = {
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    #     "Origin": "http://wenshu.court.gov.cn"
    # }
    # cookie = getCookie(url, value={"guid": "107302d5-53b9-9a67c607-cfe04fe6db9a"}, referer="http://wenshu.court.gov.cn", header=header, timeout=5)
    # debug(cookie)

    # 16477
    # debug(handle.getWenShuListOver())

    # 法律法规
    # debug(handle.getConstitutionList())

    # debug(handle.getCaseTypeIndex("民事案件"))
    # debug(handle.getWenShuDetailAll())
    # debug("ok")
    # handle.handleWsData()
    # debug(handle.getSingleProxyIp())
    # debug(handle.getProxyIp())
    # debug(urllib.parse.unquote("http://wenshu.court.gov.cn/list/list/?sorttype=1&number=&guid=754870e7-5fe1-a243f528-1645799813cc&conditions=searchWord+%E6%B2%A7%E5%B7%9E%E5%B8%82%E6%96%B0%E5%8D%8E%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2+SLFY++%E6%B3%95%E9%99%A2%E5%90%8D%E7%A7%B0%3A%E6%B2%A7%E5%B7%9E%E5%B8%82%E6%96%B0%E5%8D%8E%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2&conditions=searchWord++CPRQ++2018-09-28%20TO%202018-10-03"))
    # debug(urllib.parse.unquote("Param=%E6%B3%95%E9%99%A2%E5%90%8D%E7%A7%B0%3A%E5%8C%97%E4%BA%AC%E5%B8%82%E9%AB%98%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2%2C%E8%A3%81%E5%88%A4%E6%97%A5%E6%9C%9F%3A2015-06-05+TO+2015-06-10&Index=1&Page=10&Order=%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7&Direction=asc&vl5x=75154cdc6b6ff68bdfab6c8a&number=PR36&guid=f7133078-be04-a67a8d93-6f47bc7bde08"))
    # debug(urllib.parse.unquote("%3A2018-09-28+TO+2018-10-03"))
    # debug(handle.getWsYear())
    # debug(urllib.parse.unquote("searchWord+%E5%8C%97%E4%BA%AC%E5%B8%82%E9%AB%98%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2+SLFY++%E6%B3%95%E9%99%A2%E5%90%8D%E7%A7%B0:%E5%8C%97%E4%BA%AC%E5%B8%82%E9%AB%98%E7%BA%A7%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2"))
    # debug(urllib.parse.quote(" SFYX:(有效~已被修正~失效) ^ ZLSX:(01~02~03~04~05~06~08~09~10~11~12~23) NOT TXTID=bj ^ SFFB=Y "))
    # docid = ""
    # if not docid:
    #     debug("ok", True)
    # debug(random.randint(0, 4))
    # data = "[{\"RunEval\":\"w61ZQW7CgzAQfAtRDsK2wqjDugHClFPCnsOQw6PDikIRSRsODcKVQ09Rw75eTFMKwrEJTjHDoMKGwpHDkCLDrMO1w47DrMOsOsOBYsK5T8K3wrtjIsOTwo98w7XCksOLw7TDsMO2w7wqwrPDt8O1fiPDl8OZdsOHw4IgJAHDo8K1ecKCCDDDs8OowpBHSGQmw5sVwr9KwqgtDHTCh8KyMMKoHhRDcSEHwpTCgDrDiBoiIH8IA8KdwpAcEkZKwqgADBrDgRfDg8KjKF4twpLDrHDDjMOlZ8KSZ3IRw4UUwovDomIsPMKdwpVbdcKdw47CnMK+V1JhwoQIWVBOcGrDhlQTw50zw6XDo8Oyw7dzNDE1XHhQwqBmSFBxwrsCbMK6B8KXBcOtYFfCvMKNwr43OcOVwqPCmcOHK8KowpLCtS7CkUbDgcKYw4PCjcOYFUk7RWvCj8KdwrQtPcOuccK7w5vDt28LesKsw6rCu8OUwqLDhcKbBWhrwo1+DMKcwqRhw5gsP8O7bhgMTcKawqExNWDDp8OBwocgbMKhwplqwqfDocOhWzg4w6/CunHCsnFJw5zCv0jCk8OJw6o4wpnCh8KtUltZPMO+woMYwqFnwrpxw4Yiw7HCr3YJECdHwpwSw7bCgsKtwr0cw5gcZTzDksOGcF7DqXhHNMKPw5YDUsKPE8OXw6TCksONwpDChcOgwoxHXw==\"}]"
    # data = "[{\"Key\":\"关键词\",\"Value\":\"87720\",\"Child\":[{\"Key\":\"驳回\",\"Value\":\"6183\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":6183},{\"Key\":\"程序合法\",\"Value\":\"5747\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":5747},{\"Key\":\"类似商品\",\"Value\":\"5731\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":5731},{\"Key\":\"合同\",\"Value\":\"5005\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":5005},{\"Key\":\"混淆\",\"Value\":\"4233\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":4233},{\"Key\":\"近似商标\",\"Value\":\"3908\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":3908},{\"Key\":\"注册商标\",\"Value\":\"2058\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":2058},{\"Key\":\"在先权利\",\"Value\":\"1643\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1643},{\"Key\":\"专利\",\"Value\":\"1581\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1581},{\"Key\":\"管辖\",\"Value\":\"1489\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1489},{\"Key\":\"变更\",\"Value\":\"1282\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1282},{\"Key\":\"强制性规定\",\"Value\":\"1237\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1237},{\"Key\":\"拆迁\",\"Value\":\"1138\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1138},{\"Key\":\"劳动合同\",\"Value\":\"1045\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1045},{\"Key\":\"具体行政行为\",\"Value\":\"1020\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1020},{\"Key\":\"给付\",\"Value\":\"1012\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":1012},{\"Key\":\"鉴定\",\"Value\":\"992\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":992},{\"Key\":\"本案争议\",\"Value\":\"927\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":927},{\"Key\":\"授权\",\"Value\":\"912\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":912},{\"Key\":\"租赁\",\"Value\":\"911\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":911},{\"Key\":\"所有权\",\"Value\":\"906\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":906},{\"Key\":\"补充协议\",\"Value\":\"869\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":869},{\"Key\":\"房屋买卖\",\"Value\":\"861\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":861},{\"Key\":\"驰名商标\",\"Value\":\"848\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":848},{\"Key\":\"创造性\",\"Value\":\"793\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":793},{\"Key\":\"不予受理\",\"Value\":\"785\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":785},{\"Key\":\"返还\",\"Value\":\"774\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":774},{\"Key\":\"投资\",\"Value\":\"770\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":770},{\"Key\":\"合同约定\",\"Value\":\"743\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":743},{\"Key\":\"实用新型\",\"Value\":\"738\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":738},{\"Key\":\"技术特征\",\"Value\":\"736\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":736},{\"Key\":\"公证\",\"Value\":\"672\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":672},{\"Key\":\"劳动争议\",\"Value\":\"663\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":663},{\"Key\":\"伪造\",\"Value\":\"623\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":623},{\"Key\":\"侵权行为\",\"Value\":\"603\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":603},{\"Key\":\"交付\",\"Value\":\"592\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":592},{\"Key\":\"利害关系\",\"Value\":\"566\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":566},{\"Key\":\"承诺\",\"Value\":\"550\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":550},{\"Key\":\"赔偿数额\",\"Value\":\"530\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":530},{\"Key\":\"违约金\",\"Value\":\"514\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":514},{\"Key\":\"第三人\",\"Value\":\"509\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":509},{\"Key\":\"组合商标\",\"Value\":\"501\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":501},{\"Key\":\"代理\",\"Value\":\"492\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":492},{\"Key\":\"租金\",\"Value\":\"483\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":483},{\"Key\":\"买卖合同\",\"Value\":\"478\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":478},{\"Key\":\"赔偿责任\",\"Value\":\"476\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":476},{\"Key\":\"分公司\",\"Value\":\"472\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":472},{\"Key\":\"利息\",\"Value\":\"470\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":470},{\"Key\":\"房屋拆迁\",\"Value\":\"446\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":446},{\"Key\":\"保证\",\"Value\":\"445\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":445},{\"Key\":\"著作权\",\"Value\":\"442\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":442},{\"Key\":\"合同无效\",\"Value\":\"440\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":440},{\"Key\":\"解除合同\",\"Value\":\"434\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":434},{\"Key\":\"不动产\",\"Value\":\"399\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":399},{\"Key\":\"债权\",\"Value\":\"394\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":394},{\"Key\":\"法定代表人\",\"Value\":\"393\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":393},{\"Key\":\"胁迫\",\"Value\":\"374\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":374},{\"Key\":\"继承\",\"Value\":\"369\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":369},{\"Key\":\"合作协议\",\"Value\":\"361\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":361},{\"Key\":\"商标专用权\",\"Value\":\"352\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":352},{\"Key\":\"赔偿金\",\"Value\":\"350\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":350},{\"Key\":\"房屋所有权\",\"Value\":\"343\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":343},{\"Key\":\"宅基地\",\"Value\":\"331\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":331},{\"Key\":\"担保\",\"Value\":\"324\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":324},{\"Key\":\"房屋租赁\",\"Value\":\"317\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":317},{\"Key\":\"实际履行\",\"Value\":\"308\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":308},{\"Key\":\"赔偿损失\",\"Value\":\"307\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":307},{\"Key\":\"实际损失\",\"Value\":\"304\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":304},{\"Key\":\"处分\",\"Value\":\"297\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":297},{\"Key\":\"利害关系人\",\"Value\":\"291\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":291},{\"Key\":\"商品的通用名称\",\"Value\":\"288\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":288},{\"Key\":\"实用新型专利\",\"Value\":\"288\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":288},{\"Key\":\"行政赔偿\",\"Value\":\"288\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":288},{\"Key\":\"代理人\",\"Value\":\"286\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":286},{\"Key\":\"继续履行\",\"Value\":\"285\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":285},{\"Key\":\"承租人\",\"Value\":\"282\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":282},{\"Key\":\"房屋征收\",\"Value\":\"274\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":274},{\"Key\":\"违约责任\",\"Value\":\"266\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":266},{\"Key\":\"工伤\",\"Value\":\"264\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":264},{\"Key\":\"欺诈\",\"Value\":\"258\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":258},{\"Key\":\"法定期限\",\"Value\":\"257\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":257},{\"Key\":\"夫妻共同财产\",\"Value\":\"253\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":253},{\"Key\":\"建设工程\",\"Value\":\"250\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":250},{\"Key\":\"从属权利要求\",\"Value\":\"247\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":247},{\"Key\":\"查封\",\"Value\":\"247\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":247},{\"Key\":\"违法行为\",\"Value\":\"245\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":245},{\"Key\":\"诉讼标的\",\"Value\":\"244\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":244},{\"Key\":\"借款合同\",\"Value\":\"243\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":243},{\"Key\":\"虚假陈述\",\"Value\":\"242\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":242},{\"Key\":\"不履行\",\"Value\":\"241\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":241},{\"Key\":\"拆迁安置\",\"Value\":\"238\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":238},{\"Key\":\"侵权产品\",\"Value\":\"237\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":237},{\"Key\":\"回避\",\"Value\":\"237\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":237},{\"Key\":\"合同解除\",\"Value\":\"235\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":235},{\"Key\":\"继承人\",\"Value\":\"235\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"关键词\",\"SortKey\":100,\"IntValue\":235}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":87720},{\"Key\":\"一级案由\",\"Value\":\"28200\",\"Child\":[{\"Key\":\"\",\"Value\":\"此节点加载中...\",\"Child\":[],\"parent\":\"0\",\"id\":\"NULL0\",\"Field\":\"一级案由\",\"SortKey\":100,\"IntValue\":0},{\"Key\":\"刑事案由\",\"Value\":\"378\",\"Child\":[],\"parent\":\"\",\"id\":\"0\",\"Field\":\"一级案由\",\"SortKey\":100,\"IntValue\":378},{\"Key\":\"\",\"Value\":\"此节点加载中...\",\"Child\":[],\"parent\":\"1\",\"id\":\"NULL1\",\"Field\":\"一级案由\",\"SortKey\":100,\"IntValue\":0},{\"Key\":\"民事案由\",\"Value\":\"17494\",\"Child\":[],\"parent\":\"\",\"id\":\"1\",\"Field\":\"一级案由\",\"SortKey\":100,\"IntValue\":17494},{\"Key\":\"\",\"Value\":\"此节点加载中...\",\"Child\":[],\"parent\":\"2\",\"id\":\"NULL2\",\"Field\":\"一级案由\",\"SortKey\":100,\"IntValue\":0},{\"Key\":\"行政案由\",\"Value\":\"10328\",\"Child\":[],\"parent\":\"\",\"id\":\"2\",\"Field\":\"一级案由\",\"SortKey\":100,\"IntValue\":10328}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":28200},{\"Key\":\"法院层级\",\"Value\":\"43444\",\"Child\":[{\"Key\":\"高级法院\",\"Value\":\"43444\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"法院层级\",\"SortKey\":100,\"IntValue\":43444}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":43444},{\"Key\":\"法院地域\",\"Value\":\"43247\",\"Child\":[{\"Key\":\"最高人民法院\",\"Value\":\"0\",\"Child\":[],\"parent\":\"\",\"id\":\"0\",\"Field\":\"法院地域\",\"SortKey\":100,\"IntValue\":0},{\"Key\":\"\",\"Value\":\"此节点加载中...\",\"Child\":[],\"parent\":\"1\",\"id\":\"NULL1\",\"Field\":\"法院地域\",\"SortKey\":100,\"IntValue\":0},{\"Key\":\"北京市\",\"Value\":\"43247\",\"Child\":[],\"parent\":\"\",\"id\":\"1\",\"Field\":\"法院地域\",\"SortKey\":100,\"IntValue\":43247}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":43247},{\"Key\":\"裁判年份\",\"Value\":\"41588\",\"Child\":[{\"Key\":\"2017\",\"Value\":\"11946\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":11946},{\"Key\":\"2016\",\"Value\":\"10472\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":10472},{\"Key\":\"2014\",\"Value\":\"6776\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":6776},{\"Key\":\"2018\",\"Value\":\"6398\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":6398},{\"Key\":\"2015\",\"Value\":\"5357\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":5357},{\"Key\":\"2013\",\"Value\":\"433\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":433},{\"Key\":\"2012\",\"Value\":\"66\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":66},{\"Key\":\"2011\",\"Value\":\"26\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":26},{\"Key\":\"2010\",\"Value\":\"4\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"裁判年份\",\"SortKey\":100,\"IntValue\":4}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":41588},{\"Key\":\"审判程序\",\"Value\":\"43342\",\"Child\":[{\"Key\":\"一审\",\"Value\":\"190\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":190},{\"Key\":\"二审\",\"Value\":\"19651\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":19651},{\"Key\":\"再审\",\"Value\":\"855\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":855},{\"Key\":\"复核\",\"Value\":\"50\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":50},{\"Key\":\"刑罚变更\",\"Value\":\"166\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":166},{\"Key\":\"再审审查与审判监督\",\"Value\":\"14885\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":14885},{\"Key\":\"其他\",\"Value\":\"6934\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"审判程序\",\"SortKey\":100,\"IntValue\":6934}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":43342},{\"Key\":\"文书类型\",\"Value\":\"43444\",\"Child\":[{\"Key\":\"判决书\",\"Value\":\"12907\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"文书类型\",\"SortKey\":100,\"IntValue\":12907},{\"Key\":\"裁定书\",\"Value\":\"25064\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"文书类型\",\"SortKey\":100,\"IntValue\":25064},{\"Key\":\"调解书\",\"Value\":\"10\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"文书类型\",\"SortKey\":100,\"IntValue\":10},{\"Key\":\"决定书\",\"Value\":\"972\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"文书类型\",\"SortKey\":100,\"IntValue\":972},{\"Key\":\"通知书\",\"Value\":\"1562\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"文书类型\",\"SortKey\":100,\"IntValue\":1562},{\"Key\":\"其他\",\"Value\":\"5\",\"Child\":[],\"parent\":\"\",\"id\":\"\",\"Field\":\"文书类型\",\"SortKey\":100,\"IntValue\":5}],\"parent\":\"\",\"id\":\"\",\"Field\":\"\",\"SortKey\":100,\"IntValue\":43444}]"
    # data = json.loads(data)
    # length = len(data[4]['Child'])
    # debug(data[4]['Child'][length-1])

    # data = json.loads(data.replace("\n", "\/n"))
    # data = json.loads(data)
    # debug(data)
    # getTimeStamp(cp_date, "%Y-%m-%d")
    # s = "1996-01-01"
    # s = time.strptime(s, "%Y-%m-%d")
    # debug(time.mktime(s))
    # s = 820425600
    # s = 24*60*60*1
    # debug(s)
    # debug(getDateTime(s, "%Y-%m-%d %H:%M:%S"))
    # s = "[{\"RunEval\":\"w61Zw5vCjsKCMBDDvRbCjA9tMMO7A8OEJz9hHycNw5nCoMKuPMKswpjCik/Dhn9fYA1yKVLCl1rCqsKcwoTCjMKhwp3Di8KZw5PDqcOQw4bDuS5eb8KOwpHCjA/DqcOyM8KVw7HDvsO7YyvCk8Kfw5XDrkvCrsKSw7XChsO5wp5PAsOCacKxAAkQw5PCqMKQd0hkIsObFV0JawsBw57DgSwEVg/CjGFxw4EJw5hBw4LDiBrDucKDBMKkDmJAB3hCckgJKwDCgUJwSMOwIAjCl8KzKMOZH1N5worDkkTDjsKCwpBCwpE9wozDucOnS8KuVj7DpwvCpz9Lw4rChBA+w7PCiglOdcKfw7lEw79Mw7E6wr/DvSdPLB/DjjTDiMOLZ0hQw7bDkwhYV8O3wq4Gw53DgRrCuMKVwrp3MVXCvcKpw4fDi1AFw6o2RS0Iw4ocw67DuC5Bw6oxWnnDrcKFwq3CqcOxwojDmsODwrrDvzMYYDXDlMOUwojCvTknwoY9wrnDrcOOMMKwSXFnwoXDikrCu8Krwo3CqsKbw6PCk1J7LnFWQ8K8QMOVG2rChVpfccOrw5TDmyvCpcOuw7xfwqjCjsOtw60Iw5Y4w6V0NB7CjcKDw53CmAk6woHDicOqXsOqwo9oH8KOw6XDksKdw5BxY8KkwrUcPcO2FUDCq0nDqVw0XWNJccKlw6xowr7CtSt7a8K0w6rCkAZcworDncOgDVAEZzzDuAU=\",\"Count\":\"0\"}]"
    # s = json.loads(s)
    # debug(s)
    # debug(getData())
    post = {
        # "title": "山东富海实业股份有限公司、曲忠全与山东富海实业股份有限公司、曲忠全等环境污染责任纠纷再审复查与审判监督民事裁定书",
        # "courtName": "最高人民法院",
        # "caseReason": "案由",
        # "spry": "审判人员",
        # "sjy": "书记员",
        # "lawOffice": "律师事务所",
        # "legislativeAuth": "法律依据",
        # "caseNum": "案号",
        # "spcx": "一审",
        "cpDateStart": "2018-11-13",
        "cpDateEnd": "2018-11-20",
        "page": 1
        # "litigant": "当事人",
        # "lawyer": "律师"
    }
    # data = curlData("http://api.xiezhi.sc.cn/ws_api/getWsList.html", value=post)
    # data = curlData("http://127.0.0.1:8000/ws_api/getWsList.html", value=post)
    # debug(data)
    # lx = [[0, 1], [1, 2], [2, 3], [3, 4]]
    # lx = dict(lx)
    # debug(lx)

    # GetWsDataApi.GetWsDataApi().init("裁判日期:2018-11-13 TO 2018-11-20")
    # debug(HandleWsDataImmediately().getData("09f402f6-c250-47fb-9160-ac77188c0278"))
