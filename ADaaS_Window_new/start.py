from device import gwq
from device import idr
from multiprocessing import Process, Queue
import time
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')


class GWQProcess(Process):
    def __init__(self, vid, pid, host_ip, bus_ip, queue_task, queue_result):
        super(GWQProcess, self).__init__()
        self.gwq_device = gwq.DeviceGWQ()
        self.vid = vid
        self.p_id = pid
        self.host_ip = host_ip
        self.bus_ip = bus_ip
        self.queue_task = queue_task
        self.queue_result = queue_result

    def run(self):
        while True:
            print("柜外清: %s %s 等待消息..." % (self.host_ip, self.bus_ip))
            msg = self.queue_task.get()
            print("柜外清: %s %s 收到消息,调用方法: %s" % (self.host_ip, self.bus_ip, msg))
            method = "AHook_" + msg
            func = getattr(self.gwq_device, method)
            result = func(self.vid, self.p_id, self.host_ip, self.bus_ip)
            self.queue_result.put(result)


class IDRProcess(Process):
    def __init__(self, vid, pid, host_ip, bus_ip, queue_task, queue_result):
        super(IDRProcess, self).__init__()
        self.idr_device = idr.DeviceIDR()
        self.vid = vid
        self.p_id = pid
        self.host_ip = host_ip
        self.bus_ip = bus_ip
        self.queue_task = queue_task
        self.queue_result = queue_result

    def run(self):
        while True:
            print("二代证: %s %s 等待消息..." % (self.host_ip, self.bus_ip))
            msg = self.queue_task.get()
            print("二代证: %s %s 收到消息,调用方法: %s" % (self.host_ip, self.bus_ip, msg))
            method = "AHook_" + msg
            func = getattr(self.idr_device, method)
            result = func(self.vid, self.p_id, self.host_ip, self.bus_ip)
            self.queue_result.put(result)


gwq1_task = Queue()
gwq1_result = Queue()
gwq2_task = Queue()
gwq2_result = Queue()

idr1_task = Queue()
idr1_result = Queue()
idr2_task = Queue()
idr2_result = Queue()


@app.route("/call/gwq")
def call_gwq():
    device_id = request.args.get("id")
    method = request.args.get("method")
    if device_id == "gwq1":
        gwq1_task.put(method)
        result = gwq1_result.get()
    else:
        gwq2_task.put(method)
        result = gwq2_result.get()
    return result


@app.route("/call/idr")
def call_idr():
    device_id = request.args.get("id")
    method = request.args.get("method")
    if device_id == "idr1":
        idr1_task.put(method)
        result = idr1_result.get()
    else:
        idr2_task.put(method)
        result = idr2_result.get()
    return result


if __name__ == '__main__':
#     GWQProcess("2b46", "bc01", "10.8.1.101", "1-3.4.1", gwq1_task, gwq1_result).start()  # 实例化进程对象
#     GWQProcess("2b46", "bc01", "10.8.1.101", "1-3.7.1", gwq2_task, gwq2_result).start()  # 实例化进程对象
    IDRProcess("06ce", "e03f", "10.8.1.108", "1-3.6.4", idr1_task, idr1_result).start()  # 实例化进程对象
#     IDRProcess("06ce", "e03f", "10.8.1.101", "1-3.6.4.4", idr2_task, idr2_result).start()  # 实例化进程对象
    app.run(host='0.0.0.0', port=5000)

# if __name__ == '__main__':
#     g1 =gwq.DeviceGWQ()
#     g1.GWQ_StartSign()
    # g1.GWQ_StartKeyboard()
    # g1.AHook_GWQ_StartKeyboard("2b46", "bc01", "10.8.1.101", "1-3.4.1")
    # g1.GWQ_ReadPin()
    # g1.AHook_GWQ_ReadPin("2b46", "bc01", "10.8.1.101", "1-3.4.1")
    # g1.GWQ_StartEvaluator()
    # g1.AHook_GWQ_StartEvaluator("2b46", "bc01", "10.8.1.101", "1-3.4.1")
    # idr = idr.DeviceIDR()
    # idr.PEU_Reader_ReadIDMsg()
    # idr.AHook_PEU_Reader_ReadIDMsg("06ce", "e03f", "10.8.1.101", "1-3.6.1.4")
    # idr.AHook_PEU_Reader_ReadIDMsg("06ce", "e03f", "10.8.1.101", "1-3.6.4.4")

