"""
使用 selenium + chromedriver 来实现 12306 抢票

1、让浏览器打开 12306 的登录页面，然后手动进行登录
2、登录完成后让浏览器跳转到购票界面。
3、手动的输入出发地，目的地以及出发日期，检测到以上三个信息都输入完成后，
    然后找到查询按钮，执行点击事件，进行车次查询
4、查找我们需要的车次，然后看下对应的席位是否还有余票（有、数字）。找到这个车次的预定按钮，
    然后执行点击事件。如果没有出现以上两个（有、数字），那么我们就让循环这个查询工作
5、一旦检测到邮票（有、数字），那么执行预定按钮的点击事件，来到预定的界面后，
    找到对应的乘客，然后执行这个乘客的 checkbox, 然后执行点击事件，再找到提交订单的按钮，
    执行点击事件。
6、点击完提交订单按钮后，会弹出一个确认的对话框，然后找到“确认按钮”，然后执行点击事件，完成抢票。

"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Qiangpiao():
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.login_success_url = "https://kyfw.12306.cn/otn/view/index.html"
        self.init_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        self.driver = webdriver.Chrome(executable_path=r"D:\chromedriver_win32\chromedriver.exe")

    def run(self):
        self._wait_input()
        self._login()
        self._order_ticket()

    def _wait_input(self):
        self.from_station = input("出发地：")
        self.to_station = input("目的地：")
        self.depart_time = input("出发时间：")
        self.passengers = input("乘客姓名（如有多个乘客，用英文逗号隔开）：").split(",")
        self.trains = input("车次（如有多个车次，请用英文逗号隔开）：").split(",")

    def _login(self):
        print("---> 打开登录页面")
        self.driver.get(self.login_url)
        # 隐式等待 : 直到判断 url 为登录成功的 url
        WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.login_success_url))
        print("登陆成功")
        # 等待提示框弹出
        # WebDriverWait(self.driver, 1000).until(
        #     EC.presence_of_all_elements_located(By.XPATH, "//a[@class='btn-primary']")
        # )
        # # 关闭提示框
        # a_element = self.driver.find_element_by_xpath("//a[@class='btn-primary']")
        # a_element.click()
        # print("已经关闭提示框")

    def _order_ticket(self):
        # 1、跳转到订单页面
        self.driver.get(self.init_url)

        # 设置查询信息
        print("开始设置输入框的内容")
        # 设置了没成功
        # from_input_ele = self.driver.find_element_by_id("fromStationText")
        # from_input_ele.send_keys(self.from_station)
        # to_input_ele = self.driver.find_element_by_id("toStationText")
        # to_input_ele.send_keys(self.to_station)
        # time.sleep(1)
        # train_date_input_ele = self.driver.find_element_by_id("train_date")
        # train_date_input_ele.send_keys(self.depart_time)
        print("内容设置完成")

        # 2、等待出发点输入是否争取
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station)
        )
        # 3、等待目的地输入是否正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )
        # 4、等待出发日期输入是否正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )
        # 5、等待按钮是否可用
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )
        # 6、如果可以被点击，查找按钮并点击
        searchBtn = self.driver.find_element_by_id("query_ticket")
        time.sleep(1)
        searchBtn.click()
        print("点击了按钮")

        # 7、在点击了查询按钮之后，等待车次信息是否显示出来了
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_all_elements_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
        )
        print("sleep5")
        time.sleep(5)
        # 8、找到所有没有 datatran 属性的tr标签，这些标签存储了车次信息  find_elements_by_xpath
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        # print("tr_list :{}".format(tr_list))
        time.sleep(1)
        # 9、遍历所有满足添加的 tr 标签
        for tr in tr_list:
            train_number = tr.find_element_by_class_name("number").text
            print(train_number)
            if train_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                if left_ticket == "有" or left_ticket.isdigit:
                    orderBtn = tr.find_element_by_class_name("btn72")
                    orderBtn.click()
                    print("点击了预定按钮")
                    # 等待是否来确认乘客页面
                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.passenger_url)
                    )
                    print("已经进入页面")
                    break


if __name__ == '__main__':
    qp = Qiangpiao()
    qp.run()
    print("抢票结束")





