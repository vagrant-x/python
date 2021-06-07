import time
from selenium import webdriver

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

time.sleep(5)
# driver.close()  # 关闭页面
driver.quit()