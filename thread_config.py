config = {
    "thread_num": 11,  # 抓取文书的线程数
    "index_is_change": 5,  # 抓取文书最大允许失败次数  一页文书的最大允许失败次数为  index_is_change * is_end
    "is_end": 3,  # 最大允许失败次数
    "over_index": 22,  # 抓取的最大页码
    "proxy_ip_url": "http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=f7a9a3d793f64124ae793c2da903f65d&returnType=2&count=1",  # proxy_ip的url
    "get_docid_api_url": "http://www.wsapi.com/getDocId",  # 获取文书id的接口url
    "ws_start_get_date": "2007-01-01",  # 抓取的开始时间
    "ws_end_get_date": "2018-09-30",  # 抓取最后的时间
    "interval_time_stamp": 432000,  # 抓取时间间隔
    "interval_time_stamp_over": 86400,  # 抓取时间间隔，较小的时间间隔
    "court": "court",  # 处理的法院表(因为开始抓取间隔为5天，可能会遗漏数据，如果五天内数据超过200条，则保存下来之后缩小时间范围重新抓取)
}
