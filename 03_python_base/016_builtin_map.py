print("test map")
"""
map
    返回一个可迭代对象，这个可迭代对象通过function计算每一个元素产生
"""

# 对列表中的数字取平方，方法单一
num1 = [1, 2, 3, 4, 5]
def map_test(array):
    ret = []
    for i in num1:
        ret.append(i ** 2)
    return ret
print(map_test(num1))  # [1, 4, 9, 16, 25]

# 对列表中的元素进行未知操作， 自己实现内部逻辑
num1 = [1, 2, 3, 4, 5]
def map_test(func, array):
    ret = []
    for i in array:
        ret.append(func(i))
    return ret
print(map_test(lambda x: "A" + str(x), num1))  # ['A1', 'A2', 'A3', 'A4', 'A5']

# 通过内置函数map处理
num1 = [1, 2, 3, 4, 5]
ite = map(lambda x:"A" + str(x), num1)
print(ite)  # <map object at 0x00000155434B8AC8>
print(list(ite))  # ['A1', 'A2', 'A3', 'A4', 'A5']
