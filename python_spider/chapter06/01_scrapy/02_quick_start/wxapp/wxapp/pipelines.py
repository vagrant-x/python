# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter


class WxappPipeline:
    def __init__(self):
        self.fp = open("wxapp.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, encoding="utf-8", ensure_ascii=False)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        print("准备关闭")
        self.fp.close()