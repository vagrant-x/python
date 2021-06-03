from bs4 import BeautifulSoup

html = """
<html>
    <head><title>The Dormouse's story</title></head>
    <body>
        <div class="div_class">
            <p class="story" id="pid1" >python</p>
            <p class="story">广州</p>
            <p class="story2">python研发工程师</p>
        </div>
        <div  class="div_class">
            <p class="even">java</p>
            <p class="even">深圳</p>
            <p class="even">java研发工程师</p>
            <a id="test" class="test even" href="http://www.baidu.com">http://www.baidu.com</a>
        </div>
    </body>
</html>
"""

# 1、获取所有 p 标签
# 2、获取第二个 p 标签
# 3、获取所有 class 等于 even 的 p 标签
# 4、获取所有 id 等于 test, class 等于 test 的 a 标签
# 5、获取所有 a 标签的 herf 属性
# 6、获取所有的职位信息（纯文本）

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# 1、获取所有 p 标签
ps = soup.find_all("p")
# print(type(ps[0]))  # <class 'bs4.element.Tag'>
for p in ps:
    print(p)

# 2、获取第二个 p 标签
p = soup.find_all("p", limit=2)[1]
p = soup.find_all("p")[1]
print(p)

# 3、获取所有 class 等于 even 的 p 标签
ps = soup.find_all("p", class_="even")
ps = soup.find_all("p", attrs={"class": "even"})
for p in ps:
    print(p)

# 4、获取所有 id 等于 test, class 等于 test 的 a 标签
aList = soup.find_all("a", class_="test", id="test")
aList = soup.find_all("a", attrs={"class": "test", "id": "test"})
for a in aList:
    print(a)

# 5、获取所有 a 标签的 href 属性
aList = soup.find_all("a")
for a in aList:
    # 1、通过下标操作的方式
    print(a["href"])
    # 2、通过 attrs 属性的方式
    print(a.attrs["href"])

# 6、获取所有的职位信息（纯文本）
divs = soup.find_all("div")
positions = []
for div in divs:
    # 通过 tag.string 获取内容
    position = {}
    ps = div.find_all("p")
    language = ps[0].string
    address = ps[1].string
    name = ps[2].string
    position['language'] = language
    position['address'] = address
    position['name'] = name
    positions.append(position)

    # 通过 strings 获取内容
    gen = div.strings # 返回的是一个生成器
    # print(type(gen))  # <class 'generator'>
    infos = list(div.strings)  # 生成的列表带有空白数据
    positions.append(infos)
    # [['\n', 'python', '\n', '广州', '\n', 'python研发工程师', '\n'],
    #  ['\n', 'java', '\n', '深圳', '\n', 'java研发工程师', '\n', 'http://www.baidu.com', '\n']]

    # 通过 stripped_strings 获取内容
    gen = div.stripped_strings  # 返回的是一个生成器
    # print(type(gen))  # <class 'generator'>
    infos = list(div.stripped_strings)  # 生成的列表没有有空白数据
    positions.append(infos)
    # [['python', '广州', 'python研发工程师'],
    # ['java', '深圳', 'java研发工程师', 'http://www.baidu.com']]

    # 通过 get_text 获取内容
    print(type(div.get_text()))  # <class 'str'>
    print(div.get_text())

print(positions)

"""
find_all 的作用
    1、在提取标签的时候，第一个参数是标签的名字。然后如果在提取标签的时候想要使用标签的属性进行过滤，那么可以在这个地方通过关键字参数的形式，将属性的名字以及对应的值传进去。或者使用 atrs 属性， 将所有的属性以及对应的值放进一个字典传给 attrs 属性。
    2、有些时候，在提取标签的时候，不像提取那么多，那么可以使用 limit 参数，限制提取多少个。

find 与 find_all 的区别
    1、find：找到第一个满足条件的标签就返回。只会返回一个元素
    2、find_all：将所有满足条件的标签都返回
    
使用 find 和 find_all 的过滤条件
    1、关键字参数：将属性的名字作为关键字参数的 key ，属性的值作为关键字参数的 value。
    2、attrs 参数：将属性条件放到一个字典中，传给 attrs 参数
    
获取标签的属性：
    1、通过下标获取：通过标签的下标方式:
        href = a["href"]
    2、通过 attrs 属性获取
        href = a.attrs["href"]

string、strings、stripped_strings 和 get_text 方法：
    1、string：获取某个标签下的非标签字符串，返回的是一个字符串
    2、strings：获取某个标签下的子孙非标签字符串，返回的是一个生成器
    3、stripped_strings：获取某个标签下的子孙非标签字符串，去掉空白字符串。返回的是一个生成器
    4、get_text：获取某个标签下的子孙非标签字符串。以普通字符串返回
"""