#encoding:utf8
"""
urllib 库
"""
# from urllib import request
# resp = request.urlopen('http://www.baidu.com')
# print(resp.read())
# print(resp.getcode())
#
# from urllib import request
# request.urlretrieve('http://www.baidu.com', "baidu_bak.html")
#
# from  urllib import parse
# data = {"name": "爬虫基础", "age": 90}
# qs = parse.urlencode(data)
# print(qs)  # name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&age=90
#
# from  urllib import parse
# qs_str = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&age=90"
# data = parse.parse_qs(qs_str)
# print(data)  # {'name': ['爬虫基础'], 'age': ['90']}


# # urlparse 和 urlsplit
# from urllib import request, parse
# url = "http://www.baidu.com/s;hello?usernme=zhiliao#101"
# result1 = parse.urlsplit(url)
# print(result1)
# result2 = parse.urlparse(url)
# print(result2)
# print("result2-->params :", result2.params)
#
# result = result1
# print("scheme:", result.scheme)
# print("netloc:", result.netloc)
# print("path:", result.path)
# print("query:",result.query)
# """
# 结果：
#     SplitResult(scheme='http', netloc='www.baidu.com', path='/s;hello', query='usernme=zhiliao', fragment='101')
#     ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='hello', query='usernme=zhiliao', fragment='101')
#     result2-->params : hello
#     scheme: http
#     netloc: www.baidu.com
#     path: /s;hello
#     query: usernme=zhiliao
# """

# # reques.Request 类
# from  urllib import request
# headers = {
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
#         }
# req = request.Request("http://www.baidu.com/", headers=headers)
# resp = request.urlopen(req)
# print(resp.read())



# # 使用 request.Request 类请求
# from urllib import request
#
# url = "https://www.lagou.com/landing-page/pc/search.html?utm_source=m_cf_cpc_baidu_pc&m_kw=baidu_cpc_sz_b374bf_067de6_%E6%8B%89%E5%8B%BE%E7%BD%91&bd_vid=11059753625618410496"
# # # 没有添加 User-Agent
# # resp = request.urlopen(url)
# # print(resp.read())
# # # 返回的内容比实际网页少很多
#
# # 添加 User-Agent
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
# }
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read())
# # 获取到和浏览器一样的内容


# # 用 Request爬取拉勾网职位信息
# from urllib import request,parse
#
# url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"
#
# headers = {
#     "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
#     'Origin': 'https://www.lagou.com',
#     "cookie": "LGUID=20161229121751-c39adc5c-cd7d-11e6-8409-5254005c3644; user_trace_token=20210531172956-5c418892-9a48-4fa1-8377-2c4f7a20b741; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20210531185241-179c20de542206-0e1348daf26807-2b6f686a-1049088-179c20de543150; sajssdk_2015_cross_new_user=1; RECOMMEND_TIP=true; __SAFETY_CLOSE_TIME__21787087=1; __lg_stoken__=677cc1b348553c3ed5e9cbb7b390a2ff300eb24fefe8a8e97e42e2872fc9543fba2800c9390bbd1d173c49e0c0362f67288bd32b2db49b0ed2db58d21a0b452d975350e4ed22; index_location_city=%E5%B9%BF%E5%B7%9E; login=false; unick=""; _putrc=""; JSESSIONID=ABAAAECABIEACCAAF01E6707FDF7DE8820405BA09C6C439; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2221787087%22%2C%22first_id%22%3A%22179c20de60575-03879bc46582c2-2b6f686a-1049088-179c20de606146%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2257.0.2987.98%22%7D%2C%22%24device_id%22%3A%22179c20de60575-03879bc46582c2-2b6f686a-1049088-179c20de606146%22%7D; _gid=GA1.2.1174524155.1622458625; X_HTTP_TOKEN=34e72e60c648e0f973806422611a51a83da2b43601; _ga=GA1.2.2125950788.1622453397; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622453401,1622453584,1622458348,1622460836; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622460836; LGRID=20210531193420-de9f4106-792c-4b58-ba57-e23c467d0128; TG-TRACK-CODE=index_search; SEARCH_ID=ea9769f0cf34489a97b947fba98efdb0"
# }
#
# data = {
#     "first": "true",
#     "pn": 1,
#     "kd": "python"
# }
#
# data_bytes = parse.urlencode(data).encode("utf-8")  #
# req = request.Request(url, headers=headers, data=data_bytes, method="POST")
# resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))
# '''
# 如果不添加cookie ， 后台将返回：
# {"status":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"14.23.114.195","state":2402}
# 被识别出来
# '''


"""
# 测试 ProxyHandler 处理器（代理）
1、代理的原理：在请求目的网站之前，先请求代理服务器，如何让代理服务去请求目的网站，
    代理服务器拿到目的网站的数据后，在转发给我们的代码
2、http://httpbin.org：这个网站可以方便的查看http请求的一下参数
3、在代码中使用代理：
    (1)使用 urllib.request.ProxyHandler, 传入一个代理，这个代理是一个字典，
        字典的key依赖于代理服务器能都接收的类型， 一般是 http 或是 https, 值是 ip:port
    (2)使用上一步创建的 handler, 以及 request.build_opener 创建一个 opener 对象
    (3)使用上一步创建的 opener 调用 open 方法， 发起请求
"""

# from urllib import request
# # 没有使用代理的情况
# # url = "http://httpbin.org/ip"
# # resp = request.urlopen(url)
# # print(resp.read().decode("utf-8"))
#
# # 使用代理的情况
# url = "http://httpbin.org/ip"
# # 1、使用ProxyHandler 传入代理构建一个handler
# handler = request.ProxyHandler({"http": "124.172.117.189:16816"})
# # 2、使用上面创建的handler构建一个opener
# opener = request.build_opener(handler)
# # 3、使用opener去发送一个请求
# resp = opener.open(url)
# print(resp.read().decode("utf-8"))



# 使用代理
from urllib import request, parse

# 提取代理API接口，获取1个代理IP

# url = "http://kps.kdlapi.com/api/getkps/"
# data = {
#     "orderid": "902251317966245",
#     "num": 1,
#     "sep": 1
# }
# data = parse.urlencode(data)
# req = request.urlopen(url, data=data)
# api_url = req

from urllib import request, parse
# 为了测试这个功能，在 快代理 上找的免费代理老是访问不了，花了 6 元买了一天的代理测试成功
api_url = "http://kps.kdlapi.com/api/getkps/?orderid=902251317966245&num=1&pt=1&sep=1"
print("api_url = {}".format(api_url))
resp = request.urlopen(api_url)
proxy_ip_port = resp.read().decode("utf-8")
print(proxy_ip_port)
proxy = {
    "http": proxy_ip_port
}

# 使用代理的情况
url = "http://httpbin.org/ip"
# 1、使用ProxyHandler 传入代理构建一个handler
handler = request.ProxyHandler(proxy)
# 2、使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3、使用opener去发送一个请求
resp = opener.open(url)
print("通过代理返回的结果：{}".format(resp.read().decode("utf-8")))

