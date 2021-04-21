
## 一、简单应用
import logging

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

# 日志级别 Logger名称 用户输出消息
# WARNING:root:warning message
# ERROR:root:error message
# CRITICAL:root:critical message

"""
可见，默认情况下Python的logging模块将日志打到标准输出中，且只显示大于等于 WARNING 级别的日志，
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），
默认的日志格式为日志级别：Logger名称：用户输出消息。
"""

## 配置日志级别，日志格式，输出位置
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="log1.log",
                    filemode="w")
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

## log1.log 文件内容
# 2021-04-21 21:03:25 test_logging.py[line:28] DEBUG debug message
# 2021-04-21 21:03:25 test_logging.py[line:29] INFO info message
# 2021-04-21 21:03:25 test_logging.py[line:30] WARNING warning message
# 2021-04-21 21:03:25 test_logging.py[line:31] ERROR error message
# 2021-04-21 21:03:25 test_logging.py[line:32] CRITICAL critical message

"""
可见在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open('test.log','w'))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""

## 三、logger对象
"""

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
    记录不同日志级别信息的方法：
    
logging.basicConfig()
    用默认日志格式（Formatter）为日志系统建立一个默认的流处理器（StreamHandler）
    设置基础配置（如日志级别等）并加到根Logger(root logger)

logging.getLogger([name])
    返回一个logger对象，如果没有指定名字返回 root logger

"""
import logging

logger = logging.getLogger()

# 创建一个handler，将日志写入log2.log
fh = logging.FileHandler("log2.log")
# 创建一个handler，用于输出到控制台
sh = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
# 设置asctime 的格式
formatter.datefmt = "%Y--%m--%d %H:%M:%S"

fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")

# #控制台结果：
# 2021--04--21 22:10:25 test_logging.py[line:106] WARNING warning message
# 2021--04--21 22:10:25 test_logging.py[line:107] ERROR error message
# 2021--04--21 22:10:25 test_logging.py[line:108] CRITICAL critical message
# #log2.log 
# 2021--04--21 22:10:25 test_logging.py[line:106] WARNING warning message
# 2021--04--21 22:10:25 test_logging.py[line:107] ERROR error message
# 2021--04--21 22:10:25 test_logging.py[line:108] CRITICAL critical message

"""
logging库提供了多个组件：Logger、Handler、Filter、Formatter。
    Logger对象提供应用程序可直接使用的接口;
    Handler发送日志到适当的目的地;
    Filter提供了过滤日志信息的方法;
    Formatter指定日志显示格式。
    
注意1：
Logger是一个树形层级结构，输出信息之前都要获得一个Logger（如果没有显示的获取则自动创建并使用root Logger，如第一个例子所示）。
      logger = logging.getLogger()返回一个默认的Logger也即root Logger，并应用默认的日志级别、Handler和Formatter设置。
        当然也可以通过Logger.setLevel(lel)指定最低的日志级别，可用的日志级别有logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR、logging.CRITICAL。
      Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()输出不同级别的日志，只有日志等级大于或等于设置的日志级别的日志才会被输出。 
"""
import logging

logger = logging.getLogger()

formatter = logging.Formatter("%(asctime)s %(name)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

# 2021-04-21 21:15:15,619 root test_logging.py[line:144] WARNING logger warning message
# 2021-04-21 21:15:15,619 root test_logging.py[line:145] ERROR logger error message
# 2021-04-21 21:15:15,619 root test_logging.py[line:146] CRITICAL logger critical message

"""
从这个输出可以看出logger = logging.getLogger()返回的Logger名为root。
这里没有用logger.setLevel(logging.Debug)显示的为logger设置日志级别，所以使用默认的日志级别WARNIING，故结果只输出了大于等于WARNIING级别的信息。

