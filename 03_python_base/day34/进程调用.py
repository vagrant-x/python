# # 方法一
import multiprocessing, time

def fun1(name):
    time.sleep(1)
    print("{} {}".format(time.ctime(), name))

if __name__ == '__main__':
    pl = []
    for i in range(3):
        process = multiprocessing.Process(target=fun1, args=("xu{}".format(i),))
        process.start()
        pl.append(process)
    for p in pl:
        process.join()
    print("--- ending ---")

"""
Sat May 22 16:37:15 2021 xu0
Sat May 22 16:37:15 2021 xu1
Sat May 22 16:37:15 2021 xu2
--- ending ---
"""

# # 继承调用
import multiprocessing, time

class MyProcess(multiprocessing.Process):
    def run(self):
        time.sleep(1)
        print("{} {}".format(time.ctime(), self.name))

if __name__ == '__main__':
    pl = []
    for i in range(3):
        process = MyProcess()
        process.start()
        pl.append(process)
    for p in pl:
        p.join()
    print("--- ending ---")

"""
Sat May 22 16:39:46 2021 MyProcess-1
Sat May 22 16:39:46 2021 MyProcess-2
Sat May 22 16:39:46 2021 MyProcess-3
--- ending ---
"""

import multiprocessing, os, time

def show_info(title):
    print("title:{}".format(title))
    print("parant process id: {}".format(os.getppid()))
    print("process id; {}".format(os.getpid()))

if __name__ == '__main__':
    show_info("-->main process")
    time.sleep(1)
    print("------------------------")
    p = multiprocessing.Process(target=show_info, args=("sub1", ))
    p.start()
    p.join()

"""
结果：当前在pycharm 里面执行，main进程的父进程是pycharm 执行的进程
    title:-->main process
    parant process id: 9276 
    process id; 3300
    ------------------------
    title:sub1
    parant process id: 3300
    process id; 11668
"""