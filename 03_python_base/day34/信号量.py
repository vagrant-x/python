import threading
import time

class MyThread(threading.Thread):

    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.semaphore = semaphore

    def run(self):
        acquire_res = self.semaphore.acquire()
        # acquire_res = self.semaphore.acquire(blocking=False)
        # acquire_res = self.semaphore.acquire(timeout=0.1)
        print("{} 执行： {}, acquire_res = {}".format(threading.currentThread().name,
                            time.ctime(), acquire_res))
        time.sleep(1)
        self.semaphore.release()

if __name__ == '__main__':
    semaphore = threading.Semaphore(2)

    # # 下面 没有调用 acquire() 之前调用 release() 抛出异常（否则导致计数器大于默认值）
    # semaphore = threading.BoundedSemaphore(2)
    # semaphore.release()

    for i in range(6):
        t = MyThread(semaphore)
        t.start()
    semaphore.release()
"""
acquire_res = self.semaphore.acquire()
结果：每间隔1秒，有两个线程获取到信号量，执行打印
    Thread-1 执行： Sat May 22 11:32:37 2021, acquire_res = True
    Thread-2 执行： Sat May 22 11:32:37 2021, acquire_res = True
    Thread-3 执行： Sat May 22 11:32:38 2021, acquire_res = True
    Thread-4 执行： Sat May 22 11:32:38 2021, acquire_res = True
    Thread-5 执行： Sat May 22 11:32:39 2021, acquire_res = True
    Thread-6 执行： Sat May 22 11:32:39 2021, acquire_res = True
    
acquire_res = self.semaphore.acquire(blocking=False)
结果：第1，2 个线程获取到信号量，其他没有获取到，不阻塞跳过, 返回 False
    Thread-1 执行： Sat May 22 11:33:12 2021, acquire_res = True
    Thread-2 执行： Sat May 22 11:33:12 2021, acquire_res = True
    Thread-3 执行： Sat May 22 11:33:12 2021, acquire_res = False
    Thread-4 执行： Sat May 22 11:33:12 2021, acquire_res = False
    Thread-5 执行： Sat May 22 11:33:12 2021, acquire_res = False
    Thread-6 执行： Sat May 22 11:33:12 2021, acquire_res = False
    
acquire_res = self.semaphore.acquire(timeout=0.1)
结果：第1，2 个线程获取到信号量，其他在设定等待时间内没有获取到， 返回 False
Thread-1 执行： Sat May 22 11:34:35 2021, acquire_res = True
Thread-2 执行： Sat May 22 11:34:35 2021, acquire_res = True
Thread-3 执行： Sat May 22 11:34:35 2021, acquire_res = False
Thread-4 执行： Sat May 22 11:34:35 2021, acquire_res = False
Thread-5 执行： Sat May 22 11:34:35 2021, acquire_res = False
Thread-6 执行： Sat May 22 11:34:35 2021, acquire_res = False
"""

"""
Semaphore [ˈseməfɔː(r)]
    semaphore = threading.Semaphore() 默认的值为1
    acquire(blocking=True, timeout=None)：请求一个信号量，内部计数器-1
            不设置参数: 如果计数器大于零，计数器-1并且立即返回；如果不为零，阻塞直到有其他线程调用 release
            blocking：  true 和没有设置参数一样
                        false 不阻塞线程，如果计数器0，返回 False
            timeout： 如果在设定超时 时间内没有请求成功，返回False   
    release()： 释放一个信号量，内部计数器+1
    
注意：调用 semaphore.release() 会给内部计数器+1，如果调用 release() 次数多于 acquire() 次数，
    那么内部计数器允许的最大值会大于设定的值
    
BoundedSemaphore(Semaphore)
    release(self)：当 调用 release() 次数多于 acquire() 次数时，会抛出
                    ValueError: Semaphore released too many times
                    
"""