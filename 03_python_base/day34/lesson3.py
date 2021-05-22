# import queue
# import time
# import threading
#
# def func_remove(l):
#     while l:
#         el = l[-1]
#         print("el = ", el)
#         time.sleep(1)
#         l.remove(el)
#
# l = [1, 2, 3, 4, 5]
# t1 = threading.Thread(target= func_remove, args=(l,))
# t2 = threading.Thread(target= func_remove, args=(l,))
#
# if __name__ == '__main__':
#     t1.start()
#     t2.start()
#
# """
# 结果：其中一个线程在删除数据时，找不到 5 报错
#     el =  5
#     el =  5
#     Exception in thread Thread-1:
#     Traceback (most recent call last):
#       File "E:\0000_Python_3.7.3\lib\threading.py", line 917, in _bootstrap_inner
#         self.run()
#       File "E:\0000_Python_3.7.3\lib\threading.py", line 865, in run
#         self._target(*self._args, **self._kwargs)
#       File "E:/0000_Python/repositories/python_base/python_base/03_python_base/day34/lesson3.py", line 10, in func_remove
#         l.remove(el)
#     ValueError: list.remove(x): x not in list
#
#     el =  4
#     el =  3
#     el =  2
#     el =  1
# """
# ==============================================

import queue  # 线程队列
q = queue.Queue(3)  # 默认 maxsize = 0 ， f maxsize is <= 0, the queue size is infinite.
q.put(11)
q.put("12")
q.put({"a": "11"})
print("一般队列 queue：")
print("queue.empty(): {}".format(q.empty()))
print("queue.qsize(): {}".format(q.qsize()))
print("queue.full(): {}".format(q.full()))
print("queue.full: {}".format(q.full))
while not q.empty():
    data = q.get()
    print("data = {}, type is {}".format(data, type(data)))

# # 其他队列
# import queue  # 线程队列
# q1 = queue.LifoQueue()  # 默认 maxsize = 0 ， f maxsize is <= 0, the queue size is infinite.
# q1.put(11)
# q1.put("12")
# q1.put({"a": "11"})
# print("先进后出队列 LifoQueue：")
# while not q1.empty():
#     data = q1.get()
#     print("data = {}, type is {}".format(data, type(data)))
#
# import queue  # 线程队列
# q2 = queue.PriorityQueue() # 设置的值越小，越优先
# q2.put([2, 11])
# q2.put([4, "12"])
# q2.put([3, {"a": "11"}])
# print("优先级队列 PriorityQueue：")
# while not q2.empty():
#     data = q2.get()
#     print("data = {}, type is {}".format(data, type(data)))
#
# """
# 结果：
#     一般队列 queue：
#         data = 11, type is <class 'int'>
#         data = 12, type is <class 'str'>
#         data = {'a': '11'}, type is <class 'dict'>
#     先进后出队列 LifoQueue：
#         data = {'a': '11'}, type is <class 'dict'>
#         data = 12, type is <class 'str'>
#         data = 11, type is <class 'int'>
#     优先级队列 PriorityQueue：
#         data = [2, 11], type is <class 'list'>
#         data = [3, {'a': '11'}], type is <class 'list'>
#         data = [4, '12'], type is <class 'list'>
# """


