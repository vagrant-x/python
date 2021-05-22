import threading
import time

num = 10  # 定义一个全局变量
l = []
lock = threading.Lock()

def sub():
    global num  # 每个进程都获取这个全局变量
    # ----------》 执行结果都为 0
    # num -= 1

    # ----------》 执行结果: 9
    # tmp = num
    # time.sleep(0.001)
    # num = tmp -1

    # ----------》 执行结果: 0
    print(threading.currentThread().getName())
    lock.acquire()
    print("lock ---> {}".format(threading.currentThread().getName()))
    tmp = num
    time.sleep(0.001)
    num = tmp -1  # 对公共变量 -1
    lock.release()

for i in range(10):  # 创建100个线程执行 sub 方法
    t = threading.Thread(target=sub, name="thread-num-{}".format(i))
    t.start()
    l.append(t)

for t in l:
    t.join()  # 等待所有线程执行完毕

print("num = {}".format(num))

"""
数据安全，同步问题
"""