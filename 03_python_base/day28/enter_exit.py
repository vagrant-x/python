"""
__enter__ 和 __exit__
    上下文管理协议：即with 语句， 为了让一个对象兼容with 语句，必须在这个对象的类中声明 __enter__ 和 __ exit__ 方法

    1、 with obj ---> 触发 obj.__enter__()， 拿到返回值
    2、as f --> f = 返回值
    3、with obj as f ---> f = obj.__enter__()
    4、执行代码块
        4.1、没有异常情况，整个代码块运行完毕后触发 __exit__ , 他的三个参数都是 None
        4.2、有异常，从异常出现的位置直接触发 __exit__
            a、如果__exit__的返回值为True，代表异常被处理
            b、如果__exit__的返回值不为True, 代表异常会继续抛出
            c、exit的运行完毕代表了整个with语句的执行完毕

    with用途：
        1、使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无效手动干预
        2、在需要管理一些资源比如文件、网络连接、锁的编程环境中，可以在 __exit__ 中定制自动释放资源的机制，而无效再关心资源的回收释放

"""
class FileA:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("---> __enter__ ")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        当with ...  as...代码块没有异常时，这三个参数为None;
        当with ...  as...代码块有异常时，这三个参数分别有对应的值
        :param exc_type: 异常类型
        :param exc_val: 异常的值
        :param exc_tb: 异常堆栈信息
        :return:
            返回值True,会捕获 with ...  as...代码块的异常，并且结束代码块运行，但是代码块之外的代码会继续运行
            若，没有返回值、或者返回值不为True,一遇到with ...  as...代码块的异常，会立即抛出异常，结束所有代码的运行，包括代码块之外的代码
        """
        print("---> __exit__ ")
        print("------>exc_type: {}".format(exc_type))
        print("------>exc_val: {}".format(exc_val))
        print("------>exc_tb: {}".format(exc_tb))
        return True

with FileA("a.txt") as f:
    print(f.filename)
    print(1/0)
    print("理论上这句不会打印")
print("程序执行完。。。")
# 结果：
#     ---> __enter__
#     a.txt
#     ---> __exit__
#     ------>exc_type: <class 'ZeroDivisionError'>
#     ------>exc_val: division by zero
#     ------>exc_tb: <traceback object at 0x7f7bf18f5ac8>
#     程序执行完。。。