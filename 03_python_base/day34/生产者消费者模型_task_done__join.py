import threading, time, queue, random

q = queue.Queue()

def Producer(name, q1):
    while 1:
        q1.join()
        data = q1.get()
        time.sleep(0.01)
        print("%s 开始制作 %s 个包子" % (name, data))
        time.sleep(1)

        q1.put(data)
        q1.task_done()
        print("%s 制作完 %s 个包子" % (name, data))

def Consumer(name, q1):
    count = 0
    while count < 3:
        time.sleep(random.randrange(4))
        q1.put(name + str(count))
        q1.task_done()
        print('\033[32;1m 消费者[ %s ]预定了 %s baozi...\033[0m' % (name, count))

        q1.join()
        date = q1.get()
        time.sleep(0.01)
        print('\033[32;1m 消费者[ %s ]拿到了 %s baozi...\033[0m' % (name, date))
        count += 1

if __name__ == '__main__':
    p1 = threading.Thread(target=Producer, args=('A君', q,))
    c1 = threading.Thread(target=Consumer, args=('B君', q,))
    c2 = threading.Thread(target=Consumer, args=('C君', q,))
    p1.start()
    c1.start()
    c2.start()
