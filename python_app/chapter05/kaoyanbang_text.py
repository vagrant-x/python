# 执行命令安装appium 客户端
# pip3 install Appium-Python-Client

"""
介绍：inspector + uiautomatorviewer + appium + 夜神模拟器
功能：（1）该脚本通过 appium 连接夜神模拟器，打开 考研帮app，
      （2）然后跳过初始化验证等页面，进入输入账号密码页面进行登陆，
      （3）再跳转到 热门帖子 标签页，然后下拉页面多次
"""

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

KEY_TEL = "电话号码"
KEY_PW = "规则+常用"

cap = {
  "platformName": "Android",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "127.0.0.1:62001",
  "appium:appPackage": "com.tal.kaoyan",
  "appium:appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "appium:noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)


# 关闭： 无法播放 模态弹窗
def close_windows(driver):
    webElement = driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    print(webdriver)
    is_dispalyed = webElement.is_displayed()
    print("-----> 进入 close_windows, is_dispalyed = {}".format(str(is_dispalyed)))
    if is_dispalyed:
        driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='android:id/button1']").click()
        print("+++++> 点击 关闭 无法播放按钮")
    return True

def test_func():
    # 检查是否为第一次进入
    first_time = True
    try:
        print("判断是否第一次")
        WebDriverWait(driver, 30).until(lambda x: x.find_element(By.XPATH, "//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/activity_splash_bottom']"))
        first_time = False
    except:
        first_time = True

    if first_time:
        # 点击： 同意 用户协议
        try:
            print("-----> 查找用户协议：同意 按钮")
            if WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH,
                                                                       "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']")):
                driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']").click()
                print("+++++> 点击用户协议：同意按钮")
        except:
            print("？？？？？> 没有 用户协议：同意 按钮")

        # 点击： 我知道了 按钮
        try:
            print("-----> 查找欢迎页面：我知道了 按钮")
            if WebDriverWait(driver, 15).until(lambda x:x.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_ok']")):
                driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_ok']").click()
                print("+++++> 点击欢迎页面：我知道了 按钮")
        except:
            print("？？？？？> 没有 欢迎页面：我知道了 按钮")

    print("111111")
    # try:
    #     WebDriverWait(driver, 8).until_not(close_windows)
    # except:
    #     print("？？？？？> until_not 结束")
    # 等待 弹出框出来再出来
    WebDriverWait(driver, 40).until(lambda x: x.find_element(By.XPATH, "//android.widget.Button[@resource-id='android:id/button1']"))
    WebDriverWait(driver, 5).until_not(close_windows)

    # 选择 密码登录
    print("22222222")
    try:
        print("-----> 查找：密码登录 按钮")
        if WebDriverWait(driver, 5).until(lambda x:x.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/loginRegistorcodeAndPassword']")):
            driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/loginRegistorcodeAndPassword']").click()
            print("+++++> 点击密码登录 按钮")
    except:
        print("？？？？？> 没有 密码登录 按钮")

    # 勾选协议，设置账号密码，点击登陆
    if WebDriverWait(driver, 3).until(lambda x:x.find_element(By.XPATH, "//android.widget.CheckBox[@resource-id='com.tal.kaoyan:id/loginTreatyCheckboxPassword']")):
        driver.find_element(By.XPATH, "//android.widget.CheckBox[@resource-id='com.tal.kaoyan:id/loginTreatyCheckboxPassword']").click()
        driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/loginEmailEdittext']").send_keys(KEY_TEL)
        driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/loginPasswordEdittext']").send_keys(KEY_PW)
        time.sleep(2)
        driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/loginLoginBtn']").click()

        # 跳过初始化设置
        try:
            if WebDriverWait(driver, 80).until(lambda x: x.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/kylogin_perfect_tag_jump_button']")):
                driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/kylogin_perfect_tag_jump_button']").click()
                print("+++++> 点击 跳过 按钮")
        except:
            print("？？？？？> 不需要点击跳过")

        # 进入 热门帖子
        try:
            if WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, "//android.widget.TextView[@text='热门帖子']")):
                driver.find_element(By.XPATH, "//android.widget.TextView[@text='热门帖子']").click()
                print("+++++> 点击 热门帖子 按钮")
        except:
            print("？？？？？> 点击 热门帖子 超时")

        # 获取宽高后滑动
        width = driver.get_window_size()["width"]
        height = driver.get_window_size()["height"]
        w1 = int(width * 0.5)
        h1 = int(height * 0.75)
        h2 = int(height * 0.25)

        for i in range(5):
            driver.swipe(w1, h1, w1, h2)
            time.sleep(1)
            print("滑动第 {} 次".format(str(i)) )

if __name__ == '__main__':
    print("------ 程序开始 -----")
    test_func()
    print("------ 程序退出 -----")