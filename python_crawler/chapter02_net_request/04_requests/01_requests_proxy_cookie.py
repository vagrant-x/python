

# import requests
#
# url = "http://httpbin.org/ip"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
# }
# proxy = {
#     "http": "42.193.23.248:16817"
# }
# resp = requests.get(url=url, headers=headers, proxies=proxy)
# print(resp.text)

import requests
url = "http://www.baidu.com"
resp = requests.get(url)
print("cookies: {}".format(resp.cookies))
print("cookies_dict: {}".format(resp.cookies.get_dict()))
"""
结果：
    cookies: <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    cookies_dict: {'BDORZ': '27315'}
"""