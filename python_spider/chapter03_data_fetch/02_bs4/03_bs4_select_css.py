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
# 4、获取所有 a 标签的 herf 属性
# 5、获取所有的职位信息（纯文本）

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# 1、获取所有 p 标签
ps = soup.select("p")
# print(type(ps[0]))  # <class 'bs4.element.Tag'>
for p in ps:
    print(p)

# 2、获取第二个 p 标签
pList = soup.select("p")
print(type(pList))  # <class 'bs4.element.ResultSet'>
print(type(pList[0]))  # <class 'bs4.element.Tag'>
p2 = pList[1]
print(p2)  # <p class="story">广州</p>

# 3、获取所有 class 等于 even 的 p 标签
# plist = soup.select("p.even")
plist = soup.select("p[class='even']")
for p in plist:
    print(p)

# 4、获取所有 a 标签的 href 属性
aList = soup.select("a")
for a in aList:
    print(a["href"])  # http://www.baidu.com

# 5、获取所有的职位信息（纯文本）
# 可以使用 string、strings、stripped_strings、get_text 方法
divs = soup.select("div")
for div in divs:
    print(list(div.stripped_strings))
"""
['python', '广州', 'python研发工程师']
['java', '深圳', 'java研发工程师', 'http://www.baidu.com']
"""

"""
总结
    在 BeautifulSoup 中，要使用 css 选择器，那么应该使用 soup.select() 方法。应该传递一个 css 选择器的字符串给 select 方法。
"""