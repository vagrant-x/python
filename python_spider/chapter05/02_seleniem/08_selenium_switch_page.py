from selenium import webdriver

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

# 打开一个新窗口
driver.execute_script("window.open('https://douban.com/')")
# 切换到新打开的页面
# driver.switch_to_window(driver.window_handles[1])  # 已经废弃
driver.switch_to.window(driver.window_handles[1])

print(driver.current_url)
# print(driver.page_source)

"""
虽然在 Chrome 窗口中显示的是新页面，但是 driver 中还没切换，
如果想要在代码中切换到新的页面，并且做一些爬虫，
那么应该使用 switch_to.window 来说切换到指定的窗口。
从 driver.window_handlers 是一个列表，里面装的都是窗口句柄。
他会按照打开页面的顺序来存储窗口的句柄。
"""