from selenium import webdriver

driver_path = r"D:\chromedriver_win32\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http//114.101.250.113:9999")

driver = webdriver.Chrome(executable_path=driver_path, options=options)

driver.get("http://httpbin.org/ip")

