import requests, os, re, time, threading, queue
from urllib import request
from lxml import etree

class Producer(threading.Thread):
    # 封装请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }

    def __init__(self, page_queue, img_queue,*args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():  # 如果队列为空，解析结束
                print("解析完成页面， {} 退出".format(threading.currentThread()))
                break
            url = self.page_queue.get()  # 获取页面url
            self.parse_page(url)  # 解析页面

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        # 根据网站的编码格式对内容解码
        text = response.content.decode("utf-8")
        html = etree.HTML(text)  # 解析页面内容
        # 通过xpath 找到指定 img 标签
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get("data-original")  # 获取属性
            alt = img.get("alt")  # 图片中文名
            alt = re.sub(r'[\?？，。！!\.\*/]', "", alt)  # 替换掉不合法的文件名标识
            suffix = os.path.splitext(img_url)[1]  # 获取后缀
            filename = os.path.basename(img_url)  # 获取文件名
            if alt:  # 如果中文属性为空，文件名用原来的
                filename = alt + suffix
            # print("下载图片：{}".format(filename))
            self.img_queue.put((img_url, "images/" + filename))  # 保存需要下载的图片数据到队列
            # request.urlretrieve(img_url, "images/" + filename)


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                print("下载完成，{} 退出".format(threading.currentThread()))
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, filename)
            print("下载完图片： {}".format(filename))

thread_list = []

def main():
    page_queue = queue.Queue(100)
    img_queue = queue.Queue(1000)
    #  下载斗图啦网站前5页最新表情中的图片
    for i in range(1, 6):
        url = "https://www.doutula.com/photo/list/?page={}".format(i)
        page_queue.put(url)
    # 启动 解析页面进程
    for i in range(3):
        p = Producer(page_queue, img_queue)
        p.start()
        thread_list.append(p)
    # 启动 下载图片进程
    for i in range(5):
        c = Consumer(page_queue, img_queue)
        c.start()
        thread_list.append(c)

if __name__ == '__main__':
    start_time = time.time()
    main()
    for t in thread_list:  # 阻塞主线程，计算总共时间
        t.join()
    end_time = time.time()
    print("花费时间：{}".format(end_time - start_time))  # 17s