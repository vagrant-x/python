
"""
optparse
    optparse主要用来为脚本传递命令参数，采用预先定义好的选项来解析命令行参数
    实例化一个OptionParser()对象(可以传参也可以不传参)，带参的话会把参数变量的内容作为帮助信息输出。
    即可以用来自己定制程序的参数选项控制。

    Python 有两个内建的模块用于处理命令行参数：
    一个是 getopt，只能简单处理 命令行参数；
    另一个是 optparse，它功能强大，而且易于使用，可以方便地生成标准的、符合Unix/Posix 规范的命令行说明。

    optparse.OptionParser()
        对象中的参数中的：prog 代表当前脚本名字即os.path.basename(sys.argv[0])
    options,args = parser.parse_args()，
        optparse.OptionParser()对象实例调用parse_args()方法后即可解析脚本输入的参数值；
        返回值：
            options是一个包含了option 值的对象，
            args是一个位置参数的列表。
    parse_args()方法可以接受命令中输入的参数，也可以接受一个列表List[]，parse_args(list)


"""
import optparse

usage = "Usage：%prog [option] arg1 arg2 ..."
# parser = optparse.OptionParser()
parser = optparse.OptionParser(usage, version="%prog 1.0")

options, args = parser.parse_args()  # options = {}, args = []
print("options = {}, args = {}".format(options, args))  # options = {}, args = []

parser.add_option("-f", "--file", action="store", dest="finename",type="string",metavar="FILE",help="wirte ouput to file")
parser.add_option("-p", "--port", action="store", dest="port",type="int",help="server port")
parser.add_option("-i", "--ip", dest="ip", type="string", default="127.0.0.1")
parser.print_help()
args = ["start", "-f", "text.txt", '-p', "8080", "vs_1"]  # 相当于执行 python3 test.py -f text.txt -p 8080 的 sys.argv[1:]
options, args = parser.parse_args(args)
print("options = {}, args = {}".format(options, args))
# options = {'finename': 'text.txt', 'port': 8080, 'ip': '127.0.0.1'}, args = ['start', 'vs_1']


"""
-f                  表示短参数名(后面空格/或不用空格接参数属性值)
--file              表示长参数名(后面空格/或=号接参数属性值)
aciton
                    aciton="store"表示用户必须给出一个明确的参数值(即-f或--file后面接的参数值)，
                                并将参数值保存到dest定义的变量名中(即filename变量接收)
                    action="store_true"表示用户不需要给出参数值，
                                将bool值True保存在dest定义的变量名中(即filename变量接收)
                    action="store_false"表示用户不需要给出参数值，
                                将bool值False保存在dest定义的变量名中(即filename变量接收)
dest="filename"     定义一个变量名用来接收前面的长短参数名的参数值，
                    即可调用options.filename来获取长短参数名的参数值
type="string"       定义前面长短参数名的参数值的类型，
                    必须是字符串(这里可以是：string,int,num，float等类型)
metavar="FILE"      当用户查看帮助信息时，如果没有定义metvar的值，
                    那么显示的帮助信息中长短参数名后面默认带上dest所定义的变量名；
                    如果定义了metavar的值，那么现实的帮助信息中长短参数名后面就带上metavar定义的值
default="123.txt"   如果长短参数名未设置参数属性值，则使用默认值代替，
                    前提是action未定义或aciton只能定义为store_true/store_false(即action参数未传入)
help="**"           仅现实帮助信息中的语句提示信息
"""