import time, queue

def consumer(name):
    print("---> 准备开始吃包子。。。")
    while True:
        new_baozi = yield
        print("{} 吃了 {} 个包子".format(name, new_baozi))
        time.sleep(1)

def producer(consumer1, consumer2):
    r = consumer1.__next__()  # 先执行一次 next 走到 yields 处等待
    r = consumer2.__next__()

    n = 0
    while n < 10:
        time.sleep(1)
        print("\033[32;1m[producer]\033[0m is making baozi {} and {} [time: {}]".format(n,
                                                                                        n +1, time.ctime()))
        consumer1.send(n)
        consumer2.send(n+1)
        n += 2

if __name__ == '__main__':
    c1 = consumer("xu1")
    c2 = consumer("xu2")
    p = producer(c1, c2)


# ==============================================================
from greenlet import greenlet

def fun1(gr):
    print(12)
    gr.switch()
    print(34)
    gr.switch()

def fun2(gr):
    print(56)
    gr.switch()
    print(78)

gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()