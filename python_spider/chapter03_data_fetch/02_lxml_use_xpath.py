# 1、获取所有div 并且属性class='recruit-list' 的 标签
# 2、获取第 2 个div 标签
# 3、获取所有class 等于 recruit-title 的标签
# 4、获取所有a 标签的href 属性
# 5、获取所有的职位信息（纯文本）

from lxml import etree

parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("tencent.html", parser=parser)
print(etree.tostring(html, encoding="utf-8").decode("utf-8"))


# 1、获取所有div 并且属性class='recruit-list' 的 标签
# xpath 返回的是一个列表
divs = html.xpath("//div[@class='recruit-list']")
for div in divs:
    print(etree.tostring(div, encoding="utf-8").decode("utf-8"))

# 2、获取第 2 个div 标签
div_2 = html.xpath("//div[@class='recruit-list' and position() = 2]")[0]
print(etree.tostring(div_2, encoding="utf-8").decode("utf-8"))

# 3、获取所有class 等于 recruit-title 的标签
h4s = html.xpath("//h4[@class='recruit-title']")
for h4 in h4s:
    print(etree.tostring(h4, encoding="utf-8").decode("utf-8"))

# 4、获取所有a 标签的href 属性
hrefs = html.xpath("//a[@href]")
for href in hrefs:
    print(etree.tostring(href, encoding="utf-8").decode("utf-8"))

# 5、获取所有的职位信息（纯文本）
divs = html.xpath("//div[@class='recruit-list']")
positions = []
for div in divs:
    title = html.xpath("//div[@class='recruit-list']//h4/text()")[0]
    address = html.xpath("//div[@class='recruit-list']/a/p[position()=1]/span[position()=2]")[0]
    data = html.xpath("//div[@class='recruit-list']/a/p[position()=1]/span[position()=4]")[0]
    detail = html.xpath("//div[@class='recruit-list']/a/p[position()=2]/text()")[0]
    position = {
        "title": title,
        "address": address,
        "data": data,
        "detail": detail
    }
    positions.append(position)
print(positions)

"""
总结：lxml 结合 xpath 注意事项：
1、使用 xpath 语法，应该使用 Element.xpath 方法来执行 xpath 的选择。示例代码如下：
    divs = html.xpath("//div[@class='recruit-list']")
    xpath 函数返回的永远是一个列表
    
2、获取某个标签的属性：
    hrefs = html.xpath("//a[@href]")
    # 获得 a 标签的 href 属性对应的值
    
3、获取文本，是通过 xpath 中的 text() 函数， 示例代码如下：
    address = tr.xpath("./td[4]/text()")[0]

4、如果想要某个标签下，再执行 xpath 函数， 获得这个标签下的子孙元素，
    应该在斜杆之前加一个点，代表是在当前元素下获取。示例代码如下：
    address = tr.xpath("./td[4]/text()")[0]
"""