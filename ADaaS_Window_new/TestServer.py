from multiprocessing import Process, Queue
import time
from flask import Flask, request
app = Flask(__name__)

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

q1_send = Queue()
q2_send = Queue()

@app.route("/call")
def call():
    bid = request.args.get("id")
    if bid == "gwq1":
        q1.put("id = gwq1")
    else:
        q2.put("id = gwq2")
    return "called"

if __name__ == '__main__':
    MyProcess('Python1', q1_send).start()  # 实例化进程对象
    MyProcess('Python2', q1_send).start()  # 实例化进程对象
    app.run()
