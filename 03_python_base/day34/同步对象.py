import threading
import time

class Boss(threading.Thread):

    def __init__(self, event):
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        print("Boss: 今晚加班到 22：00")
        print("event flag = {}".format(self.event.is_set()))
        self.event.set()
        time.sleep(5)

        print("Boss: 22:00 到了，可以下班")
        print("event flag = {}".format(self.event.is_set()))
        self.event.set()

class Worker(threading.Thread):

    def __init__(self, event):
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        self.event.wait()  # flag 默认 False ，等待直到有人调用 set()
        print("{} Worker: 又加班".format(threading.currentThread().name))
        time.sleep(1)  # 休眠1s 再 clear 其他线程才有机会执行完 wait()
        self.event.clear()
        # self.event.wait(1)  # 只等待1s ,老板没发话，下班
        self.event.wait()
        print("{} Worker: 下班啦".format(threading.currentThread().name))

if __name__ == '__main__':
    tl = []
    event = threading.Event()

    for i in range(3):
        t = Worker(event)
        t.start()
        tl.append(t)

    boss = Boss(event)
    boss.start()
    tl.append(boss)

    for t in tl:
        t.join()
    print("执行完成")

"""
结果：
    Boss: 今晚加班到 22：00
    event flag = False
    Thread-1 Worker: 又加班
    Thread-2 Worker: 又加班
    Thread-3 Worker: 又加班
    Boss: 22:00 到了，可以下班
    event flag = False
    Thread-3 Worker: 下班啦
    Thread-2 Worker: 下班啦
    Thread-1 Worker: 下班啦
    执行完成
"""