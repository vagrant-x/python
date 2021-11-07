# 1、获取所有div 并且属性class='recruit-list' 的 标签
# 2、获取第 2 个div 标签
# 3、获取所有class 等于 recruit-title 的标签
# 4、获取所有a 标签的href 属性
# 5、获取所有的职位信息（纯文本）

from lxml import etree

parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("tencent.html", parser=parser)
# print(etree.tostring(html, encoding="utf-8").decode("utf-8"))
#
#
# # 1、获取所有div 并且属性class='recruit-list' 的 标签
# # xpath 返回的是一个列表
# divs = html.xpath("//div[@class='recruit-list']")
# for div in divs:
#     print(etree.tostring(div, encoding="utf-8").decode("utf-8"))
#
# # 2、获取第 2 个div 标签
# div_2 = html.xpath("//div[@class='recruit-list' and position() = 2]")[0]
# print(etree.tostring(div_2, encoding="utf-8").decode("utf-8"))
#
# # 3、获取所有class 等于 recruit-title 的标签
# h4s = html.xpath("//h4[@class='recruit-title']")
# for h4 in h4s:
#     print(etree.tostring(h4, encoding="utf-8").decode("utf-8"))
#
# # 4、获取所有a 标签的href 属性
# hrefs = html.xpath("//a[@href]")
# for href in hrefs:
#     print(etree.tostring(href, encoding="utf-8").decode("utf-8"))
#
# # 5、获取所有的职位信息（纯文本）
# divs = html.xpath("//div[@class='recruit-list']")
# positions = []
# for div in divs:
#     title = html.xpath("//div[@class='recruit-list']//h4/text()")[0]
#     address = html.xpath("//div[@class='recruit-list']/a/p[position()=1]/span[position()=2]")[0]
#     data = html.xpath("//div[@class='recruit-list']/a/p[position()=1]/span[position()=4]")[0]
#     detail = html.xpath("//div[@class='recruit-list']/a/p[position()=2]/text()")[0]
#     position = {
#         "title": title,
#         "address": address,
#         "data": data,
#         "detail": detail
#     }
#     positions.append(position)
# print(positions)

print("========================================================================")
"""
<div id="test_div" class="33370-jiagoushi0">测试id</div>
<div id="test_div1" class="33371-jiagoushi1">测试id1<div>->内部div内容</div></div>
<div id="test_div2" class="33372-jiagoushi2">测试id2</div>
"""
# 使用索引定位元素 :[1]
data = html.xpath("(//h4)[1]/text()")[0]  # 查询全局所有h4 标签中的第一个的text
print(data)

# 元素属性类型：@id 、@name、@type、@class、@tittle
data = html.xpath("//div[@id='test_div']/@id")[0]  # # 通过id 属性查询id=test_div 的标签，获取第一个的id
print(data)

# 部分属性值匹配

# starts-with
data = html.xpath("//div[starts-with(@class, '33370')]/text()")  # 查找class 开头是33370 的div 里面所有的文本
print("starts-with: {}".format(data))  # start-with: ['测试id']

# contains
data = html.xpath("//div[contains(@class, 'shi0')]/text()")  # 查找class 包含shi0 的div 里面所有的文本
print("contains: {}".format(data))  # contains: ['测试id']

# string()
data = html.xpath("string(//div[starts-with(@class, '33371')])")
print(data)  # 测试id

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