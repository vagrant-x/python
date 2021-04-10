import time


def timer(func):
    def wrapper():
        start_time = time.time()
        res = func()  # 执行被装饰方法
        stop_time = time.time()
        print("运行时间： %s" % (stop_time - start_time))
        return res  # 接受正在调用的方法的返回值，并返回
    return wrapper


@timer
def test():
    time.sleep(3)
    print("test sleep 3s")
    return "test return ok"


print(test())  # 执行的是 wrapper
# 结果：
#     test sleep 3s
#     运行时间： 3.0002923011779785
#     test return ok