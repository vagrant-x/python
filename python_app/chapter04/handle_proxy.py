import requests

url = "http://www.httpbin.org/ip"
# 私密代理
# proxies={
# 'http':user+':'+password+'@127.0.0.1:8080',
# 'https':user+':'+password+'@127.0.0.1:8080'
# }
proxies = {"http": "127.0.0.1:8888"}  # 通用代理
response = requests.get(url=url, proxies=proxies)
print(response.text)