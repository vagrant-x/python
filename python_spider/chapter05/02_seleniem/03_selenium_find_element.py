import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

# inputTag = driver.find_element_by_id("kw")
# inputTag = driver.find_element(By.ID, "kw")

# inputTag = driver.find_element_by_name("wd")
# inputTag = driver.find_element(By.NAME, "wd")

# inputTag = driver.find_element_by_class_name("s_ipt")
# inputTag = driver.find_element(By.CLASS_NAME, "s_ipt")

# inputTag = driver.find_element_by_tag_name("input")
# inputTag = driver.find_element(By.TAG_NAME, "input")

# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag = driver.find_element(By.XPATH, "//input[@id='kw']")

# inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag = driver.find_element(By.CSS_SELECTOR, ".quickdelete-wrap > input")

inputTag.send_keys("python")