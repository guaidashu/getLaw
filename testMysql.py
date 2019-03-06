from tool.function import debug
from tool import db

if __name__ == "__main__":
    DB = db.DBConfig()
    selectArr = {
        "table": "court",
    }
    data = DB.select(selectArr)
    debug(data)
