import requests
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Referer": "http://www.weather.com.cn/textFC/db.shtml",
}

def parse_page(url):
    # 获取天气预报页面
    response = requests.get(url=url, headers=HEADERS)
    text = response.content.decode("utf-8")
    # print(text)

    # 通过 BeautifulSoup 解析html 页面,并获取到面所有 table 标签内容
    # 使用 html5lib 代替 lxml: 由于 gat.html 页面的天气数据，只有 <table>, 没有  </table>,
    # lxml 解析不了，会报错，但是通过 浏览器解析后我们看到的html , 浏览器已经帮我们补全所以看出是少了闭合标签
    # 如果通过 html5lib解析器 解析, 返回的 table 会帮程序补全闭合标签
    # 安装命令: pip3 install html5lib
    soup = BeautifulSoup(text, "html5lib")
    # 页面会有7天的数据（默认使用第一个（今天））
    conMidtab = soup.find("div", class_="conMidtab")
    tables = conMidtab.find_all("table")

    # 解析每个表格的数据
    cities = []
    for table in tables:
        # print(table)
        trs = table.find_all("tr")[2:]  # 第一二行为表头
        # 解析每一行的数据
        for index, tr in enumerate(trs):
            tds = tr.find_all("td")
            td = tds[0]
            if index == 0: td = tds[1]  # 数据的第一行的第一列是省份，第二列才是城市
            city = list(tds[0].stripped_strings)[0]
            min_temp = list(tds[-2].stripped_strings)[0]
            cities.append({"city": city, "min_temp": int(min_temp)})
    return cities

def creat_html(xdata, ydata):
    bar = Bar()
    bar.add_xaxis(xdata)
    bar.add_yaxis("城市", ydata)
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="城市最低温度排序后10名", subtitle="我是副标题"),
        # brush_opts=opts.BrushOpts(),
    )
    # 渲染数据并保存到html 页面
    bar.render("bar_with_brush.html")

def main():
    all_data = []
    url_list = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml",
    ]
    for url in url_list:
        datas = parse_page(url)
        all_data.extend(datas)
    # 通过匿名函数设置排序的key
    all_data.sort(key=lambda data: data["min_temp"])

    # url = "http://www.weather.com.cn/textFC/gat.shtml"
    # datas = parse_page(url)
    # all_data.extend(datas)
    # all_data.sort(key=lambda data: data["min_temp"])

    # 通过 pyecharts 将 城市最低温度 排序 最高 的10个城市显示成 html
    show_data = all_data[-10:]
    cities = list(map(lambda data: data["city"], show_data))
    min_temps = list(map(lambda data: data["min_temp"], show_data))
    creat_html(cities, min_temps)

    print("all_data: ", all_data)


if __name__ == '__main__':
    main()
