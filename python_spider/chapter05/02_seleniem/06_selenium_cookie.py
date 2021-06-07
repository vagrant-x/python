from selenium import webdriver

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

# 查看所有
for cookie in driver.get_cookies():
    print(cookie)

print("查询某个 cookie" + "* " * 20)
# 查询某个 cookie
print(driver.get_cookie("BAIDUID"))

print("删除某个cookie " + "* " * 20)
# 删除某个 cookie
driver.delete_cookie("BAIDUID")
print(driver.get_cookie("BAIDUID"))

print("删除所有cookie " + "* " * 20)
driver.delete_all_cookies()