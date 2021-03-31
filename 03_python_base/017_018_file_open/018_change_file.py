print("测试几个练习")

"""
（1）将硬盘存放的该文件内容全部加载到内存，在内存中修改，修改后，由内存覆盖硬盘（vim等）
"""
import os
def func1(filename):
    with open(filename, 'r', encoding="utf-8") as read_f,\
        open(filename + ".swap", "w", encoding='utf-8') as write_f:
        data = read_f.read()  # 读取文件所有内容
        data = data.replace("ok", "line:")
        write_f.write(data)
    os.remove(filename)  # 删除原来文件
    os.rename(filename + ".swap", filename)  # 重命名临时文件
func1("test_change_file.txt")


"""
（2）将硬盘存放的文件内容一行一行地读入内存，修改完毕后写入新文件，最后用新文件覆盖源文件
"""
import os
def func1(filename):
    with open(filename, 'r', encoding="utf-8") as read_f,\
        open(filename + ".swap", "w", encoding='utf-8') as write_f:
        for data in read_f:
            data = data.replace( "line:", "ok")
            write_f.write(data)
    os.remove(filename)  # 删除原来文件
    os.rename(filename + ".swap", filename)  # 重命名临时文件
func1("test_change_file.txt")