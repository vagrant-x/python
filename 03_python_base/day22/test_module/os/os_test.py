"""
os 模块：
    os模块是与操作系统交互的一个接口


os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.environ  获取系统环境变量

os.path.abspath(path)  返回path规范化的绝对路径
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间


"""
import os

# 获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())  # D:\08_python\02_workspace\resposities\python_base\03_python_base\day22\re\os

# 改变当前脚本工作目录，相当于shell下cd
os.chdir("testdir")
print(os.getcwd())  # D:\08_python\02_workspace\resposities\python_base\03_python_base\day22\re\os\testdir

# 返回当前目录：.
print(os.curdir)  # .

# 返回当前目录的父目录字符串： ..
print(os.pardir)  # ..

# 可生成多层递归目录
os.makedirs("dir1/dir2")

# 若目录为空，则删除。并递归到上一层目录，如果还是为空，则删除；以此类推
os.removedirs("dir1/dir2")

# 生成单级目录，相当于shell中mkdir dirname
os.mkdir("dir1")

# 删除单级空目录，若目录不为空则无法删除，报错，相当于shell 中 rmdir dirname
os.rmdir("dir1")

# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印。没有设置参数默认当前
print(os.listdir())  # ['os', 'os_test.py', 'testdir']

# 删除一个文件， 不存在则报错
os.remove("test.txt")

# 重命名一个文件/目录
os.rename("test.txt", "new_test.txt")

# 获取文件/目录信息
print(os.stat("new_test.txt"))
"""
    os.stat_result(
        st_mode=33206,
        st_ino=3659174697243147,
        st_dev=850382589,
        st_nlink=1,             链接数
        st_uid=0,
        st_gid=0,
        st_size=0,
        st_atime=1618408602,    访问时间
        st_mtime=1618408602,    修改时间
        st_ctime=1618408602     创建时间
    )
"""

# 输出操作系统特定的路径分隔符， windows下为 "\\", Linux下为"/"
print(os.sep)  # \

# 输出当前平台使用的行终止符， windows下为"\r\n", linux 下为"\n"
print(os.linesep)

# 输出用于分割文件路径的字符串， windows下为;   linux 下为:
print(os.pathsep)  # ;

# 输出字符串指示当前使用平台， windows为 nt    linux 为 posix
print(os.name)  # nt

# 运行shell 命令，直接显示
print(os.system("ls"))

# 获取系统环境变量
print(os.environ)

#--------- os.path ------------
# 返回path 规范化的绝对路径
print(os.path.abspath("D:\\08_python\\02_workspace\\resposities\\python_base"))

# 将path 分割成目录和文件名二元组返回
print(os.path.split("D:\\08_python\\test.txt"))  # ('D:\\08_python', 'test.txt')
# 将path 的目录返回。其实就是 os.path.split(path) 第一个元素
print(os.path.dirname("D:\\08_python\\test.txt"))  # D:\08_python
# 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.basename("D:\\08_python\\test.txt"))  # test.txt

# 如果path存在，返回 True，如果paht不存在，返回False
print(os.path.exists("D:\\08_python"))  # True

# 判断是否是绝对路径
print(os.path.isabs("os"))  # False

# 如果path是一个存在的文件夹，返回 True, 否则返回 False
print(os.path.isfile("new_test.txt"))  # True

# 返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime("new_test.txt"))  # 1618408602.9422123
# 返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime("new_test.txt"))  # 1618408602.9422123
#  返回path所指向的文件或者目录的最后创建时间
print(os.path.getctime("new_test.txt"))  # 1618408602.9422123

# 如果path是一个存在的路径，返回 True, 否则返回 False
print(os.path.isdir("D:\\08_python"))

# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join("D:\\08_python", "new_test.txt"))  # D:\08_python\new_test.txt

