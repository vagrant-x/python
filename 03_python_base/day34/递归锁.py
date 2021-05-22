import threading
import time


class MyThread(threading.Thread):

    def __init__(self, r_lock):
        threading.Thread.__init__(self)
        self.r_lock = r_lock

    def run(self):
        self.actionA()
        time.sleep(0.01)
        self.actionB()

    def actionA(self):
        self.r_lock.acquire()  # counter = 1
        print(self.name, "getLock:A", time.ctime())
        time.sleep(2)

        self.r_lock.acquire()  # counter = 2
        print(self.name, "getLock:B", time.ctime())
        time.sleep(1)

        self.r_lock.release()  # counter = 1
        self.r_lock.release()  # counter = 0

    def actionB(self):
        self.r_lock.acquire()
        print(self.name, "getLock:B", time.ctime())
        time.sleep(2)

        self.r_lock.acquire()
        print(self.name, "getLock:A", time.ctime())
        time.sleep(1)

        self.r_lock.release()
        self.r_lock.release()

if __name__ == '__main__':
    r_lock = threading.RLock()
    tl = []
    for i in range(3):
        t = MyThread(r_lock)
        t.start()
        tl.append(t)
    for t in tl:
        t.join()
    print("main thread ending ...")

"""
结果(顺序不一定一样)：
    Thread-1 getLock:A Sat May 22 09:38:40 2021
    Thread-1 getLock:B Sat May 22 09:38:42 2021
    Thread-2 getLock:A Sat May 22 09:38:43 2021
    Thread-2 getLock:B Sat May 22 09:38:45 2021
    Thread-2 getLock:B Sat May 22 09:38:46 2021
    Thread-2 getLock:A Sat May 22 09:38:48 2021
    Thread-1 getLock:B Sat May 22 09:38:49 2021
    Thread-1 getLock:A Sat May 22 09:38:51 2021
    Thread-3 getLock:A Sat May 22 09:38:52 2021
    Thread-3 getLock:B Sat May 22 09:38:54 2021
    Thread-3 getLock:B Sat May 22 09:38:55 2021
    Thread-3 getLock:A Sat May 22 09:38:57 2021
    main thread ending ...
"""