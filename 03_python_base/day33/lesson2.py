# import threading
# import time
#
#
# def music():
#     print("begin to listen     {}".format(time.ctime()))
#     time.sleep(3)
#     print("stop to listen      {}".format(time.ctime()))
#
#
# def game():
#     print("begin to play game  {}".format(time.ctime()))
#     time.sleep(5)
#     print("stop to play game   {}".format(time.ctime()))
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=music)
#     t2 = threading.Thread(target=game)
#     t1.start()
#     t2.start()
#
#     # t1.join()
#     # t2.join()
#
#     t1.join(timeout=1)
#     # 如果设置 timeout 属性，表明在调用 join() 方法的地方（当前）等待，超过等待时间，调用 join() 处继续执行之后代码
#
#     time.sleep(0.01)  # 休眠0.01 避免输出到控制台打印到同一行
#     print("main ending ...     {}".format(time.ctime()))
#
# """
# #1 没有设置 join()
# begin to listen     Fri May 21 20:22:01 2021
# begin to play game  Fri May 21 20:22:01 2021
# main ending ...     Fri May 21 20:22:01 2021
# stop to listen      Fri May 21 20:22:04 2021
# stop to play game   Fri May 21 20:22:06 2021
#
# #2 设置
# t1.join()
# t2.join()
# 结果：
#     begin to listen    Fri May 21 20:14:26 2021
#     begin to play game Fri May 21 20:14:26 2021
#     stop to listen     Fri May 21 20:14:29 2021
#     stop to play game  Fri May 21 20:14:31 2021
#     main ending ...    Fri May 21 20:14:31 2021
#
# #3 只设置  t1.join(timeout=1)，主线程在等待1秒后，直接执行打印后续代码
# 结果：
#     begin to listen     Fri May 21 20:23:38 2021
#     begin to play game  Fri May 21 20:23:38 2021
#     main ending ...     Fri May 21 20:23:39 2021
#     stop to listen      Fri May 21 20:23:41 2021
#     stop to play game   Fri May 21 20:23:43 2021
# """


# ============================================================================

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

t1 = threading.Thread(target=music)
t2 = threading.Thread(target=game)

thread_list = [t1, t2]

if __name__ == '__main__':
    for t in thread_list:
    # -------------不同设置----------------
    #     t.setDaemon(True)
        if t is t2: t.setDaemon(True)
        t.start()
        # t.join()
    # t.join()  # 对列表最后一个执行 join() 方法
    # t1.join()
    # -------------------------------------
    time.sleep(0.01)  # 休眠0.01 避免输出到控制台打印到同一行
    print("main ending ...     {}".format(time.ctime()))

"""
# -------------不同设置----------------
    t.start()
# -------------------------------------
结果：
    begin to listen     Fri May 21 20:42:40 2021
    begin to play game  Fri May 21 20:42:40 2021
    main ending ...     Fri May 21 20:42:40 2021
    stop to listen      Fri May 21 20:42:43 2021
    stop to play game   Fri May 21 20:42:45 2021
    
    
# -------------不同设置----------------
    t.start()
    t.join()
# -------------------------------------
结果：启动一个线程，阻塞直到这个线程执行完，接着继续执行同样的操作
    begin to listen     Fri May 21 20:44:34 2021
    stop to listen      Fri May 21 20:44:37 2021
    begin to play game  Fri May 21 20:44:37 2021
    stop to play game   Fri May 21 20:44:42 2021
    main ending ...     Fri May 21 20:44:42 2021
    
    
# -------------不同设置----------------
    t.start()
t1.join()
# -------------------------------------
结果：for循环结束，所有线程启动，t1阻塞主线程，等到t1结束，才打印[main ending ...     Fri May 21 20:47:30 2021]
    begin to listen     Fri May 21 20:47:27 2021
    begin to play game  Fri May 21 20:47:27 2021
    stop to listen      Fri May 21 20:47:30 2021
    main ending ...     Fri May 21 20:47:30 2021
    stop to play game   Fri May 21 20:47:32 2021
"""



"""
setDeamon 方法的测试

将线程声明为守护线程，必须在start() 方法调用之前设置， 如果不设置为守护线程程序会被无限挂起。

当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，
那么当主线程完成想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。

但是有时候我们需要的是只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法

# -------------不同设置----------------
    t.setDaemon(True)
    t.start()
# -------------------------------------
结果：t1,t2 都设置为守护线程，主线程结束，两个守护线程也跟着结束
    begin to listen     Fri May 21 21:22:29 2021
    begin to play game  Fri May 21 21:22:29 2021
    main ending ...     Fri May 21 21:22:29 2021
    
    
# -------------不同设置----------------
    if t is t1: t.setDaemon(True)
    t.start()
# -------------------------------------
结果：设置t1为守护线程，但是由于t2执行时间长于t1,所以t1能正常执行完毕
    begin to listen     Fri May 21 21:24:55 2021
    begin to play game  Fri May 21 21:24:55 2021
    main ending ...     Fri May 21 21:24:55 2021
    stop to listen      Fri May 21 21:24:58 2021
    stop to play game   Fri May 21 21:25:00 2021
    
    
# -------------不同设置----------------
    if t is t2: t.setDaemon(True)
    t.start()
# -------------------------------------
结果：设置t2为守护线程，t1不设置，因为t1的执行时间比t2短，执行完t1,主线程执行结束，t2也跟着结束。
    begin to listen     Fri May 21 21:26:34 2021
    begin to play game  Fri May 21 21:26:34 2021
    main ending ...     Fri May 21 21:26:34 2021
    stop to listen      Fri May 21 21:26:37 2021
"""



