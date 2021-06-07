"""
    常见的表单元素
        input type='text/ password/ email/ number'
        button input[type='submit']
        checkbox input='checkbox'
        select 下拉列表
"""

# import time
# from selenium import webdriver
#
# driver_path = r"D:\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.baidu.com")
#
# # 操作输入框
# inputTag = driver.find_element_by_id("kw")
# inputTag.send_keys("python")
# time.sleep(3)
# inputTag.clear()


import time
from selenium import webdriver

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

# 操作输入框
inputTag = driver.find_element_by_id("kw")
inputTag.send_keys("python")
submitBt = driver.find_element_by_id("su")
submitBt.click()
