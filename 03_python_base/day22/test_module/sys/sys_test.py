"""
sys 模块


"""
import sys

#-------> Dynamic objects:

# 平台标识
print(sys.platform)  # win32

# 解释器版本
print(sys.version)  # 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)]

# 模块的搜索路径，第一个是执行脚本所在路径
# 如果是通过pycharm 执行，第二个路径是pycharm当前项目的路径
print(sys.path)

# 所有加载模块的字典，key 是模块名， 如 {'sys': <module 'sys' (built-in)>, ......}
print(sys.modules)

#获取命令行参数
"""
    通过命令行执行  python3 sys_test.py param1 param2
        返回 ['sys_test.py', 'param1', 'param2'],第一个参数是文件名
    通过pycharm 运行
        返回 ['D:/08_python/02_workspace/resposities/python_base/03_python_base/day22/re/sys/sys_test.py']
        第一个参数是绝对路径
"""
print(sys.argv)

# 推出解释器，不设置默认为0，如果是整数，将被用于推出状态；如果是其他对象，将会打印该对象
print(sys.exit({"a": 11}))
print("应该不会执行")


# 进度条
import sys
import time
for i in range(100):
    sys.stdout.write("#")
    time.sleep(0.1)
    sys.stdout.flush()

