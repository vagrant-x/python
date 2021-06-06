import threading
import time
import random

gMoney = 1000
gTotalTime = 10
gTime = 0
gCondition = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        while True:
            global gTime
            global gMoney
            money = random.randint(100,1000)
            gCondition.acquire()  # 获取锁
            if gTime >= gTotalTime:
                print("{}挣不动了 ".format(threading.currentThread()))
                gCondition.release()
                break
            gMoney += money
            print("{}挣了{}元，现在总共有{}元".format(threading.currentThread(), money, gMoney))
            gTime += 1
            gCondition.notify()  # 通知多少个等待的线程，默认1
            # gCondition.notify_all()  # 通知所有在等待的线程，重新竞争锁
            gCondition.release()  # 释放锁
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        while True:
            global gMoney
            money = random.randint(100, 1000)
            gCondition.acquire()  # 获取锁
            while money > gMoney:  # 获得锁，但是钱不够消费，继续等待
                if gTime >= gTotalTime and money > gMoney:
                    print("没人挣钱，钱不够，{} 走了".format(threading.currentThread()))
                    gCondition.release()
                    return  # 退出执行方法
                print("{}想消费{}元，现在只有{}元， 余额不足".format(threading.currentThread(), money, gMoney))
                gCondition.wait()  # 不断等待，直到获得锁并余额满足消费
            gMoney -= money
            print("{}消费{}元，现在剩余{}元".format(threading.currentThread(), money, gMoney))
            gCondition.release()
            time.sleep(0.5)


def main():
    for i in range(3):
        consumer = Consumer(name="消费者{}".format(i))
        consumer.start()
    for i in range(5):
        producer = Producer(name="生产者{}".format(i))
        producer.start()


if __name__ == '__main__':
    main()