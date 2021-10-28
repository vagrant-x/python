import ctypes
import os
from ctypes import *
from ahook import AHook
from tools import filetools


class DeviceGWQ(object):
    def __init__(self, *args, **kwargs):
        super(DeviceGWQ, self).__init__(*args, **kwargs)
        self.name = "柜外清"
        root_path = filetools.get_root_path()
        self.DLL_64_PATH = os.path.join(root_path, r"libs\gwq\x86\CENT_GWQ.dll")

    def AHook_GWQ_StartKeyboard(self, vid, pid, host_ip, bus_ip):
        """
        调用钩子库后，再调用数字键盘
        :return:
        """
        return AHook.call_device_by_hook(vid, pid, host_ip, bus_ip, self.GWQ_StartKeyboard)

    def AHook_GWQ_ReadPin(self, vid, pid, host_ip, bus_ip):
        """
        调用钩子库后，再调用密码键盘
        :return:
        """
        return AHook.call_device_by_hook(vid, pid, host_ip, bus_ip, self.GWQ_ReadPin)

    def AHook_GWQ_StartEvaluator(self, vid, pid, host_ip, bus_ip):
        """
        调用钩子库后，再调用评价器
        :return:
        """
        return AHook.call_device_by_hook(vid, pid, host_ip, bus_ip, self.GWQ_StartEvaluator)

    def GWQ_StartKeyboard(self):
        """
        数字键盘
        :return:
        """
        print("加载厂商dll路径:%s", self.DLL_64_PATH)
        dll = ctypes.WinDLL(self.DLL_64_PATH)

        iProtNo = c_int(0)
        extendPort = c_char_p(b'')
        iBaudRate = c_int(9600)
        iTimeOut = c_int(30)
        numType = c_int(0)
        iDisplayResult = ctypes.create_string_buffer(50)
        # -3 打开串口失败
        dll.GWQ_StartKeyboard(iProtNo, extendPort, iBaudRate, iTimeOut, numType, iDisplayResult)
        res = iDisplayResult.value.decode("utf-8")
        print("调用结果：{}".format(res))
        return res

    def GWQ_ReadPin(self):
        """
          明文读取密码
          :return:
          """
        print("加载厂商dll路径:%s", self.DLL_64_PATH)
        dll = ctypes.WinDLL(self.DLL_64_PATH)
        # 设置参数
        iProtNo = c_int(0)
        extendPort = c_char_p(b'')
        iBaudRate = c_int(9600)
        iPinMode = c_int(1)
        iVoiceType = c_int(0)
        iTimeOut = c_int(30)
        pin = ctypes.create_string_buffer(20)
        iPinSize = c_int(20)
        dll.GWQ_ReadPin(iProtNo, extendPort, iBaudRate, iPinMode, iVoiceType, iTimeOut, pin, iPinSize)
        res = pin.value.decode("utf-8")
        print("调用结果：{}".format(res))
        return res

    def GWQ_StartEvaluator(self):
        """
        启动评价器
        :return:
        """
        print("加载厂商dll路径:%s", self.DLL_64_PATH)
        dll = ctypes.WinDLL(self.DLL_64_PATH)
        # 设置参数
        iProtNo = c_int(0)
        extendPort = c_char_p(b'')
        iBaudRate = c_int(9600)
        tellerName = c_char_p("张三".encode())
        tellerNo = c_char_p(b"A0000")
        nStartLevel = 3
        headfile = c_char_p(b"")
        iTimeOut = c_int(30)
        evalValue = POINTER(c_int)(c_int(0))
        dll.GWQ_StartEvaluator(iProtNo, extendPort, iBaudRate, tellerName,
                               tellerNo, nStartLevel, headfile, iTimeOut, evalValue)
        eval_result = evalValue[0]
        if eval_result == 1:
            res = "满意"
        elif eval_result == 2:
            res = "一般"
        elif eval_result == 3:
            res = "不满意"
        else:
            res = "无效评价"
        print("调用结果：{}".format(res))
        return res

    def GWQ_StartSign(self):
        """
        启动电子签名
        :return:
        """
        print("加载厂商dll路径:%s", self.DLL_64_PATH)
        dll = ctypes.WinDLL(self.DLL_64_PATH)
        # 设置参数
        iProtNo = c_int(0)
        extendPort = c_char_p(b'')
        iBaudRate = c_int(9600)
        iTimeOut = c_int(30)
        pdfPath = c_char_p(b"hwBack.pdf")
        signPath = c_char_p(b"hw.png")
        XmlPath = c_char_p(b"hw.xml")
        res = dll.GWQ_StartSign(iProtNo, extendPort, iBaudRate, iTimeOut, pdfPath, signPath, XmlPath)
        print("调用结果： %s" % res)
        pdf_bytes = self.read_pdf("hw.png")
        return res

    def read_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as pdf:
            pdf_bytes = pdf.read()
        chk = 0
        for pdf_int in pdf_bytes:
            chk = chk ^ pdf_int
        chk_byte = chk.to_bytes(1, byteorder='big')
        len_bytes = len(pdf_bytes).to_bytes(3, byteorder='big')
        return b'\x02\x02' + chk_byte + len_bytes + pdf_bytes
