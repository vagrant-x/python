from bs4 import BeautifulSoup

html = """
<html>
    <head><title>The Dormouse's story</title></head>
    <body>
        <div class="div_class">
            <p class="story" id="pid1" >python</p>
            <p class="story">广州</p>
            <p class="story2">python研发工程师</p>
            <p id="p1">
            <!-- 这是一个注释 -->
            </p>
            <p id="p2"><!-- 这是一个注释 --></p>
        </div>
    </body>
</html>
"""
soup = BeautifulSoup(html, "lxml")

# Tag
p = soup.select("p")[0]
print(type(p))  # <class 'bs4.element.Tag'>

# NavigableString
p = soup.select("p")[0]
print(type(p.string))  # <class 'bs4.element.NavigableString'>

# BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup.name)  # [document]

# Comment
p1 = soup.select("p#p2")[0]
print(p1.string)  #  这是一个注释
print(type(p1.string))  # <class 'bs4.element.Comment'>

# contents
p1 = soup.select("p#p1")[0]
print(p1.string)  # None
print(p1.contents)  # ['\n', ' 这是一个注释 ', '\n']

print("===============================")
div = soup.find("div")
# div.contents 返回所有子节点列表
for p in div.contents:
    print(p)

print("===============================")
div = soup.find("div")
# div.contents 返回所有子节点的生成器
for p in div.children:
    print(p)