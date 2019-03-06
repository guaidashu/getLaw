# move docid
import sys
import os
import json
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from tool import phoenix_db
from tool.function import curlData, debug

if __name__ == "__main__":
    ws_db = phoenix_db.DBConfig()
    start = 153806
    table_columns = ws_db.getColumns({"table": "ws_origin_content"})
    url = "http://api.tan90.club/ws_api/getWsOriginContent.html?start=" + str(start)
    # url = "http://127.0.0.1:8000/ws_api/getWsOriginContent.html?start=" + str(start)
    while True:
        try:
            debug("开始获取", True)
            data = curlData(url=url, timeout=20)
            data = json.loads(data)
            data = data['data']
            break
        except Exception as e:
            debug(e, True)
    # noinspection PyBroadException
    try:
        curlData("http://autostart.tan90.club/", timeout=5)
    except:
        pass
    while True:
        try:
            for k, v in enumerate(data):
                v['table'] = "ws_origin_content"
                tmp = v['id']
                v['id'] = " NEXT VALUE FOR LAW_WS_ORIGIN_CONTENT_SEQUENCE"
                ws_db.insert(v, is_close_db=False, table_columns=table_columns)
                debug("文书 %s => 迁移成功" % str(tmp), True)
            start = start + 1000
            url = "http://api.tan90.club/ws_api/getWsOriginContent.html?start=" + str(start)
            # url = "http://127.0.0.1:8000/ws_api/getWsOriginContent.html?start=" + str(start)
            time.sleep(3)
            while True:
                try:
                    debug("开始获取", True)
                    data = curlData(url=url, timeout=20)
                    data = json.loads(data)
                    data = data['data']
                    break
                except Exception as e:
                    debug(e, True)
            # noinspection PyBroadException
            try:
                curlData("http://autostart.tan90.club/", timeout=5)
            except:
                pass
        except Exception as e:
            debug(e, True)
            break
    ws_db.closeDB()
