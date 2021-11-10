import scrapy
import re
from fang.items import NewHouseItem, ESFHouseItem

class FSpider(scrapy.Spider):
    name = 'f'
    allowed_domains = ['fang.com']
    start_urls = ['https://fang.com/SoufunFamily.htm']


    """
        广州的url: http://gz.fang.com/
            广州新房url: https://gz.newhouse.fang.com/house/s/
            广州二手房url: https://gz.esf.fang.com/
    """
    def parse(self, response):
        trs = response.xpath("//div[@id='c02']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td")
            p_text = tds[1].xpath('.//text()').get()
            p_text = re.sub(r'\s', "", p_text)  # 获取省份信息
            if p_text:
                province = p_text
            if province == "其它":  # 中国以外的不获取
                continue
            links = tds[2].xpath(".//a")
            for a in links:
                city_name = a.xpath("./text()").get()  # 获取城市名称
                city_url = a.xpath("./@href").get()  # 获取城市url
                if city_name == "北京":  # 北京需要特殊处理
                    continue  # 先跳过
                    # newhouse_url = "https://newhouse.fang.com/house/s/"
                    # esf_url = "https://esf.fang.com/"
                else:
                    newhouse_url = re.sub("\.", ".newhouse.", city_url, count=1) + "house/s/"  # 拼接城市新房链接
                    esf_url = re.sub("\.",  ".esf.",city_url, count=1)  # 拼接城市二手房链接
                print("省份： {}， 城市： {}， url：{}".format(province, city_name, city_url))
                print("省份： {}， 城市： {}， newhouse_url：{}, esf = {}".format(province, city_name, newhouse_url, esf_url))
                # 请求新房页面
                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse,
                                     meta={"info": (province, city_name)})
                # 请求二手房页面
                yield scrapy.Request(url=esf_url, callback=self.parse_esf,
                                     meta={"info": (province, city_name)})
            #     break
            # break

    def parse_newhouse(self, response):
        province, city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class, 'nl_con')]/ul/li")
        for li in lis:
            # 小区名称
            name = li.xpath(".//div[contains(@class, 'nlcd_name')]/a/text()").get().strip()
            # 价格
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r'\s|暂未取得预售证', "", price)
            # 几居
            rooms = li.xpath(".//div[contains(@class, 'house_type')]/a/text()").getall()
            # 面积
            area = "".join(li.xpath(".//div[contains(@class, 'house_type')]/text()").getall())
            area = re.sub(r'\s|—|/', "", area)
            # 地址
            address = li.xpath(".//div[@class='address']/a/@title").get()
            # 行政区
            district = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district = re.search(".*\[(.+)\].*", district).group(1)
            # 是否在售
            sale = li.xpath(".//div[@class='fangyuan']/span/text()").get()
            sale = re.sub(r"\s", "", sale)
            # 房天下详情页面的url
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            item = NewHouseItem(
                    province=province,
                    city=city,
                    name=name,
                    price=price,
                    rooms=rooms,
                    area=area,
                    address=address,
                    district=district,
                    sale=sale,
                    origin_url=origin_url
                )
            print(item)
            yield item
            # 获取：下一页数据
            next_url = response.xpath(".//div[@class='page']//a[@class='next']/@href").get()
            next_url = response.urljoin(next_url)
            print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_newhouse, meta={"info":(province, city)})

    def parse_esf(self, response):
        province, city = response.meta.get("info")
        dls = response.xpath("//div[contains(@class, 'shop_list')]/dl")
        for dl in dls:
            item = ESFHouseItem(province=province, city=city)
            # 小区名字
            name = dl.xpath(".//dd[1]/p[@class='add_shop']/a/text()").get()
            if name is None:  # 如果插入的是刚刚，直接跳过
                continue
            item["name"] = re.sub("\s", "", name)

            infos = dl.xpath(".//dd[1]/p[@class='tel_shop']//text()").getall()
            for info in infos:
                info = re.sub("\s", "", info)
                if "室" in info:  # 几居，这是一个列表
                    item["rooms"] = info
                elif "层" in info:  # 层
                    item["floor"] = info
                elif "向" in info:  # 朝向
                    item["toward"] = info
                elif "年" in info:  # 年代
                    item["year"] = re.sub("年建", "", info)
                elif "㎡" in info:  # 面积
                    item["area"] = info
            # 地址
            item["address"] = dl.xpath(".//dd[1]/p[@class='add_shop']/span/text()").get()
            # 价格
            price = "".join(dl.xpath(".//dd/span[contains(@class, 'red')]//text()").getall())
            item["price"] = re.sub("\s", "", price)
            # 单价
            item["unit"] = dl.xpath(".//dd[@class='price_right']/span[last()]/text()").get()
            # 房天下详情页面的url
            origin_url = dl.xpath(".//dd[1]/h4[@class='clearfix']/a/@href").get()
            item["origin_url"] =response.urljoin(origin_url)
            yield item
        # print(response.text)
        next_page = response.xpath("//div[@class='page_al']/p[3]/a/text()").get()
        print("------->{}".format(next_page))
        if next_page is not None and "下一页" in next_page:
            next_url = response.xpath(".//div[@class='page_al']/p[3]/a/@href").get()
            print(next_url)
            next_url = response.urljoin(next_url)
            print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse_esf, meta={"info":(province, city)})


# 问题
    # 1 北京的时候会自动跳转
    # 2 下一页按钮找不到