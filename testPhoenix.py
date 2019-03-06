import json
import re
from time import sleep

from phoenixdb import connect
import phoenixdb.cursor
from tool.function import debug, getTimeStamp, curlData
from tool.phoenix_db import DBConfig
from tool import db

# database_url = "47.106.218.50:8765"
# conn = connect(url=database_url, autocommit=True)
#
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE "test_phoenix" ("id" integer PRIMARY KEY, "username" varchar)')
# cursor.execute('UPSERT INTO "test_phoenix"("id","username") values (?, ?)', (5, 'admin'))
# cursor.execute('drop sequence law_case_reason_sequence')
# cursor.execute('upsert into "law_proxy_ip" ("is_used","id")values(1,21)')
# conn.commit()
# cursor.execute('select * from "law_proxy_ip" limit 1 offset 0')
# data = cursor.fetchall()
# debug(data)
# data = cursor.description
# debug(data)
#
# cursor = conn.cursor(cursor_factory=phoenixdb.cursor.DictCursor)
# cursor.execute("select * from test_phoenix where username='admin'")
# debug(cursor.fetchall())
# conn.close()

DB = DBConfig()
# data = {
#     "table": "case_reason",
#     "id": 1,
#     "case_name": "民事案件",
#     "parent_id": 0,
#     "case_type": 1
# }
data = {
    "table": "docid"
}
# reason_1_dict = {
#     "table": "case_reason",
#     "case_name": "first",
#     "id": " NEXT VALUE FOR LAW_CASE_REASON_SEQUENCE",
#     "case_type": 1,
#     "parent_id": 0
# }
# sql = DB.getInsertSql(reason_1_dict, "case_reason")
# debug(sql)
# sql = 'create table "law_ws_origin_content" ("id" integer PRIMARY KEY,"content" varchar,"is_handle" integer)'
# sql = 'create table "law_ws_content" ("id" integer PRIMARY KEY,"title" VARCHAR,"head" varchar,"fact1" varchar,"fact2" varchar,"reason" varchar,"result" varchar,"tail" varchar,"court_name" VARCHAR,"case_type" integer,"case_reason" varchar,"ws_type" integer,"spry" varchar,"sjy" varchar,"law_office" varchar,"legislative_authority" varchar,"legislative_authority_content" varchar,"case_num" varchar,"court_level" integer,"spcx" varchar,"cp_date_start" bigint,"cp_date_end" bigint,"cp_date" bigint,"ws_update_time" bigint,"litigant" varchar,"litigant2" varchar,"lawyer" varchar,"xzqh" varchar,"province" varchar,"city" varchar,"county" varchar,"court_area" varchar,"crime" varchar,"ssf" varchar,"flag" integer,"docid" varchar,"content" varchar,"cp_reason" varchar, "is_get" integer)'
# sql = 'create table "law_case_reason" ("id" integer PRIMARY KEY, "case_name" VARCHAR, "parent_id" INTEGER, "case_type" integer)'
# sql = 'create table "law_ws_record"("id" integer PRIMARY KEY,"start_date" varchar,"end_date" varchar,"court_id" varchar)'
# sql = 'create table "law_ws_docid"("id" integer PRIMARY KEY,"docid" varchar, "is_handle" integer,"title" varchar,"cp_date" varchar,"content" varchar, "case_type" integer, "court_name" varchar, "case_num" varchar)'
# sql = 'create table "law_ws_over_record"("id" integer PRIMARY KEY,"start_date" varchar,"end_date" varchar,"court_name" varchar)'
# sql = 'create table "law_ws_docid_record"("id" integer PRIMARY KEY,"court_name" varchar,"court_num" integer,"start_date" varchar,"court_year" varchar)'
# sql = 'create table "law_ws_content_id_record"("id" integer PRIMARY KEY,"docid_id" integer)'
# sql_sequence = 'create sequence law_case_reason_sequence'
# sql = 'create table "law_test" ("id" integer PRIMARY KEY, "num" bigint)'
# sql = 'create table "law_proxy_ip"("id" integer PRIMARY KEY,"ip" varchar,"port" varchar,"is_used" integer, "time_stamp" integer)'
# data = DB.select(data)
# DB.createTable(sql)
# DB.createTable(sql, "law_ws_content_sequence")
# DB.createTable(sql, "law_ws_origin_content_sequence")
# DB.createTable(sql, False)
# DB.createTable(sql, "law_ws_record_sequence")
# DB.createTable(sql, "law_ws_over_record_sequence")
# DB.createTable(sql, "law_docid_sequence")
# DB.createTable(sql, "law_ws_docid_sequence")

# DB.createTable(sql)
# DB.free(sql_sequence)
# result = DB.free('select current value for law_case_reason_sequence', False)
# result = DB.free('drop table "law_ws_content"', False)
# result = DB.free('drop sequence law_ws_content_sequence', False)
# result = DB.free('drop table "law_ws_docid"', False)
# result = DB.free('drop table "law_ws_record"', False)
# result = DB.free('drop table "law_ws_over_record"', False)
# result = DB.free('drop sequence law_ws_docid_sequence', False)
# result = DB.free('drop sequence law_ws_record_sequence', False)
# result = DB.free('drop table "law_ws_docid_record"', False)
# result = DB.free('drop table "law_ws_origin_content"', False)
# result = DB.free('drop sequence law_ws_origin_content_sequence', False)

# sql = 'create table "law_handle_error_id"("id" integer PRIMARY KEY )'
# 处理数据错误表
# DB.createTable(sql, False)

# sql = 'create table "law_ws_handle_where"("id" integer PRIMARY KEY ,"ws_id" integer )'
# DB.createTable(sql, False)

