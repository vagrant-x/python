from multiprocessing import Process, Queue
import time
import eel

class MyProcess(Process): #继承Process类
    def __init__(self,name, q):
        super(MyProcess,self).__init__()
        self.name = name
        self.queue = q

    def run(self):
        while True:
            msg = self.queue.get()
            print('测试%s多进程: %s' % (self.name, msg))
            time.sleep(2)

q1 = Queue()
q2 = Queue()

@eel.expose
def init():
    print("初始化")
    MyProcess('Python1', q1).start() #实例化进程对象
    # MyProcess('Python2', q2).start() #实例化进程对象

@eel.expose
def call(bid):
    if bid == "gwq1":
        q1.put("id = gwq1")
    else:
        q2.put("id = gwq2")

eel.init('ui')
eel.start('index.html', mode=None)

# if __name__ == '__main__':
#     for i in range(2):  #开启5个子进程执行fun1函数
#         p = MyProcess('Python' + str(i)) #实例化进程对象
#         p.start()