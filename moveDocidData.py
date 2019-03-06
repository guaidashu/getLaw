# move docid
import sys
import os
import json

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from time import sleep

from tool import phoenix_db
from tool.function import curlData, debug


ws_db = phoenix_db.DBConfig()


# noinspection PyBroadException
def moveDocid(start):
    url = "http://api.tan90.club/ws_api/getWsDocid.html?start=" + str(start)
    while True:
        try:
            data = curlData(url=url, timeout=5)
            data = json.loads(data)
            data = data['data']
            break
        except Exception as e:
            debug(e, True)
            sleep(2)
    for k, v in enumerate(data):
        v['table'] = "ws_docid"
        v['id'] = "NEXT VALUE FOR LAW_WS_DOCID_SEQUENCE"
        ws_db.insert(v, is_close_db=False)
        debug("文书 %s => 迁移成功" % v['docid'], True)


if __name__ == "__main__":
    start = 1
    while True:
        try:
            moveDocid(start)
            start = start + 1000
        except Exception as e:
            debug(e, True)
            break
    ws_db.closeDB()
