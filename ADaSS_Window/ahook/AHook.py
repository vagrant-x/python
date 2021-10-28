import ctypes
import time
import os
from tools import filetools

ROOT_PATH = filetools.get_root_path()

def call_device_by_hook(func, *args, **kwargs):
    """
    测试  20210607_钟紫怡_Ahook_usbip测试
    """
    # dll_ahook = ctypes.WinDLL(DLL_32_PATH_AHOOK)
    DLL_32_PATH_AHOOK = os.path.join(ROOT_PATH, r"libs\ahook\Ahook.x86.dll")
    dll_ahook = ctypes.CDLL(DLL_32_PATH_AHOOK)
    print(dll_ahook)

    c1 = ctypes.c_char_p(b"2b46")
    c2 = ctypes.c_char_p(b"bc01")
    host = ctypes.c_char_p(b"10.8.1.101")
    usb_p = ctypes.c_char_p(b"1-3.4.1")

    #  选择替换
    set_res = dll_ahook.SetHook()
    print("---pin_v1》》》SetHook --> set_res = {}".format(set_res))

    # select("2B46", "bc01", "10.8.1.101", "1-3.5.1");
    print("---pin_v1》》》设置参数开始")
    dll_ahook.SelectDev(c1, c2, host, usb_p)
    print("---pin_v1》》》设置参数成功，开始调用")
    # time.sleep(2)
    res = func(*args, **kwargs)
    #  解除替换
    un_set_res = dll_ahook.UnHook()
    print("---pin_v1》》》UnHook --> un_set_res = {}".format(un_set_res))
    return res