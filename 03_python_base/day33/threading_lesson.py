# # 直接调用
# import threading
# import time
#
# def sayHi(name):  # 定义需要在线程中运行的函数
#     print("[{}], hello {}".format(time.ctime(), name))
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayHi, args=("x1",))  # 生成线程实例
#     t2 = threading.Thread(target=sayHi, args=("x2",))
#     t1.start()  # 启动线程
#     t2.start()
#     # time.sleep(0.01)
#     print("main ending ...")
#
# """
# 结果（3秒后程序关闭）：
# [Fri May 21 19:38:50 2021], hello x1
# [Fri May 21 19:38:50 2021], hello x2
# main ending ...
#
# """


# 继承调用
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义线程需要执行的代码
        print("running on number: {}".format(self.num))
        time.sleep(self.num)
        print(threading.enumerate())

if __name__ == '__main__':
    t1 = MyThread(3)
    t2 = MyThread(5)
    t1.start()
    t2.start()
    print(threading.enumerate())
    time.sleep(0.01)
    print("main ending ...")

"""
结果（3秒后程序关闭）：
    running on number: n1
    running on number: n2
    main ending ...
"""
