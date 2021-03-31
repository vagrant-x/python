print(" ---- 文件操作 -----")

# ============= 读 ==================
# test_r.txt 文件
# 1
# 22
# 333
# 4444
# 55555

"""
    r 读取文件必须存在，文件不存在报错
"""
# f = open("test_r.txt", encoding="utf-8")
# data = f.read()
# print(data)
# f.close()
# # 1
# # 22
# # 333
# # 4444
# # 55555

# f = open("test001.txt", encoding="utf-8")
# data = f.read()
# print(data)
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'test001.txt'

# f = open("test_r.txt", 'r', encoding="utf-8")
# print("文件是否可读：{}".format(f.readable()))
# # print(f.readline())  # 读取一行数据
# print(f.readlines())  # 返回所有行数据的列表 ['1\n', '22\n', '333\n', '4444\n', '55555']
# f.close()


# ============= 读 ==================

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

# with 关键字
with open("t1_r.txt", 'r', encoding='utf-8') as f_r,\
    open('t1_w.txt', 'w', encoding='utf-8') as  f_w:
    data = f_r.read()
    f_w.write(data)

# 查看文件编码
f = open('test_r.txt')
print("文件 {} 的编码：{}".format(f.name, f.encoding))  # 文件 test_r.txt 的编码：cp936(GBK)
