import os
import hashlib
import sys
import time

def get_file_md5(filename):
    if not os.path.exists(filename):
        return None
    md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for line in f:
            md5.update(line)
    return md5.hexdigest()

def show_progress_bar(msg, send_size, total_size):
    i = send_size * 100 // total_size
    print("\r", end="")
    print("{}: {}%: ".format(msg, i), "▋" * (i // 2), end="")
    sys.stdout.flush()


if __name__ == '__main__':
    print(get_file_md5("system_tools.py"))

    for i in range(101):
        show_progress_bar("上传文件", i, 100)
        time.sleep(0.05)