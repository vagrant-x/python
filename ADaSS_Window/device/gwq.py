import ctypes
import os
from ctypes import *
from ahook import AHook
from tools import filetools

# 定义柜外清方法名的全局变量
gwq_funs= [
    "GWQ_StartKeyboard",  # 数字键盘
    "GWQ_ReadPin",  # 明文读取密码
    "GWQ_StartEvaluator",  # 启动评价器
]

class DeviceGWQ(object):
    def __init__(self, *args, **kwargs):
        super(DeviceGWQ, self).__init__( *args, **kwargs)
        self.name = "柜外清"
        root_path = filetools.get_root_path()
        self.DLL_64_PATH = os.path.join(root_path, r"libs\gwq\x86\CENT_GWQ.dll")

    def AHook_GWQ_StartKeyboard(self, *args, **kwargs):
        """
        调用钩子库后，再调用数字键盘
        :return:
        """
        res =  AHook.call_device_by_hook(self.GWQ_StartKeyboard, *args, **kwargs)
        print("AHook_GWQ_StartKeyboard res = {}".format(res))
        return res

    def GWQ_StartKeyboard(self, *args, **kwargs):
        """
        数字键盘
        :return:
        """
        print("+++myfun》》》加载dll路径:%s", self.DLL_64_PATH)
        # dll = ctypes.CDLL(DLL_64_PATH)
        dll = ctypes.WinDLL(self.DLL_64_PATH)
        print("+++myfun》》》加载的dll: {}".format(dll))

        # int WINAPI GWQ_StartKeyboard (int iPortNo, char extendPort, int iBaudRate,int iTimeOut, int numType,char *iDisplayResult)
        iProtNo = c_int(0)
        extendPort = c_int(0)  # c_char("NULL")
        iBaudRate = c_int(9600)
        iTimeOut = c_int(30)
        numType = c_int(0)
        # iDisplayResult = create_string_buffer(b'\000' * 1024 * 1024)  # 创建指定大小的内存
        iDisplayResult = c_char_p(b"")
        # -3 打开串口失败
        dll.GWQ_StartKeyboard(iProtNo, extendPort, iBaudRate, iTimeOut, numType, iDisplayResult)
        res = iDisplayResult.value.decode("utf-8")
        print("+++myfun》》》调用结果：{}".format(res))
        print("GWQ_StartKeyboard res = {}".format(res))
        return res

    def GWQ_ReadPin(self):
        """
        启动评价器
        :return:
        """
        pass

    def GWQ_StartEvaluator(self):
        """
          明文读取密码
          :return:
          """
        pass
