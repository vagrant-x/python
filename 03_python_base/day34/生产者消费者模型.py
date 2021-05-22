import threading, time, queue, random

q = queue.Queue()

def Producer(name, q1):
    count = 0
    while count < 10:
        print("making ......")
        time.sleep(random.randrange(3))
        q1.put(count)
        print('Producer %s has produced %s baozi..' % (name, count))
        count += 1

def Consumer(name, q1):
    count = 0
    while count < 10:
        time.sleep(random.randrange(4))
        if not q1.empty():
            data = q1.get()
            print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' % (name, data))
        else:
            print("------ 现在还没有包子 ------> {} 走了".format(name))
        count += 1

if __name__ == '__main__':
    p1 = threading.Thread(target=Producer, args=('A君', q,))
    c1 = threading.Thread(target=Consumer, args=('B君', q,))
    # c2 = threading.Thread(target=Consumer, args=('C君',))
    # c3 = threading.Thread(target=Consumer, args=('D君',))
    p1.start()
    c1.start()
    # c2.start()
    # c3.start()