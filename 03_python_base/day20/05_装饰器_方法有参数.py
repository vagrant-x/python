import time


def timer(func):
    """
        *args：将被修饰方法传入的非关键字参数打包为元组 args
        **kwargs: 将被修饰方法传入的关键字参数打包为字典 kwargs
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)  # *args 拆解元组，按顺序传给被修饰函数； **kwargs：拆解字典
        stop_time = time.time()
        print("运行时间： %s" % (stop_time - start_time))
        return res
    return wrapper


@timer  # 给test 方法添加计算执行时间的装饰器
def test(name, age):
    time.sleep(3)
    print("name = {}, age = {}".format(name, age))
    return "test return ok"


# 调用被装饰器装饰的方法
print(test("xu", 100))  # 执行的是 wrapper
# 结果：
#     name = xu, age = 100
#     运行时间： 3.000420331954956
#     test return ok
