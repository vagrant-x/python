import re, time
from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By


class LagouSpider(object):

    driver_path = r"D:\chromedriver_win32\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="

    def run(self):
        self.driver.get(self.url)  # 请求页面
        while True:
            source = self.driver.page_source  # 获取html页面数据
            self.parse_list_page(source)  # 解析职位列表页面
            time.sleep(1)
            # 等待 xpath 寻找的元素出现，否则 10 s 抛出异常
            # 如果没有这一句，页面下一页的按钮可能还没加载出来，获取不到
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            )
            nextBtn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            print(nextBtn.get_attribute("class"))
            if "pager_next_disabled" in nextBtn.get_attribute("class"):
                print("已经到最后一页退出")
                break
            print("进入下一页")
            nextBtn.click()  # 这个需要放在 get_attribute 之后，否则点击之后会找不到，报错


    def parse_list_page(self, source):
        html = etree.HTML(source)
        hrefs = html.xpath("//a[@class='position_link']/@href")
        for href in hrefs:
            self.request_detail_page(href)
            time.sleep(1)

    def request_detail_page(self, url):
        self.driver.execute_script("window.open('{}')".format(url))
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到新打开的职位详情页
        source = self.driver.page_source  # 获取详情页面 html
        self.parse_detail_page(source)  # 解析 html
        self.driver.close()  # 关闭当前详情页面
        self.driver.switch_to.window(self.driver.window_handles[0])  # 切换回到职位列表页面

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        p_name = html.xpath("//span[@class='position-head-wrap-name']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        p_salary = job_request_spans[0].xpath(".//text()")[0]
        p_city = job_request_spans[1].xpath(".//text()")[0]
        p_city = re.sub(r"[\s/]", "", p_city)
        p_years = job_request_spans[2].xpath(".//text()")[0]
        p_years = re.sub(r"[\s/]", "", p_years)
        p_education = job_request_spans[3].xpath(".//text()")[0]
        p_education = re.sub(r"[\s/]", "", p_education)
        p_detail = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        p_info = {
            "p_name": p_name,
            "p_salary": p_salary,
            "p_city": p_city,
            "p_years": p_years,
            "p_education": p_education,
            "p_detail": p_detail,
        }
        print(p_info)
        print("* " * 20)
        return p_info


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
