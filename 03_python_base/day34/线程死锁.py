import threading
import time


class MyThread(threading.Thread):

    def __init__(self, lockA, lockB):
        threading.Thread.__init__(self)
        self.lockA = lockA
        self.lockB = lockB


    def run(self):
        self.actionA()
        time.sleep(0.01)
        self.actionB()

    def actionA(self):
        self.lockA.acquire()  # 获取 A 锁
        print(self.name, "getLock:A", time.ctime())
        time.sleep(2)

        self.lockB.acquire()  # 获取 B 锁
        print(self.name, "getLock:B", time.ctime())
        time.sleep(1)

        self.lockB.release()  # 释放 A 锁
        self.lockA.release()  # 释放 B 锁

    def actionB(self):
        self.lockB.acquire()
        print(self.name, "getLock:B", time.ctime())
        time.sleep(2)

        self.lockA.acquire()
        print(self.name, "getLock:A", time.ctime())
        time.sleep(1)

        self.lockA.release()
        self.lockB.release()

if __name__ == '__main__':
    A = threading.Lock()
    B = threading.Lock()
    tl = []
    for i in range(3):
        t = MyThread(A, B)
        t.start()
        tl.append(t)
    for t in tl:
        t.join()
    print("main thread ending ...")

"""
结果：
    Thread-1 getLock:A Sat May 22 09:36:46 2021
    Thread-1 getLock:B Sat May 22 09:36:48 2021
    Thread-2 getLock:A Sat May 22 09:36:49 2021
    Thread-1 getLock:B Sat May 22 09:36:49 2021
"""