import multiprocessing, time

def fun1(l, num):
    # time.sleep(1)
    l.acquire()  # 获取锁
    print("进程同步，执行第 {} 号进程".format(num))
    l.release()  # 释放锁

if __name__ == '__main__':
    lock = multiprocessing.Lock()

    for i in range(5):
        p = multiprocessing.Process(target=fun1, args=(lock, i,))
        p.start()
