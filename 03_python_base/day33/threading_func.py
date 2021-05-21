import threading
import time

def music():
    print("begin to listen     {}".format(time.ctime()))
    time.sleep(3)
    print("stop to listen      {}".format(time.ctime()))

def game():
    print("begin to play game  {}".format(time.ctime()))
    time.sleep(5)
    print("stop to play game   {}".format(time.ctime()))

if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)
    t1.start()
    t2.start()

    time.sleep(4)
    print("t1.isAlive = {}, t2.isAlive = {}".format(t1.isAlive(), t2.isAlive()))
    # 结果： t1.isAlive = False, t2.isAlive = True

    print("线程 t1 设置之前名字： {}".format(t1.getName()))
    t1.setName("my-Thread-t1")
    print("线程 t1 设置之后名字： {}".format(t1.getName()))
    # 结果
    #   线程 t1 设置之前名字： Thread-1
    #   线程 t1 设置之后名字： my-Thread-t1

    print(threading.currentThread())
    # 结果: <_MainThread(MainThread, started 15076)>

    print(threading.enumerate())
    # 结果： [<_MainThread(MainThread, started 15776)>, <Thread(my-Thread-t1, started 6664)>, <Thread(Thread-2, started 13352)>]

    print(threading.activeCount())
    # 结果：3

