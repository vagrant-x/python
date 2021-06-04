# 写入 csv 文件

# import csv
#
# headers = ["name", "age", "height"]
# datas = [
#     ("许1", 89, 150),
#     ("许2", 64, 160),
#     ("许3", 60, 170),
# ]
# with open("persons.csv", "w", encoding="utf-8", newline="") as  fp:
#     writer = csv.writer(fp)  # 创建一个可写对象
#     writer.writerow(headers)  # 写入一行数据
#     writer.writerows(datas)  # 写入多行数据



# import csv
#
# headers = ["name", "age", "height"]
# datas = [
#     {"name":"许1", "age": 12, "height": 23},
#     {"name": "许2", "age": 22, "height": 123},
#     {"name": "许3", "age": 32, "height": 223},
# ]
# with open("persons2.csv", "w", encoding="utf-8", newline="") as fp:
#     writer = csv.DictWriter(fp, headers)  # 创建一个可写对象
#     # 注意：写如表头的时候，需要调用 writeheader 方法
#     writer.writeheader()
#     writer.writerow({"name":"许1", "age": 12, "height": 23})  # 写入一行数据
#     writer.writerows(datas)  # 写入多行数据


# 读取 csv 文件
import csv
with open("persons.csv", "r", encoding="utf8") as fp:
    reader = csv.reader(fp)
    print("返回的类型：{}".format(type(reader)))
    print("第一行内容：{}".format(next(reader)))
    for p in reader:
        print("name = {}, age = {}, height = {}".format(
            p[0], p[1], p[2]
        ))
"""
结果：
    返回的类型：<class '_csv.reader'>
    第一行内容：['name', 'age', 'height']
    name = 许1, age = 89, height = 150
    name = 许2, age = 64, height = 160
    name = 许3, age = 60, height = 170
"""

print("-------------------")

import csv
with open("persons2.csv", "r", encoding="utf8") as fp:
    # 使用 DictReader 创建 reader 对象，不会包含标题那行的数据
    # reader 是一个迭代器, 遍历时返回字典对象
    reader = csv.DictReader(fp)
    print(type(reader))
    for p in reader:
        print("name = {}, age = {}, height = {}".format(
            p["name"], p["age"], p["height"]
        ))
"""
结果：
    <class 'csv.DictReader'>
    name = 许1, age = 12, height = 23
    name = 许1, age = 12, height = 23
    name = 许2, age = 22, height = 123
    name = 许3, age = 32, height = 223
"""