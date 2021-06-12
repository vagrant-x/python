# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from crv import settings
from urllib import request
from scrapy.pipelines.images import ImagesPipeline

class CrvPipeline:
    def __init__(self):
        self.images_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")
        if not os.path.exists(self.images_path):
            os.mkdir(self.images_path)

    def process_item(self, item, spider):
        # 获取 图片分类并创建保存文件夹
        title = item["title"]
        title_path = os.path.join(self.images_path, title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)

        # 下载图片
        urls = item["urls"]
        for url in urls:
            img_name = url.split("_")[-1]
            img_path = os.path.join(title_path, img_name)
            request.urlretrieve(url, img_path)
        return item

class CrvImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        # 这个方法是在图片将要被存储的时候调用，来获取这个图片的存储路径。
        category = item["title"]
        category_path = os.path.join(settings.IMAGES_STORE, category)
        image_name = request.url.split("_")[-1]
        image_path = os.path.join(category_path, image_name)
        print("image_path ; {}".format(image_path))
        return image_path
