from bs4 import BeautifulSoup

html = """
<html>
    <head><title>The Dormouse's story</title></head>
    <body>
        <div class="div1_class">
            <p class="story" id="pid1" >python</p>
            <p class="story">广州</p>
            <p class="story2">python研发工程师</p>
        </div>
        <div>
            <p class="even">java</p>
            <p class="even">深圳</p>
            <p class="even">java研发工程师</p>
            <a id="test" class="test" herf="http://www.baidu.com">http://www.baidu.com</a>
        </div>
    </body>
</html>
"""
# 这里使用 lxml， 需要先安装 lxml模块
soup = BeautifulSoup(html, "lxml")
print(soup.prettify())