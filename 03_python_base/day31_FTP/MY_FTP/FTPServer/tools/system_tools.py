import os
import time
import sys

def get_pwd():
    """
    获取项目执行的根目录
    :return:
    """
    return os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_home():
    root = get_pwd()
    return os.path.join(root, "home")

def jindutiao(msg, send_size, total_size):
    scale = 50
    print(msg.center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        a = "*" * i
        b = "." * (scale - i)
        c = (send_size / total_size) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
        time.sleep(0.1)
    # print("\n" + msg.center(scale // 2, "-"))

def show_progress_bar(msg, send_size, total_size):
    i = send_size * 100 // total_size
    print("\r", end="")
    print("{}: {}%: ".format(msg, i), "▋" * (i // 2), end="")
    sys.stdout.flush()

def progress_bar():
  for i in range(1, 101):
    print("\r", end="")
    print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
    sys.stdout.flush()
    time.sleep(0.05)

if __name__ == '__main__':
    print(get_pwd())
    print(get_home())
    # progress_bar()
    for i in range(101):
        show_progress_bar("上传文件", i, 100)
        time.sleep(0.05)