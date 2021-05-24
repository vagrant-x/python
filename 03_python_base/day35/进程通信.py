# # 进程间通信：Queue
# import multiprocessing, time, queue
#
# def fun1(q):
#     time.sleep(1)
#     q.put("name:xu")
#     q.put("pwd:123")
#
# if __name__ == '__main__':
#     # process_q = queue.Queue()  # 这个是线程队列
#     process_q = multiprocessing.Queue()  # 进程队列
#     sub_p = multiprocessing.Process(target=fun1, args=(process_q,))
#     sub_p.start()
#     print("main--->:{}".format(process_q.get()))
#     print("main--->:{}".format(process_q.get()))
#
# """
# 结果：
#     main--->:name:xu
#     main--->:pwd:123
# """

# # 进程间通信：Pipe
# import multiprocessing, time
#
# def fun2(conn):
#     conn.send(["message from sub process"])
#     response = conn.recv()
#     print("sub--->{}".format(response))
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = multiprocessing.Pipe()
#     sub_p = multiprocessing.Process(target=fun2, args=(child_conn,))
#     sub_p.start()
#
#     data = parent_conn.recv()
#     print("main--->{}, type = {}".format(data, type(data)))
#     parent_conn.send("我的好儿子")
#
# """
# main--->['message from sub process'], type = <class 'list'>
# sub--->我的好儿子
# """

# 进程间通信：Manager
import multiprocessing, time

def fun3(d, l, i):
    d[i] = str(i)
    l.append(i)

if __name__ == '__main__':
    p_list = []
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(3))
        l.append("\\")
        print(l)
        for i in range(5):
            p = multiprocessing.Process(target=fun3,args=(d, l, i))
            p.start()
            p_list.append(p)
        for p in p_list:
            p.join()
        print(d)
        print(l)
"""
结果：
    [0, 1, 2, '\\']
    {4: '4', 1: '1', 0: '0', 3: '3', 2: '2'}
    [0, 1, 2, '\\', 4, 1, 0, 3, 2]
"""

