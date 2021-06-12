import scrapy


class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['a1i2z3uobaike.com']
    start_urls = ['http://a1i2z3uobaike.com/chenlong/login.php']

    def parse(self, response):

        url = "http://a1i2z3uobaike.com/chenlong/login.php"
        headers = {
            "Cookie": "PHPSESSID=oe5nkt4ca1jrhltqho2bfl8g47; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1623392325; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1623392325",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "aizuobaike.com",
            "Origin": "http://aizuobaike.com",
            "Referer": "http://aizuobaike.com/chenlong/login.php?gotopage=%2Fchenlong%2F",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        }
        data = {
            "gotopage": "/chenlong/",
            "dopost": "login",
            "adminstyle": "newdedecms",
            "userid": "admin",
            "pwd": "admin",
            "validate": "WDCL",
            "sm1": "",
        }

        request = scrapy.FormRequest(url=url, headers=headers, callback=self.paser_page, formdata=data)
        yield request

    def paser_page(self, response):
        print(" # " * 10)
        print(response.text)
        with open("test.html", "wb") as fp:
            fp.write(response.body)
        print(" # " * 10)

"""
表单能都发送成功，但是验证码出错
"""