注意2：
如果创建两个同名的logger对象
"""
import logging

logger = logging.getLogger()

logger1 = logging.getLogger("mylogger")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("mylogger")
logger2.setLevel(logging.INFO)

fh = logging.FileHandler("log3.log")
sh = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-10s %(message)s")
# 设置asctime 的格式
formatter.datefmt = "%Y--%m--%d %H:%M:%S"

fh.setFormatter(formatter)
sh.setFormatter(formatter)

# logger.addHandler(fh)
# logger.addHandler(sh)

logger1.addHandler(fh)
logger1.addHandler(sh)

logger2.addHandler(fh)
logger2.addHandler(sh)

logger1.debug("logger1 debug message")
logger1.info("logger1 info message")
logger1.warning("logger1 warning message")
logger1.error("logger1 error message")
logger1.critical("logger1 critical message")

logger2.debug("logger2 debug message")
logger2.info("logger2 info message")
logger2.warning("logger2 warning message")
logger2.error("logger2 error message")
logger2.critical("logger2 critical message")

# 控制台结果：
# 2021--04--21 21:35:54 test_logging.py[line:189] INFO       logger1 info message
# 2021--04--21 21:35:54 test_logging.py[line:189] INFO       logger1 info message
# 2021--04--21 21:35:54 test_logging.py[line:190] WARNING    logger1 warning message
# 2021--04--21 21:35:54 test_logging.py[line:190] WARNING    logger1 warning message
# 2021--04--21 21:35:54 test_logging.py[line:191] ERROR      logger1 error message
# 2021--04--21 21:35:54 test_logging.py[line:191] ERROR      logger1 error message
# 2021--04--21 21:35:54 test_logging.py[line:192] CRITICAL   logger1 critical message
# 2021--04--21 21:35:54 test_logging.py[line:192] CRITICAL   logger1 critical message
# 2021--04--21 21:35:54 test_logging.py[line:195] INFO       logger2 info message
# 2021--04--21 21:35:54 test_logging.py[line:195] INFO       logger2 info message
# 2021--04--21 21:35:54 test_logging.py[line:196] WARNING    logger2 warning message
# 2021--04--21 21:35:54 test_logging.py[line:196] WARNING    logger2 warning message
# 2021--04--21 21:35:54 test_logging.py[line:197] ERROR      logger2 error message
# 2021--04--21 21:35:54 test_logging.py[line:197] ERROR      logger2 error message
# 2021--04--21 21:35:54 test_logging.py[line:198] CRITICAL   logger2 critical message
# 2021--04--21 21:35:54 test_logging.py[line:198] CRITICAL   logger2 critical message

"""
问题：
（1）我们明明通过logger1.setLevel(logging.DEBUG)将logger1的日志级别设置为了DEBUG，为何显示的时候没有显示出DEBUG级别的日志信息，而是从INFO级别的日志开始显示呢？
    原来logger1和logger2对应的是同一个Logger实例，只要logging.getLogger（name）中名称参数name相同则返回的Logger实例就是同一个，且仅有一个，也即name与Logger实例一一对应。
    在logger2实例中通过logger2.setLevel(logging.INFO)设置mylogger的日志级别为logging.INFO，所以最后logger1的输出遵从了后来设置的日志级别。

（2）为什么logger1、logger2对应的每个输出分别显示两次?
    这是因为我们通过logger = logging.getLogger()显示的创建了root Logger，而logger1 = logging.getLogger('mylogger')创建了root Logger的孩子(root.)mylogger,logger2同样。
    而孩子,孙子，重孙……既会将消息分发给他的handler进行处理也会传递给所有的祖先Logger处理。
    
    把logger 设置handler的代码注释掉：
        # logger.addHandler(fh)
        # logger.addHandler(sh)
    结果为
"""

# 2021--04--21 21:39:20 test_logging.py[line:189] INFO       logger1 info message
# 2021--04--21 21:39:20 test_logging.py[line:190] WARNING    logger1 warning message
# 2021--04--21 21:39:20 test_logging.py[line:191] ERROR      logger1 error message
# 2021--04--21 21:39:20 test_logging.py[line:192] CRITICAL   logger1 critical message
# 2021--04--21 21:39:20 test_logging.py[line:195] INFO       logger2 info message
# 2021--04--21 21:39:20 test_logging.py[line:196] WARNING    logger2 warning message
# 2021--04--21 21:39:20 test_logging.py[line:197] ERROR      logger2 error message
# 2021--04--21 21:39:20 test_logging.py[line:198] CRITICAL   logger2 critical message

"""
因为我们注释了logger对象设置handler，因为logger 和 logger的父级没有设置日志信息的输出位置，所以在这里只打印了一次。

孩子,孙子，重孙……可逐层继承来自祖先的日志级别、Handler、Filter设置，
也可以通过Logger.setLevel(lel)、Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)、Logger.addFilter(filt)、Logger.removeFilter(filt)。
设置自己特别的日志级别、Handler、Filter。若不设置则使用继承来的值。

Filter
    限制只有满足过滤规则的日志才会输出。
    比如我们定义了filter = logging.Filter('a.b.c'),并将这个Filter添加到了一个Handler上，则使用该Handler的Logger中只有名字带.b.c前缀的Logger才能输出其日志。

    filter = logging.Filter('mylogger1') 
    logger.addFilter(filter)
    这是只对logger这个对象进行筛选
    如果想对所有的对象进行筛选，则：
      filter = logging.Filter('mylogger1') 
      fh.addFilter(filter)
      ch.addFilter(filter)
    这样，所有添加fh或者ch的logger对象都会进行筛选。
"""
import logging

logger1 = logging.getLogger("mylogger1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("mylogger2")
logger2.setLevel(logging.INFO)

fh = logging.FileHandler("log4.log")
sh = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-10s %(message)s")
# 设置asctime 的格式
formatter.datefmt = "%Y--%m--%d %H:%M:%S"

fh.setFormatter(formatter)
sh.setFormatter(formatter)

# 定义filter
filter = logging.Filter("mylogger1")
fh.addFilter(filter)
sh.addFilter(filter)

logger1.addHandler(fh)
logger1.addHandler(sh)

logger2.addHandler(fh)
logger2.addHandler(sh)

logger1.info("logger1 info message")
logger2.info("logger2 info message")

# 结果：
# 2021--04--21 23:56:46 test_logging.py[line:284] INFO       logger1 info message