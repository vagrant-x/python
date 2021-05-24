import multiprocessing, time, os

def Foo(num):
    time.sleep(1)
    print("Foo ---> sub_{}, pid = {}".format(num, os.getpid()))
    return "sub_{}".format(num)  # 将进程执行结果返回给 回调函数

def Bar(arg):  # 进程回调函数： arg 接收进程执行方法返回的结果
    print("Bar +++> arg = {}, pid = {}".format(arg, os.getpid()))

if __name__ == '__main__':
    print("main ###> pid = {}".format(os.getpid()))
    pool = multiprocessing.Pool(3)  # 创建一个进程池，同时能并发执行 3 个进程

    for i in range(10):
        # pool.apply(func=Foo, args=(i, ))
        # pool.apply_async(func=Foo, args=(i,))
        # 回调函数：  就是某个动作或者函数执行成功后再去执行的函数
        pool.apply_async(func=Foo, args=(i,), callback=Bar)

    pool.close()
    pool.join()         # close() 与 join() 调用顺序是固定的