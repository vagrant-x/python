
# # # get
# import requests
# response = requests.get("https://www.baidu.com/")
# # print(type(response.text))  # <class 'str'>
# # print(response.text)
# # print(response.content.decode("utf-8"))  # 使用 u8 解码，没有出现乱码
#
#
# # get 带有 headers 和查询参数
# import requests
#
# headers = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
# }
# data = {
#     "kw": "中国"
# }
# url = "https://www.baidu.com/s"
# # params 接收一个字典或字符串的查询参数，字典类型自动转换为 url， 不需要 urlencode()
# response = requests.get(url=url, params=data, headers=headers)
#
# # 查看响应码
# print("status_code: {}".format(response.status_code))  # status_code: 200
#
# # 查看解码 response.text 时使用的解码方式
# print("encoding:{}".format(response.encoding))  # encoding:utf-8
#
# # 查看完整的 url 地址
# print("url:{}".format(response.url))  # url:https://www.baidu.com/
#
# # 查看响应内容，response.content 返回的字节流数据
# print("context:{}".format(response.content))
#
# # Requests 会自动解码后的内容，大多数 unicode 字符集都能被无缝地解码。
# print("text:{}".format(response.text))




# # post
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"
headers = {
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
    "Cookie": "LGUID=20161229121751-c39adc5c-cd7d-11e6-8409-5254005c3644; user_trace_token=20210531172956-5c418892-9a48-4fa1-8377-2c4f7a20b741; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20210531185241-179c20de542206-0e1348daf26807-2b6f686a-1049088-179c20de543150; RECOMMEND_TIP=true; __lg_stoken__=677cc1b348553c3ed5e9cbb7b390a2ff300eb24fefe8a8e97e42e2872fc9543fba2800c9390bbd1d173c49e0c0362f67288bd32b2db49b0ed2db58d21a0b452d975350e4ed22; index_location_city=%E5%B9%BF%E5%B7%9E; login=false; unick=""; _putrc=""; JSESSIONID=ABAAAECABIEACCAAF01E6707FDF7DE8820405BA09C6C439; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; X_HTTP_TOKEN=34e72e60c648e0f923883522611a51a83da2b43601; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2221787087%22%2C%22first_id%22%3A%22179c20de60575-03879bc46582c2-2b6f686a-1049088-179c20de606146%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2257.0.2987.98%22%7D%2C%22%24device_id%22%3A%22179c20de60575-03879bc46582c2-2b6f686a-1049088-179c20de606146%22%7D; _gat=1; _ga=GA1.2.2125950788.1622453397; _gid=GA1.2.1174524155.1622458625; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622453401,1622453584,1622458348,1622460836; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622538830; TG-TRACK-CODE=index_search; LGSID=20210601171352-cf8ce267-baa7-496a-85b4-d5c3239d2f39; LGRID=20210601171402-1ac136e6-0d19-488f-9639-d1ad2bb75fe7; SEARCH_ID=6a4a97b38c434d13830a64516514c7e3"
}
data = {
    "first": "true",
    "pn": 1,
    "kd": "python"
}

response = requests.post(url=url, data=data, headers=headers)
print(response.text)
print(response.json())  # 调用内置的 JSON 解码器解析数据
