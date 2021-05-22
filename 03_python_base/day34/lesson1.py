import threading
import time

def add():
    sum1 = 0
    for i in  range(50000000):
        sum1 += i
    print('sum1 = {}'.format(sum1))

def mul():
    sum2 = 1
    for i in range(1, 100000):
        sum2 *= i
    print('sum2 = {}'.format(sum2))

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=mul)
l = [t1, t2]

if __name__ == '__main__':
    print("---->start-----")
    start_time = time.time()

    # 通过线程并发执行（单位：s）  16.29,   14.86,   15.38
    # for t in l:
    #     t.start()
    # for t in l:
    #     t.join()

    # 通过主线程串行执行（单位：s）  14.37, 15.05, 14.88
    add()
    mul()

    print("-----> 执行时间： {}".format(time.time() - start_time))

"""
并发 和 并行
并发：是指系统具有处理多个任务（动作）的能力
并行：是指系统具有 同时 处理多个任务（动作）的能力
并行是并发的一个子集

下面的代码，通过线程并发和单线程串行执行3次的时间如下：
通过线程并发执行（单位：s）  16.29,   14.86,   15.38
通过主线程串行执行（单位：s）  14.37, 15.05, 14.88
问题： 多核没有利用上！
GIL 全局解释锁
    因为有GIL, 所以一个进程内，同一时刻，只有一个线程被CPU执行
    
任务：IO密集型、 计算密集型
对于io密集型的任务：python多线程有利于提高效率，可以采用 多进程+协程
对于计算密集型任务：python多线程就不推荐了， python就不适用了

"""
