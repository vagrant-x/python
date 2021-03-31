print(" ---- 文件操作 -----")

# ============= 读 ==================
# test_r.txt 文件
# 1
# 22
# 333
# 4444
# 55555
#
# """
#     r 读取文件必须存在，文件不存在报错
# """
# f = open("test_r.txt", encoding="utf-8")
# data = f.read()
# print(data)
# f.close()
# # 1
# # 22
# # 333
# # 4444
# # 55555
#
# # 文件必须存在，不存在抛出异常
# f = open("test001.txt", encoding="utf-8")
# data = f.read()
# print(data)
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'test001.txt'
#
# f = open("test_r.txt", 'r', encoding="utf-8")
# print("文件是否可读：{}".format(f.readable()))
# # print(f.readline())  # 读取一行数据
# print(f.readlines())  # 返回所有行数据的列表 ['1\n', '22\n', '333\n', '4444\n', '55555']
# f.close()


# ============= 写 ==================

# f = open("test_w.txt", 'w', encoding="utf-8")
# print("文件是否可读：{}".format(f.readable()))
# print("文件是否可写：{}".format(f.writable()))
# f.write("a\nbb\n")  # 写入一个字符串
# f.writelines(['ccc\n', 'ddddd\n'])  # 写入一个列表
# f.close()



# ============= 追加 ==================
# f = open("test_a.txt", 'a', encoding='utf-8')
# f.write("新添加的内容")
# f.close()


# =========================== 其他处理模式 ===============================

# # with 关键字
# with open("t1_r.txt", 'r', encoding='utf-8') as f_r,\
#     open('t1_w.txt', 'w', encoding='utf-8') as  f_w:
#     data = f_r.read()
#     f_w.write(data)


# # 查看文件打开时编码
# f = open('test_r.txt')
# print("文件 {} 的编码：{}".format(f.name, f.encoding))  # 文件 test_r.txt 的编码：cp936(GBK)


# =========================== 文件处理模式b模式 ===============================

# # 字符串 -------- encode-------> bytes
# # bytes ----------decode -------> 字符串
#
# # 从文件中直接读取字节数据
# f = open("test_b_r.txt", "rb")
# data = f.read()
# print(data)
# print(data.decode('utf-8'))
# f.close()
#
# # 直接将字节数据写入文件
# f = open("test_b_w.txt", "wb")
# f.write("2222".encode("utf-8"))
# f.close()
#
# # 在文件后面追加字节数据
# f = open("test_b_a.txt", "ab")
# f.write("这是追加的文字".encode("utf-8"))
# f.close()


# =========================== 文件的其他方法 ===============================
#
# # r+ 可读，可写
# f = open('test_a+.txt', 'r+', encoding='utf-8')
# print(f.read())
# print(f.write("新写入的内容"))  # 写入完成，返回写入字符长度
# f.close()

# # 测试 tell 获取光标位置
# f = open('test_a+.txt', 'r+', encoding='utf-8')
# print("光标初始位置：{}".format(f.tell()))  # 光标初始位置：0
# print(f.readline())  # 文件内容为r+
# print("光标读取一行后位置：{}".format(f.tell()))  # 光标读取一行后位置：19
# f.close()


# # 测试truncate
# # 从头开始计算，将文件只保留前n个字节的内容，文件必须以写方式打开，
# # 但是除了w 和 w+ 除外， w模式会直接清空原有内容
# f = open('test_truncate.txt', 'r+', encoding='utf-8')
# print(f.read())  # 文件内容 0123456789abcdef
# f.truncate(10)  # 执行后文件内容 0123456789
# f.close()

"""
seek有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
    0 默认方式，从文件的其实开始计算字节的位置
    1 从上一次光标的位置开始计算光标的位置
    2 从末尾倒着计算光标的位置

    test_seek.txt 文件内容
    aaabbbccc1
    dddeeefff2

    这里使用字母进行测试，如果使用中文，一个中文字符utf-8编码需要3个字节，
    待会测试可能出现乱码，为了方便，测试文件内容没有中文
"""
# f = open('test_seek.txt', 'r+', encoding='utf-8')
# f.seek(1)  # 从开始计算，将光标移动到第三个字节处
# print(f.tell())  # 1
# print(f.readline())  # aabbbccc1
# f.seek(3)
# print(f.tell())  # 3
# print(f.read())
# # 结果：
# #     bbbccc1
# #     dddeeefff2
#
# #第二个参数为 1
# f = open("test_seek_012.txt", 'rb')
# print(f.tell())  # 0
# f.seek(3, 1)  # 从开始移动三个字节
# print(f.tell())  # 3
# f.seek(4, 1)  # 在上次的基础上移动4个字节
# print(f.tell())  # 7
#
# # 第二个参数为 2
# # 文件内容 aaabbbcccddd111222333
# f = open("test_seek_012.txt", 'rb')
# print(f.tell())  # 0
# f.seek(-9, 2)
# print(f.tell())  # 12
# print(f.read())  # b'111222333'
# print(f.tell())  # 21


# 其他方法
# f = open('test_a+.txt', 'r+', encoding='utf-8')
# print("文件是否关闭：{}".format(f.closed))  # 文件是否关闭：False
# print("文件打开编码：{}".format(f.encoding))  # 文件打开编码：utf-8
# print("文件光标未知：{}".format(f.tell()))  # 文件光标未知：0
# print("将内容从内存写入硬件（文件）：{}".format(f.flush()))  # 将内容从内存写入硬件（文件）：None
# f.close()


# 小例子 ： 读取日志文件的最后一行日志
"""
test_log.txt 内容如下：
这是第1行
这是第2行
这是第3行
这是第4行
这是第5行
这是第6行
这是最后一行
"""
f = open("test_log.txt", "rb")
char_length = -20
while True:
    f.seek(char_length, 2)
    data = f.readlines()
    if len(data) > 1:
        print(data[-1].decode("utf-8"))  # 这是最后一行
        break
    char_length *= 2
f.close()


# # with 关键字
# with open("t1_r.txt", 'r', encoding='utf-8') as f_r,\
#     open('t1_w.txt', 'w', encoding='utf-8') as  f_w:
#     data = f_r.read()
#     f_w.write(data)
