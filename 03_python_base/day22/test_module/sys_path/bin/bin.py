import sys
import os

# 在pycharm 里面，__file__ 是绝对路径，在命令行模式下是文件名
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("sys_path = {}".format(sys_path))
sys.path.append(sys_path)

from my_module import cal
print(cal.add(1, 2))
