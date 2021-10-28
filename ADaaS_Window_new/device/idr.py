import ctypes
import os
from ctypes import *
from ahook import AHook
from tools import filetools
import time

class DeviceIDR(object):
    def __init__(self, *args, **kwargs):
        super(DeviceIDR, self).__init__(*args, **kwargs)
        self.name = "二代证"
        root_path = filetools.get_root_path()
        self.DLL_64_PATH = os.path.join(root_path, r"libs\idr\x86\est32.dll")

    def AHook_PEU_Reader_ReadIDMsg(self, vid, pid, hostIp, busIp):
        """
        调用钩子库后，再调用二代证
        :return:
        """
        return AHook.call_device_by_hook(vid, pid, hostIp, busIp, self.PEU_Reader_ReadIDMsg)

    def PEU_Reader_ReadIDMsg(self):
        """
        读取身份证信息
        :return:
        """
        print("加载厂商dll路径:%s", self.DLL_64_PATH)
        dll = ctypes.WinDLL(self.DLL_64_PATH)
        # 连接读卡器
        dev_name = c_char_p(b"USB1")
        readHandle = dll.EU_Reader_Open(dev_name)
        if readHandle > 0:
            pBmpFile = c_char_p(b"")
            pName = ctypes.create_string_buffer(50)
            pSex = ctypes.create_string_buffer(10)
            pNation = ctypes.create_string_buffer(10)
            pBirth = ctypes.create_string_buffer(30)
            pAddress = ctypes.create_string_buffer(100)
            pCertNo = ctypes.create_string_buffer(50)
            pDepartment = ctypes.create_string_buffer(50)
            pEffectData = ctypes.create_string_buffer(30)
            pExpire = ctypes.create_string_buffer(30)
            pErrMsg = ctypes.create_string_buffer(50)
            # 读取身份证信息
            begin_time = time.time()
            is_success = False
            while True:
                read_result = dll.PEU_Reader_ReadIDMsg(readHandle, pBmpFile, pName, pSex, pNation, pBirth, pAddress, pCertNo, pDepartment, pEffectData, pExpire, pErrMsg)
                if read_result == 0:
                    is_success = True
                    break
                else:
                    current_time = time.time()
                    if (current_time - begin_time) > 30:
                        print("读卡超时")
                        break
                    else:
                        time.sleep(0.5)
            if is_success:
                res = {
                    "姓名": pName.value.decode("gbk"),
                    "性别": pSex.value.decode("gbk"),
                    "民族": pNation.value.decode("gbk"),
                    "出生": pBirth.value.decode("gbk"),
                    "住址": pAddress.value.decode("gbk"),
                    "公民身份号码": pCertNo.value.decode("gbk"),
                    "签发机关": pDepartment.value.decode("gbk"),
                    "有效期限": pExpire.value.decode("gbk")
                }
            else:
                res = "读取失败"
            # 断开连接
            dll.EU_Reader_Close(readHandle)
        else:
            res = "打开身份证阅读器失败"
        print("调用结果：{}".format(res))
        return res
