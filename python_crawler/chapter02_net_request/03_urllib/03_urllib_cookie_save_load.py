# 保存cookie到本地
"""
本文通过 httpbin.org 提供的接口提交一个 cookie,设置成功后服务器会返回设置的 cookie 让浏览器保存
"""
from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar("cookie.txt")
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
req = request.Request("http://httpbin.org/cookies/set?myCookie=A0001", headers=headers)

resp =opener.open(req)
print(resp.read().decode("utf-8"))
# 设置 废弃 和 过期 的 cookie 都保存下来
cookiejar.save(ignore_discard=True, ignore_expires=True)

"""
结果 cookit.txt 文件中保存内容如下
    # Netscape HTTP Cookie File
    # http://curl.haxx.se/rfc/cookie_spec.html
    # This is a generated file!  Do not edit.
    
    httpbin.org	FALSE	/	FALSE		myCookie	A0001
"""
"""
cookiejar.save(ignore_discard=True, ignore_expires=True)
    ignore_discard = True : 即使cookies将被丢弃也将它保存下来
    ignore_expires = True : 如果cookies已经过期也将它保存并且文件已存在时将覆盖
    
"""

# ===========================================================================
from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar2 = MozillaCookieJar("cookie2.txt")
cookiejar2.load(ignore_discard=True, ignore_expires=True)
handler2 = request.HTTPCookieProcessor(cookiejar2)
opener2 = request.build_opener(handler2)

# 打印现有保存的 cookie
for c in cookiejar2:
    print(c)

"""
cookie2.txt 文件
    # Netscape HTTP Cookie File
    # http://curl.haxx.se/rfc/cookie_spec.html
    # This is a generated file!  Do not edit.
    
    httpbin.org	FALSE	/	FALSE		myCookie1	A0001
    httpbin.org	FALSE	/	FALSE		myCookie2	A0002
    
打印结果：
    <Cookie myCookie1=A0001 for httpbin.org/>
    <Cookie myCookie2=A0002 for httpbin.org/>
"""