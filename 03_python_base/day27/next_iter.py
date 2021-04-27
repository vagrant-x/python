"""
__next__ 和 __iter__

    1、迭代器协议是指：对象必须提供一个next 方法，执行该方法要么返回迭代中的下一项，要么引起一个 StopIteration，以终止迭代（只能往后不能往前退）
    2、可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个 __iter__ 方法）
    3、协议是一种约定，可迭代对象实现了迭代器协议，Python的内部工具类（如for, sum, min, max函数等）使用迭代器协议访问对象
"""
class Iter:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        print("=======》 调用 __iter__")
        return self

    def __next__(self):
        print("===》 调用 __next__")
        if self.n > 10:
            raise StopIteration("n > 10")
        else:
            self.n += 1
            return self.n

# for 先调用 __iter__ 得到 iter 的迭代器对象（这里是本身），然后调用迭代器对象的 __next__ 进行迭代
iter = Iter(8)
l = [i for i in iter]
print(l)
# 结果：
#     ===》 调用 __iter__
#     ===》 调用 __next__
#     ===》 调用 __next__
#     ===》 调用 __next__
#     ===》 调用 __next__
#     [9, 10, 11]


# 实现斐波那契数列
class Fibonacci:

    def __init__(self):
        self._a = 0
        self._b = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._a == 0:
            self._a = 1
            return self._a
        if self._b == 0:
            self._b = 1
            return self._b
        self._a, self._b = self._b, self._a + self._b
        return self._b

l = []
fb = Fibonacci()
for i in range(6):
    l.append(next(fb))
print(l)  # [1, 1, 2, 3, 5, 8]