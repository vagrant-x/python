
from urllib import request

csdn_url = "http://47.106.134.39:10086/wp-blog/wp-admin/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER",
    # "Origin": "https://mp.csdn.net",
    "Referer": "http://47.106.134.39:10086/wp-blog/wp-login.php",
    "Cookie": "wordpress_143dbe2bf39634bb00ebe77d685bad79="
              "admin%7C1623728016%7CTizOsc9GjD9BVvku7NSAUUYHdhdsNP3wKCrKj0AurSF%"
              "7C3ebadcce94763d4e004793919da9fabb87431cecb47ea539a9871c067364ec91; "
              "wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_143dbe2bf39634bb00ebe77d685bad79"
              "=admin%7C1623728016%7CTizOsc9GjD9BVvku7NSAUUYHdhdsNP3wKCrKj0AurSF%7C099f9d1ffeb11c6f155feee"
              "c7f7c25e0c0092aa4f789709d2b10c2b04fcccf84; "
              "wp-settings-1=libraryContent%3Dbrowse; wp-settings-time-1=1622518418"
}
req = request.Request(csdn_url, headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))
with open("test_cookie.html", "wb") as f:
    f.write(resp.read())
'''
在没有设置 Cookie 的情况下，请求url 获取到的是登录页面的数据
设置了有效的 Cookie 数据之后，能正确获取到页面数据
'''
# ---------------------------------------------------------------------------


"""
通过python 登陆获取 cookie ：
"""
from urllib import request, parse
from http.cookiejar import CookieJar
# 1、登录
# 1.1、创建一个 cookiejar 对象
cookiejar = CookieJar()
# 1.2、使用 cookiejar 创建一个 HTTPCookieProcess 对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3、使用上一步创建的 handler 创建一个 opener
opener = request.build_opener(handler)
# 1.4、使用 opener 发送登陆的请求（账号和密码）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
data = {
    "log":"313067870@qq.com",
    "pwd":"Qsdf_082255",
    "wp-submit":"Log In",
    "redirect_to":"http://47.106.134.39:10086/wp-blog/wp-admin/",
    "testcookie":"1"
}
login_url = "http://47.106.134.39:10086/wp-blog/wp-login.php"
data_bytes = parse.urlencode(data).encode("utf-8")
req = request.Request(url=login_url, headers=headers, data=data_bytes)
opener.open(req) # 这里为了获得 Cookie 不用接受返回，Cookie 会存在 cookiejar

#2、访问个人主页
admin_url = "http://47.106.134.39:10086/wp-blog/wp-admin/"
# 获得个人主页的页面的时候，不用新建一个opener
# 而应该使用之前的那个 opener， 因为之前的那个 opener 已经包含了登陆需要的 cookie 信息
req = request.Request(admin_url, headers=headers)
resp =opener.open(req)
with open("admin.html", "wb") as f:
    f.write(resp.read())

# ---------------------------------------------------------------------------


"""
通过python 登陆获取 cookie ：封装成方法 
"""
from urllib import request, parse
from http.cookiejar import CookieJar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
def get_opener():
    # 1、登录
    # 1.1、创建一个 cookiejar 对象
    cookiejar = CookieJar()
    # 1.2、使用 cookiejar 创建一个 HTTPCookieProcess 对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3、使用上一步创建的 handler 创建一个 opener
    opener = request.build_opener(handler)
    return opener


def login(opener):
    # 1.4、使用 opener 发送登陆的请求（账号和密码）
    data = {
        "log":"313067870@qq.com",
        "pwd":"Qsdf_082255",
        "wp-submit":"Log In",
        "redirect_to":"http://47.106.134.39:10086/wp-blog/wp-admin/",
        "testcookie":"1"
    }
    login_url = "http://47.106.134.39:10086/wp-blog/wp-login.php"
    data_bytes = parse.urlencode(data).encode("utf-8")
    req = request.Request(url=login_url, headers=headers, data=data_bytes)
    opener.open(req) # 这里为了获得 Cookie 不用接受返回，Cookie 会存在 cookiejar

def visit_profile(opener):
    #2、访问个人主页
    admin_url = "http://47.106.134.39:10086/wp-blog/wp-admin/"
    # 获得个人主页的页面的时候，不用新建一个opener
    # 而应该使用之前的那个 opener， 因为之前的那个 opener 已经包含了登陆需要的 cookie 信息
    req = request.Request(admin_url, headers=headers)
    resp =opener.open(req)
    with open("admin.html", "wb") as f:
        f.write(resp.read())

if __name__ == '__main__':
    opener = get_opener()
    login(opener)
    visit_profile(opener)
