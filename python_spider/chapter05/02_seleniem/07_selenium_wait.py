# from selenium import webdriver
#
# driver_path = r"D:\chromedriver_win32\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# # 隐式等待
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com")
#
# driver.find_element_by_id("123")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")
# 显式等待
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "123"))
    )
finally:
    print("退出浏览器")
    driver.quit()