import ctypes
from ctypes import *
import time
import tkinter as tk

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
    usb_p = ctypes.c_char_p(b"1-3.6.1")

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

def call_back(a):
    print("点击了按钮:{}".format(a))

def my_GUI():
    # 第一步，实例化 object, 建立窗口 window
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title("测试 ubsip")

    # 设置窗口大小（宽 * 高）
    window.geometry("650x500")

    # 定义第一个容器
    # frame_left = tk.LabelFrame(window,  text="测试1", labelanchor="n", width=200, height=200)
    frame_left = tk.Frame(window,width=200, height=600, bg="grey")
    frame_left.pack_propagate(0)
    # frame_left.pack(fill="both", expand="yes")
    # frame_left.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.6)

    # 单选按钮

    # 定义几个颜色的全局变量
    colors = ["Blue", "Gold", "Red"]

    # 单选按钮回调函数,就是当单选按钮被点击会执行该函数
    def radCall():
        radSel = radVar.get()
        print(radVar.get())
        if radSel == 0:
            window.configure(background=colors[0])  # 设置整个界面的背景颜色
        elif radSel == 1:
            window.configure(background=colors[1])
        elif radSel == 2:
            window.configure(background=colors[2])

    radVar = tk.IntVar()  # 通过tk.IntVar() 获取单选按钮value参数对应的值
    radVar.set(99)

    f_l_btn = tk.Button(frame_left, text="1-3.5.1", command=lambda : call_back(radVar.get()))
    f_l_btn.pack()

    for col in range(3):
        # curRad = 'rad' + str(col)
        curRad = tk.Radiobutton(frame_left, text=colors[col], variable=radVar, value=col,
                                command=radCall)  # 当该单选按钮被点击时，会触发参数command对应的函数
        # curRad.grid(column=col, row=5, sticky=tk.W)  # 参数sticky对应的值参考复选框的解释
        curRad.pack()

    frame_left.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.6)


    # 定义第二个容器
    # frame_right = tk.LabelFrame(window, text="测试2", labelanchor="n")
    # frame_right.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.6)

    # f_r_btn = tk.Button(frame_right, text="1-3.6.1", command=call_back)
    # f_r_btn.pack()

    # 最后一步：主窗口循环显示
    window.mainloop()

def test_window():
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title("测试 ubsip")

    # 设置窗口大小（宽 * 高）
    window.geometry("650x500")
    left_frame = tk.Frame(window, width=300, height=600, bg="grey")
    left_frame.pack_propagate(0)
    right_frame = tk.Frame(window, width=300, height=600, bg="lightgrey")
    right_frame.pack_propagate(0)

    left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
    right_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

    window.mainloop()



if __name__ == '__main__':
    # myfun()
    # call_device_by_hook_pin_v1(myfun)
    # my_GUI()
    test_window()
