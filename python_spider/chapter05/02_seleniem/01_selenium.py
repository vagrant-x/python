from selenium import webdriver

# chromedriver.exe 的绝对路径
driver_path = r"D:\chromedriver_win32\chromedriver.exe"

# 初始化一个driver, 并且指定 chromedriver 的路径
driver = webdriver.Chrome(executable_path=driver_path)

# 请求网页
driver.get("https://www.baidu.com")

# 通过 page_source 获取网页源代码
print(driver.page_source)