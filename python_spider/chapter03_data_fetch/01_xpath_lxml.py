from lxml import etree

text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
"""

def parse_text():
    # 利用 etree.HTML 将字符串解析为 HTML 文档
    htmlElement = etree.HTML(text)
    # etree.tostring(htmlElement, encoding="utf-8") 将字符串序列化为HTML 文档
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

def parse_lagou_file():
    parser = etree.HTMLParser(encoding="utf-8")  # 获取html 解析器
    htmlElement = etree.parse("lagou.html", parser=parser)  # 默认是xml 解析器
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))


if __name__ == '__main__':
    parse_lagou_file()