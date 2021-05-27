# 由于IO操作非常耗时，程序经常会处于等待状态
# 比如请求多个网页有时候需要等待，gevent可以自动切换协程
# 遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()解决
# 首行添加下面的语句即可
from gevent import monkey; monkey.patch_all()
import gevent
import requests
import time

start = time.time()

def fun1(url):
    print("GET: {}".format(url))
    resp = requests.get(url)
    data = resp.text
    print("{} bytes received from {}".format(len(data), url))

# fun1('https://www.python.org/')
# # fun1('https://www.yahoo.com/')
# fun1('https://baidu.com/')
# fun1('https://www.sina.com.cn/')

gevent.joinall([
    gevent.spawn(fun1, "https://github.com/kubernete"),
    gevent.spawn(fun1, 'https://www.sina.com.cn/'),
    gevent.spawn(fun1, 'https://www.python.org/'),
    gevent.spawn(fun1, 'https://www.yahoo.com/'),
    gevent.spawn(fun1, 'https://www.baidu.com/')
])

if __name__ == '__main__':
    print("cost time = {}".format(time.time() - start))