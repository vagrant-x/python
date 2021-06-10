import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        # SelectorList
        duanziDivs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for duanziDiv in duanziDivs:
            # duanziDiv 类型： Selector
            auther = duanziDiv.xpath(".//h2/text()").get().strip()
            content = duanziDiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            item = QsbkItem(auther=auther, content=content)
            # duanzi = {"auther": auther, "content": content}
            # 方法将返回一个生成器
            yield item
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return   # 访问到最后一页没有“下一页”按钮，最后一个 li 没有 href
        else:
            # 重启创建一个请求，让调度器处理
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)

