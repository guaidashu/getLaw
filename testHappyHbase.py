import happybase
from tool.function import debug
from tool.function import byteToStr

connection = happybase.Connection("111.230.14.15", 9090)

connection.open()

# families = {
#     "columns1": dict(max_versions=10),
#     "columns3": dict()
# }
# connection.create_table("law_test3", families)

table = connection.tables()

debug(table)

# 插入数据

# table = connection.table("test")
#
# data = {
#     "columns2:data": "中文是否可以2"
# }
#
# data = table.put("3", data)

# 获取数据

# table = connection.table("test")

# data = table.scan(columns=['columns2'], row_start="1",
#                   filter="SingleColumnValueFilter('columns2', 'data', =, 'substring:2')")
# data = table.scan()

# byteToStr(data)
# data = byteToStr(data, "generator")

# debug(data)

# data = table.cells("1", "columns1")
#
# debug(data)

connection.close()
