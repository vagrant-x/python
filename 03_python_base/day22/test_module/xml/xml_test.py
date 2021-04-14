"""
xml 模块
    xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单

"""

# xml协议在各个语言里的都 是支持的，在python中可以用以下模块操作xml
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")  # 解析xml数据
root = tree.getroot()  # 获取根节点
print(root.tag)  # data

# 遍历xml文档
for child in root:
    print("tag = {} , attrib = {}".format(child.tag, child.attrib))  # 打印子节点标签和属性 ：tag = country , attrib = {'name': 'Liechtenstein'}
    for i in child:
        print("tag = {} , text = {}".format(i.tag, i.text)) # tag = rank , text = 2

# 只变量year 节点
for node in root.iter("year"):
    print("tag = {} , text = {}".format(node.tag, node.text))
# 结果：
# tag = year , text = 2008
# tag = year , text = 2011
# tag = year , text = 2011

# 修改
for node in root.iter("year"):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")
tree.write("data_bak.xml")

# 删除
for country in root.findall("country"):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write("data_bak2.xml")


#  ---------------------------
# 创建xml文档
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
age.text = "18"
sex = ET.SubElement(name, "sex")
sex.text = "man"

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("new_data.xml", encoding="utf-7", xml_declaration=True)

print("--------")
# 打印机生成的格式
ET.dump(new_xml)  # <namelist><name enrolled="yes"><age checked="no">18</age><sex>man</sex></name></namelist>
