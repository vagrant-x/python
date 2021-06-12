import scrapy

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        ua = response.json()
        print("*" * 30)
        print(ua)
        print("*" * 30)
        return scrapy.Request(self.start_urls[0], dont_filter=True)

