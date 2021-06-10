import ctypes
from ctypes import *
import time

def myfun():
    DLL_64_PATH = r"G:\test\D\ADaSS_Window\libs\gwq\x86\CENT_GWQ.dll"
    print("+++myfun》》》加载dll路径:%s", DLL_64_PATH)
    # dll = ctypes.CDLL(DLL_64_PATH)
    dll = ctypes.WinDLL(DLL_64_PATH)
    print("+++myfun》》》加载的dll: {}".format(dll) )

    # int WINAPI GWQ_StartKeyboard (int iPortNo, char extendPort, int iBaudRate,int iTimeOut, int numType,char *iDisplayResult)
    iProtNo = c_int(0)
    extendPort = c_int(0)  # c_char("NULL")
    iBaudRate = c_int(9600)
    iTimeOut = c_int(30)
    numType = c_int(0)
    # iDisplayResult = create_string_buffer(b'\000' * 1024 * 1024)  # 创建指定大小的内存
    iDisplayResult = c_char_p(b"")
    # -3 打开串口失败
    res = dll.GWQ_StartKeyboard(iProtNo, extendPort, iBaudRate, iTimeOut, numType, iDisplayResult)
    print("+++myfun》》》调用结果：{}".format(res))
    print(iDisplayResult.value.decode("utf-8"))

def call_device_by_hook_pin_v1(func):
    """
    测试  20210607_钟紫怡_Ahook_usbip测试
    """
    DLL_32_PATH_AHOOK = r"G:\test\D\ADaSS_Window\libs\ahook\Ahook.dll"
    # dll_ahook = ctypes.WinDLL(DLL_32_PATH_AHOOK)
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
    time.sleep(2)
    func()
    #  解除替换
    un_set_res = dll_ahook.UnHook()
    print("---pin_v1》》》UnHook --> un_set_res = {}".format(un_set_res))


if __name__ == '__main__':
    # myfun()
    call_device_by_hook_pin_v1(myfun)