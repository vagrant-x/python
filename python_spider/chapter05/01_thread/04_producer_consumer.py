import threading
import time
import random

gMoney = 1000
gTotalTime = 10
gTime = 0
gLock = threading.Lock()

class Producer(threading.Thread):
    def run(self):
        while True:
            global gTime
            global gMoney
            money = random.randint(100,1000)
            gLock.acquire()
            if gTime < gTotalTime:
                gMoney += money
                print("{}挣了{}元，现在总共有{}元".format(threading.currentThread(), money, gMoney))
                gTime += 1
                gLock.release()
                time.sleep(0.5)
            else:
                gLock.release()
                break


class Consumer(threading.Thread):
    def run(self):
        while True:
            global gMoney
            money = random.randint(100, 1000)
            if gTime >= gTotalTime:
                break
            gLock.acquire()
            if money > gMoney:
                print("{}想消费{}元，现在只有{}元,消费失败".format(threading.currentThread(), money, gMoney))
            else:
                gMoney -= money
                print("{}消费{}元，现在剩余{}元".format(threading.currentThread(), money, gMoney))
            time.sleep(0.5)
            gLock.release()

def main():
    for i in range(3):
        consumer = Consumer(name="消费者{}".format(i))
        consumer.start()
    for i in range(5):
        producer = Producer(name="生产者{}".format(i))
        producer.start()


if __name__ == '__main__':
    main()