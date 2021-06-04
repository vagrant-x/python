"""
需求：
从古诗文网站下载古诗文信息
使用 re 模块和 正则表达式 进行解析
"""

import re
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
}

def parse_page(url):
    # 获取页面数据
    response = requests.get(url, HEADERS)
    text = response.content.decode("utf-8")

    # re.S = re.DOTALL : 使特殊字符与任何字符都匹配，包括换行符。没有此标识，"." 将匹配换行符之外的任何内容
    titles = re.findall(r'<div\s*class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)  # 获取题目
    outhers = re.findall(r'<p\s*class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)  # 获取作者
    contents = re.findall(r'<div\s*class="contson".*?>(.*?)</div>', text, re.DOTALL)  # 获取诗句
    contents = list(map(lambda data: re.sub(r'<.*?>', "", data).strip(), contents))  # 去掉换行

    # 组装成（title, outher, content）的列表
    poem_list = list(zip(titles, outhers, contents))
    poems_dict = []
    for p in poem_list:
        p_dict = {}
        p_dict["title"] = p[0]
        p_dict["outher"] = p[1]
        p_dict["content"] = p[2]
        poems_dict.append(p_dict)
    return poems_dict

def main():
    poems = []
    for i in range(1, 5):
        print(i)
        url = "https://www.gushiwen.cn/default_{}.aspx".format(i)
        sub_poems = parse_page(url)
        poems.extend(sub_poems)
    print("poems = ", poems)

if __name__ == '__main__':
    main()