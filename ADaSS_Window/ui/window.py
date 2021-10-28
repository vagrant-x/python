import tkinter as tk
import tkinter.messagebox
from device import gwq
from tools import checktools

class AWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super(AWindow, self).__init__( *args, **kwargs)
        self.set_window()
        self.geometry("800x465")  # 设置窗口大小（宽 * 高）
        self.remote_ip = None

    def set_window(self):
        """
        设置左右两个组件容器
        """
        self.top_frame = tk.Frame(self, width=800, height=35, bg="green")
        # 输入ip 提示
        user_label = tk.Label(self.top_frame, text='remote ip: ', width=10, bg='lightgrey')
        user_label.pack(side=tk.LEFT)

        # ip 输入框
        ip_var = tk.StringVar(value='10.8.1.101')
        ip_entry = tk.Entry(self.top_frame, show=None, textvariable=ip_var)  # 显示成明文形式
        ip_entry.pack(side=tk.LEFT)

        # 输入vid_pid 提示
        vpid_label = tk.Label(self.top_frame, text='vid:pid: ', width=10, bg='lightgrey')
        vpid_label.pack(side=tk.LEFT)

        # vid_pid 输入框
        vip_pid_var = tk.StringVar(value='2b46:bc01')
        vpid_entry = tk.Entry(self.top_frame, show=None, textvariable=vip_pid_var)  # 显示成明文形式
        vpid_entry.pack(side=tk.LEFT)

        f_l_btn = tk.Button(self.top_frame, text="init", width=10, command=lambda: self.btn_init_callback(ip_entry, vpid_entry))
        f_l_btn.pack(side=tk.LEFT)

        self.top_frame.pack_propagate(0)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)


    def btn_init_callback(self, ip_entry, vpid_entry):
        print("ip = {}, vid:pid = {}".format(ip_entry.get(), vpid_entry.get()))
        # 获取 IP 并进行检查
        ip = ip_entry.get()
        if not checktools.check_ip(ip):
            tk.Message
            tk.messagebox.showwarning(title='警告', message='输入IP为[{}],格式错误，请重新输入！'.format(ip))
            return
        # 获取 vid_pid 并进行检查
        vid_pid = vpid_entry.get()
        if not checktools.check_vid_pid(vid_pid):
            tk.messagebox.showwarning(title='警告', message='输入vid:pid为[{}],格式错误，请重新输入！'.format(vid_pid))
            return

        print("连接的远程ip :{}".format(ip))
        is_return = False
        if hasattr(self, "left_frame"):
            print("left_frame 已经初始化")
            for widget in self.left_frame.winfo_children():
                widget.destroy()  # 清空子组件
        else:
            self.left_frame = tk.Frame(self, width=400, height=500, bg="grey")
        if hasattr(self, "right_frame"):
            print("right_frame 已经初始化")
            for widget in self.right_frame.winfo_children():
                widget.destroy()
        else:
            self.right_frame = tk.Frame(self, width=400, height=500, bg="lightgrey")

        self.frame_add_element(self.left_frame,  btn_text="1-3.4.1")
        self.left_frame.pack_propagate(0)

        self.frame_add_element(self.right_frame, btn_text="1-3.5.1")
        self.right_frame.pack_propagate(0)

        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.right_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

    # 单选按钮回调函数,就是当单选按钮被点击会执行该函数
    def btn_click_callback(self, text_element, device_gwq, radVar, *args, **kwargs):
        func_str = gwq.gwq_funs[radVar.get()]  # 获取选择的方法
        func_str = "AHook_" + func_str  # 调用带有设置钩子库函数的方法
        if hasattr(device_gwq, func_str):
            func = getattr(device_gwq, func_str)
            result = func(*args, **kwargs)
            text_element.insert("end", "[{}]执行[{}]方法返回结果[{}]\n".format(device_gwq.name, func_str, result))
        else:
            text_element.insert("end","[{}]暂时不支持[{}]方法\n".format(device_gwq.name, func_str))
        # text_element.insert("end", func_str + "\n")  # 将内容设置到Text 显示
        print(func_str)

    def frame_add_element(self, frame, btn_text=None):
        """
        给窗口添加元素
        """
        radVar = tk.IntVar()  # 通过tk.IntVar() 获取单选按钮value参数对应的值
        # radVar.set(99)

        for col in range(len(gwq.gwq_funs)):
            # command=radCall  # 当该单选按钮被点击时，会触发参数command对应的函数
            curRad = tk.Radiobutton(frame, text=gwq.gwq_funs[col], variable=radVar, value=col)
            curRad.pack()

        if not btn_text:
            btn_text = "PORT-1"
        text_element = tk.Text(frame, bg="white", fg="black")
        device_gwq = gwq.DeviceGWQ()  # 创建一个调用柜外清实例
        f_l_btn = tk.Button(frame, text=btn_text, command=lambda: self.btn_click_callback(text_element, device_gwq, radVar))
        f_l_btn.pack()

        text_element.pack(side=tk.TOP, expand=1)


if __name__ == '__main__':
    print(gwq.gwq_funs)
    aWindow = AWindow()
    aWindow.mainloop()

# https://blog.csdn.net/ahilll/article/details/81531587