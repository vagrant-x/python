import json

# 将 python 对象转换成 json 字符串
persons = [
    {
        "name": "xu1",
        "age": 11,
        "height": 171
    },
    {
        "name": "xu2",
        "age": 12,
        "height": 172
    },
]
persons_str = json.dumps(persons)
print(type(persons_str))  # <class 'str'>
print(persons_str)  # [{"name": "xu1", "age": 11, "height": 171}, {"name": "xu2", "age": 12, "height": 172}]



# 将 python 对象转换成 json 字符串并保存到文件
persons = [
    {
        "name": "xu1_许三多",
        "age": 11,
        "height": 171
    },
    {
        "name": "xu2_许三多",
        "age": 12,
        "height": 172
    },
]
# 方法一：将字符串写入文件
# persons_str = json.dumps(persons)
# with open("persons.json", "w", encoding="utf-8") as fp:
#     fp.write(persons_str)

# 方法一：直接通过 json.dump 写入对象
with open("persons.json", "w", encoding="utf-8") as fp:
    json.dump(persons, fp, ensure_ascii=False)


# json 无法序列化自定义对象
class Person(object):
    country="china"
a = {
    "person": Person()
}
json.dumps(a)
"""
报错：
    TypeError: Object of type Person is not JSON serializable
"""

#=========================================================================

import json

persons_str = '[{"name": "xu1", "age": 11, "height": 171}, {"name": "xu2", "age": 12, "height": 172}]'
persons = json.loads(persons_str)
print(type(persons))
for p in persons:
    print(p)
"""
结果：
    <class 'list'>
    {'name': 'xu1', 'age': 11, 'height': 171}
    {'name': 'xu2', 'age': 12, 'height': 172}
"""


with open("persons.json", "r", encoding="utf-8") as fp:
    persons = json.load(fp)
    print(type(persons))
    for p in persons:
        print(p)
"""
结果：
    <class 'list'>
    {'name': 'xu1_许三多', 'age': 11, 'height': 171}
    {'name': 'xu2_许三多', 'age': 12, 'height': 172}
"""