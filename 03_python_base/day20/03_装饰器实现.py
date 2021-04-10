"""
装饰器：本质就是函数，功能是为其他函数添加附加功能

原则：
    1、不修改被修改函数的源代码
    2、不修改被修饰函数的调用方式

装饰器 = 高阶函数 + 函数嵌套 + 闭包

"""



import time

def timer(func):  # 实现一个计算函数执行时间的函数作为装饰器，用来计算被装饰函数的执行时间并打印
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间： %s" % (stop_time - start_time))
    return wrapper

# def test():  # 不使用装饰器的同等实现
#     time.sleep(3)
#     print("test sleep 3s")
#
# test = timer(test)  # 返回的是 wrapper 的地址
# test()  # 执行的是 wrapper


@timer
def test():  # 装饰器的实现
    time.sleep(3)
    print("test sleep 3s")

test()  # 执行的是 wrapper
# 结果：
#     test sleep 3s
#     运行时间： 3.000915050506592