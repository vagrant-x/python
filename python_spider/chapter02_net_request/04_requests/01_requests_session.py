
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
data = {
    "log": "313067870@qq.com",
    "pwd": "Qsdf_082255",
    "wp-submit": "Log In",
    "redirect_to": "http://47.106.134.39:10086/wp-blog/wp-admin/",
    "testcookie": "1"
}
login_url = "http://47.106.134.39:10086/wp-blog/wp-login.php"
admin_url = "http://47.106.134.39:10086/wp-blog/wp-admin/"

session = requests.Session()
session.post(login_url, data=data, headers=headers)
response = session.get(admin_url)
with open("admin.html", "wb") as f:
    f.write(response.content)
