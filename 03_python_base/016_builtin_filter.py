print("test filter")
"""
filter
    返回一个迭代器，迭代经过函数计算返回为True的项
"""

# 获得元素能被2整除的列表, 函数方法单一
num1 = [1, 2, 3, 4, 5, 6]
def filter_test(array):
    ret = []
    for i in array:
        if i % 2 == 0:
            ret.append(i)
    return ret
print(filter_test(num1))  # [2, 4, 6]

# 对列表中的元素进行未知操作，自己实现内部逻辑
num1 = [1, 2, 3, 4, 5, 6]
def filter_test(func, array):
    ret = []
    for i in array:
        if func(i):
            ret.append(i)
    return ret
print(filter_test(lambda x: True if x % 2 == 0 else False, num1))  # [2, 4, 6]

# 通过内置函数 filter 处理
num1 = [1, 2, 3, 4, 5, 6]
f_res = filter(lambda x: True if x % 2 == 0 else False, num1)
print(f_res)  # <filter object at 0x0000025F491B8B00>
print(list(f_res))  # [2, 4, 6]


num1 = [0, 1, 2, 3, 4, 5, 6, "", {}, False]
f_res = filter(None, num1)
print(num1)
