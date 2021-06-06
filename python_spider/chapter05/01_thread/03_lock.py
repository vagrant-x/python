# import threading
#
# g_value = 0
#
# def add():
#     global g_value
#     for i in range(1000000):
#         g_value += 1
#     print("value = {}".format(g_value))
#
# if __name__ == '__main__':
#     for i in range(2):
#         t = threading.Thread(target=add)
#         t.start()


import threading

g_value = 0
g_lock = threading.Lock()

def add():
    global g_value
    g_lock.acquire()
    for i in range(1000000):
        g_value += 1
    g_lock.release()
    print("value = {}".format(g_value))

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=add)
        t.start()
