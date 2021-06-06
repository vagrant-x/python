from gevent import monkey; monkey.patch_all()  # 必须在首行
import requests, os, re, time, gevent
from urllib import request
from lxml import etree


def parse_page(url):
    url_list = []
    # 封装请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    # 根据网站的编码格式对内容解码
    text = response.content.decode("utf-8")
    html = etree.HTML(text)  # 解析页面内容
    # 通过xpath 找到指定 img 标签
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get("data-original")  # 获取属性
        alt = img.get("alt")  # 图片中文名
        alt = re.sub(r'[\?？，。！!\.\*/\|]', "", alt)  # 替换掉不合法的文件名标识
        suffix = os.path.splitext(img_url)[1]  # 获取后缀
        filename = os.path.basename(img_url)  # 获取文件名
        if alt:  # 如果中文属性为空，文件名用原来的
            filename = alt + suffix
        # print("下载图片：{}".format(filename))
        # request.urlretrieve(img_url, "images/" + filename)
        url_list.append((img_url, "images/" + filename))
    return url_list

def download_img(url, filename):
    print("开始下载图片：{}".format(filename))
    request.urlretrieve(url, filename)

def main():
    #  下载斗图啦网站前5页最新表情中的图片
    all_url_list = []
    for i in range(1, 6):
        url = "https://www.doutula.com/photo/list/?page={}".format(i)
        urls = parse_page(url)
        # print(urls)
        all_url_list.extend(urls)

    # 使用 gevent 模块实现协程，下载图片
    print("解析完成，开始下载")
    list1 = []
    for url, filename in all_url_list:
        list1.append(gevent.spawn(download_img, url, filename))
    gevent.joinall(list1)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("花费时间：{}".format(end_time - start_time))  # 14.8
