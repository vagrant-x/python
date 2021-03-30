print("test reduce")
"""
reduce
    通过两个参数的函数，从左到右累加的应用于序列的项，将序列缩减为当个值。
    例如，reduce（lambda x，y:x+y，[1，2，3，4，5]）计算 ((((1+2)+3)+4)+5). 

# 在python2 中，reduce不需要引入即可直接使用
E:\0000_Python_2.7>python
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> reduce(lambda x, y: x + y, [1,2,3,4])
10
>>>

# 在python3 中 需要通过 from functools import reduce 导入
E:\0000_Python\repositories\python_base\python_base>python3
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> reduce(lambda x, y: x + y, [1,2,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reduce' is not defined
>>> from functools import reduce
>>> reduce(lambda x, y: x + y, [1,2,3,4])
10
>>>


"""

# 通过功能单一的函数实现
num1 = [1, 2, 3, 4]
def reduce_test(array):
    sum = 0
    for i in array:
        sum += i
    return sum
print(reduce_test(num1))  # 10


# 通过功能教强大的函数进行实现
num1 = [1, 2, 3, 4]
def reduce_test(func, array):
    res = array.pop()
    for i in array:
        res = func(res, i)
    return res
print(reduce_test(lambda x,y: x + y, num1))  # 10


# 通过内置函数 reduce实现
from functools import reduce
num1 = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, num1))  # 10

num1 = ["a1", "a2", "a3"]
print(reduce(lambda x, y: x + y, num1))  # a1a2a3

num1 = [(), (3, 4), (1, 2)]
print(reduce(lambda x, y: x + y, num1))  # (3, 4, 1, 2)