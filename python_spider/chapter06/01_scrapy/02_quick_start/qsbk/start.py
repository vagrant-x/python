from scrapy import cmdline

# 下面是等价的
cmdline.execute(["scrapy", "crawl", "qsbk_spider"])
# cmdline.execute("scrapy crawl qsbk_spider".split())