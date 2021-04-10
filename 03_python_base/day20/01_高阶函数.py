"""
高阶函数定义：
    1、函数接收的参数是一个函数
    2、函数的返回值是一个函数名
    3、满足上述条件任意一个，都可以称为高阶函数

"""
# import time
# def foo():
#     time.sleep(3)
#     print("sleep 3s")
#
# def test(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print("函数的运行时间是： %s" % (stop_time - start_time))
#
# test(foo)

#条件：
# 不修改foo源码
# 不修改foo调用方式

import time
def foo():
    time.sleep(3)
    print("sleep 3s")

def timer(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("执行时间{}".format(stop_time - start_time))
    return func
foo = timer(foo)
foo()
# 结果： 多运行了一次
