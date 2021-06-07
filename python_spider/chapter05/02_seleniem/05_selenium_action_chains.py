
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

# 测试行为链
inputTag = driver.find_element_by_id("kw")
submitBt = driver.find_element_by_id("su")

action = ActionChains(driver)  #创建 ActionChaions
action.move_to_element(inputTag)
action.send_keys_to_element(inputTag, "python")
action.move_to_element(submitBt)
action.click(submitBt)
action.perform()  # 执行所有行为