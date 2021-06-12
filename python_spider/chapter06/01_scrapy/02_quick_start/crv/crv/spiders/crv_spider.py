import scrapy
from crv.items import CrvItem

class CrvSpiderSpider(scrapy.Spider):
    name = 'crv_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series-s46246/314.html#pvareaid=3454542']

    def parse(self, response):
        divs = response.xpath("//div[@class='column grid-16']/div")[2:]  # 过滤掉1，2 行
        for div in divs:
            print(div.xpath(".//div[@class='uibox-title']"))
            title = div.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = div.xpath(".//ul/li/a/img/@src").getall()
            urls = list(map(response.urljoin, urls))
            item = CrvItem(title=title, urls=urls)
            print(item)
            yield item
