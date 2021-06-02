"""
需求：爬取 电影天堂 最新电影信息
链接：https://dytt8.net/html/gndy/dyzz/index.html
网页手动保存到当前目录：04_dytt.html
"""

import requests
from lxml import etree

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Referer": "https://dytt8.net/html/gndy/dyzz/index.html"
}
BASE_URL = "https://dytt8.net"

def get_detail_urls(url):
    """
    根据url获取电影的详情链接
    :param url: 请求的url
    :return: 电影详情信息的url 列表
    """
    resp = requests.get(url=url, headers=HEADERS)
    text = resp.text
    html = etree.HTML(text)
    # 用最快速的方法找到电影详情的链接，通过 table 的 class=tbspan 快速定位
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = list(map(lambda url: BASE_URL + url, detail_urls))  # 将map对象转换成list
    return detail_urls

def get_detail_page(url):
    movie = {}  # 保存电影信息
    resp = requests.get(url=url, headers=HEADERS)
    try:
        text = resp.content.decode("gb2312")  # 有无法解析的字符
    except UnicodeDecodeError as e:
        print("出现无法解析的符号,直接跳过")
        return None
    # text = resp.text
    html = etree.HTML(text)
    # 查询电影名称
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie["title"] = title

    # 其他信息在 id="Zoom" 的div里面
    zoomEle = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomEle.xpath("//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie["cover"] = cover  # 电影图片链接
    movie["screenshot"] = screenshot

    def parse_info(rule, info):
        return info.replace(rule, "").strip()

    infos = zoomEle.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎片　　名"):
            name = parse_info("◎片　　名", info)
            movie["name"] = name
        elif info.startswith("◎年　　代"):
            year = parse_info("◎年　　代", info)
            movie["year"] = year
        elif info.startswith("◎产　　地"):
            address = parse_info("◎产　　地", info)
            movie["address"] = address
        elif info.startswith("◎类　　别"):
            category = parse_info("◎类　　别", info)
            movie["category"] = category
        elif info.startswith("◎语　　言"):
            language = parse_info("◎语　　言", info)
            movie["language"] = language
        elif info.startswith("◎豆瓣评分"):
            rating = parse_info("◎豆瓣评分", info)
            movie["rating"] = rating
        elif info.startswith("◎片　　长"):
            duration = parse_info("◎片　　长", info)
            movie["duration"] = duration
        elif info.startswith("◎导　　演"):
            movie["director"] = parse_info("◎导　　演", info)
        elif info.startswith("◎主　　演"):
            actor = parse_info("◎主　　演", info)
            actors = [actor]
            for i in range(index+1, len(infos)):
                if infos[i].startswith("◎标　　签"): break
                actors.append(infos[i].strip())
            movie["actors"] = actors
        elif info.startswith("◎标　　签"):
            movie["director"] = parse_info("◎标　　签", info)
        elif info.startswith("◎简　　介"):
            profile = ""
            for i in range(index+1, len(infos)):
                if infos[i].startswith("磁力链"): break
                profile += infos[i].strip()
            movie['profile'] = profile

    link = zoomEle.xpath(".//a/@href")[0]
    movie['link'] = link
    return movie


def spider():
    movies = []
    url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    # 获取7页的电影信息
    for i in range(1, 8):  # 循环获取所有电影详情链接
        url = url.format(i)
        detail_urls = get_detail_urls(url)
        print(detail_urls)
        for detail_url in detail_urls:  # 循环获取电影信息
            movie = get_detail_page(detail_url)
            movies.append(movie)
            print(movie)

    # # 先用第一页测试
    # url = "https://dytt8.net/html/gndy/dyzz/list_23_1.html"
    # detail_urls = get_detail_urls(url)
    # for detail_url in detail_urls:
    #     movie = get_detail_page(detail_url)
    #     movies.append(movie)
    #     # print(movie)
    #     break


if __name__ == '__main__':
    spider()

