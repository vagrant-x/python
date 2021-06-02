"""
需求：爬取豆瓣网正在上映的电影信息
链接：https://movie.douban.com/cinema/nowplaying/guangzhou/
网页手动保存到当前目录：03_douban.html
"""
import requests
from lxml import etree

# 1、将目标网站上的页面抓取下来
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Referer": "https://movie.douban.com/cinema/nowplaying/guangzhou/"
}
url = "https://movie.douban.com/cinema/nowplaying/guangzhou/"
resp = requests.get(url=url, headers=headers)
text = resp.content
# 解码方式根据html 设置的编码：<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
# print(text.decode("utf-8"))

# 2、将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]  # 有两个：1.正在上映，2.即将上映
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    address = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    img_src = li.xpath(".//img/@src")[0]
    movie = {
        "title": title,  # 电影名
        "score": score,  # 评分
        "duration": duration,  # 时长
        "address": address,  # 国家
        "director": director,  # 导演
        "actors": actors,  # 主演
        "img_scr": img_src  # 图片
    }
    movies.append(movie)
print(movies)

