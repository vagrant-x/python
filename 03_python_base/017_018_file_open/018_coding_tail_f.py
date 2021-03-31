print("测试几个练习")

"""
练习，基于seek 实现 tail -f 功能
"""
import time
def tail_f(filename):
    with open(filename, 'rb') as f:
        f.seek(0, 2)  # 将光标设置到文件的最后
        while True:
            data = f.readline()
            if data:
                print(data.decode("utf-8"))
            else:
                time.sleep(1)  # 等待1s 再读取
tail_f("test_tail_f.txt")