# 代理ip表
# DB.createTable(sql, "law_proxy_ip_sequence")
# result = DB.free('drop table "law_proxy_ip"', False)
# result = DB.free('drop sequence law_proxy_ip_sequence', False)

# 缓存cookie表
# sql = 'create table "law_ws_docid_cookie"("id" integer PRIMARY KEY ,"cookie" varchar )'
# DB.createTable(sql, False)
# DB.insert({"table": "ws_docid_cookie", "id": 1, "cookie": ""})

# result = DB.insert(reasone_1_dict)
# debug(result)
# data = DB.free('select * from "law_docid" where "docid"=' + "'8252121f-8260-4241-b707-018d52d151ca'")

selectArr = {
    # "table": "ws_record",
    # "table": "ws_origin_content",
    # "table": "ws_over_record",
    "table": "ws_docid_record",
    # "table": "ws_docid",
    # "table": "ws_content",
    # "table": "ws_content_id_record",
    # "table": "ws_handle_where",
    # "id": 1,
    # "ws_id": 70901
    # "table": "LAW_COURT_INFO"
    # "table": "proxy_ip"
    # "table": "case_reason"
    # "table": "ws_content_id_record",
    # "columns": ['"id"'],35/work/getgrade/getLaw/testPhoenix.py
    # list(1) =>{
    #     [0] => list(1) =>{
    #         [0] => 1133586
    #     }
    # }
    # 数据库关闭失败：
    # ('the connection is already closed', None, None, None)
    #
    # Process finished with exit code 0
    # "id": 1,
    # "docid_id": 1,
    # "court_name": "兰西县人民法院",
    # "court_num": 0,
    # "start_date": "2018-01-01",
    # "court_year": "2018"
    # "is_handle": 0,
    # "columns": ['id'],
    # "docid": "sonjie"
    # "condition": ['"id"=15 or "id"=16 or "id"=17 or "id"=19 or "id"=20'],
    # "condition": ['"docid"=\'a3bfcd82-5eac-4359-bf81-d1fbe117d447\''],
    # "condition": ['"case_reason"=\'过失致人死亡\''],
    # "limit": [0, 1],
    # "condition": ['"id">60000 and "id"<=60010']
    # "condition": ['"id"=200002']
    # "order": ['"id"', "desc"]
}
# data = DB.insert(selectArr, is_close_db=False)
# 1 最高人民法院
# 2 柏乡县人民法院
# 3 榆社县人民法院
# 4 舒兰市人民法院
# 5 兰西县人民法院
# data = DB.getColumns(selectArr)
# data = DB.delete(selectArr, is_close_db=False)

# data = DB.free('select * from "law_ws_content" where "docid"="101" ')
data = DB.select(selectArr, is_close_db=False)
# debug(data)
# data_list = list()
# for i, v in enumerate(data):
#     tmp = data[i]['content']
#     tmp = re.findall("dirData = ([\w\W]*?)};", tmp)
#     tmp = tmp[0] + "}"
#     tmp = curlData("http://www.wsapi.com/handleFlfg", {"data": tmp})
#     tmp = json.loads(tmp)
# noinspection PyBroadException
# try:
#     tmp['legislative_authority'] = json.dumps(tmp['legislative_authority'])
#     # tmp['legislative_authority'] = json.loads(tmp['legislative_authority'])
# except:
#     tmp['legislative_authority'] = ""
# data_list.append(tmp)


# data = data[0]['content']
# data = re.findall("dirData = ([\w\W]*?)};", data)
# data = data[0] + "}"
# data = curlData("http://www.wsapi.com/handleFlfg", {"data": data})

# data = json.loads(data)
# data['legislative_authority'] = json.dumps(data['legislative_authority'])
# debug(data)
# data = json.loads(data)
# debug(json.loads(data))
# data = re.findall("JSON.stringify\(([\w\W]*?)\);", data)
# debug(json.loads(data[0]))

# mysql_db = db.DBConfig()
# data = mysql_db.select({"table": "court", "limit": [800, 200]}, is_close_db=False)
# mysql_db.closeDB()


# data = DB.select({"table": "ws_docid",  "condition": ['"is_handle"=0'], "limit": [0, 1]},
#                  is_close_db=False)

# 文书docid
# data = DB.free('select count("id") from "law_ws_docid"', is_close_db=False)
# 4729082
# 239792
# 奕弈

# 文书数据
# data = DB.free('select count("id") from "law_ws_content"', is_close_db=False)

# 文书源数据
# data = DB.free('select count("id") from "law_ws_origin_content"', is_close_db=False)
# 288571

# data = DB.select({"table": "ws_content_id_record", "limit": [0, 1]})

# arr = {
#     'court_num': "264",
#     'start_date': "2016-10-07",
#     'court_name': "河北省沧州市中级人民法院",
#     'court_year': "2016",
#     'id': 1
# }
# arr = {
#     'table': "ws_docid_record",
#     'court_num': "268",
#     'court_year': "2015",
#     'court_name': "青县人民法院",
#     'start_date': "2015-09-13",
#     'id': 1
# }
# data = DB.select({"table": "ws_docid", "condition": ['"id">1000000 and "id"<=1000020']})
# data = DB.insert(arr, is_close_db=False)
# data = DB.getColumns(selectArr, is_close_db=False)
# data = DB.getInsertSql(selectArr, "ws_content")
# data = DB.select({"table": "test"}, is_close_db=False)
debug(data)
# debug(sql)
#
# data = DB.select(data)
# debug(data)
DB.closeDB()
