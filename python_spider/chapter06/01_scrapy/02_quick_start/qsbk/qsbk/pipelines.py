# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import json
#
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open("duanzi.json", "w", encoding="utf-8")
#
#     def open_spider(self, spider):
#         print("爬虫开始。。。。")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + "\n")
#         return item
#
#     def close_spider(self, spider):
#         print("爬虫结束。。。")
#         self.fp.close()

# from scrapy.exporters import JsonItemExporter
#
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, encoding="utf-8", ensure_ascii=False )
#
#     def open_spider(self, spider):
#         print("爬虫开始。。。。")
#         self.exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         print("爬虫结束。。。")
#         self.exporter.finish_exporting()
#         self.fp.close()

from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline:
    def __init__(self):
        self.fp = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, encoding="utf-8", ensure_ascii=False )

    def open_spider(self, spider):
        print("爬虫开始。。。。")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        print("爬虫结束。。。")
        self.fp.close()


