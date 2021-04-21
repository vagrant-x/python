"""
通过logging.config.fileConfig()配置日志
    相对于直接在文件中配置日志，这种配置方式可以将日志配置和代码分离，方便代码的维护和日志管理。

（1）在配置文件中，首先包含了三大主要模块，loggers, handlers, formatters。
    对于三个主要模块其包含的内容都是通过keys进行指定，
    然后通过logger_key/handler_key/formatter_key对里面的key进行具体的设置。

（2）loggers 配置logger的模块，其中必须包含一个名字叫做root的logger，
    当在应用程序中，使用无参函数logging.getLogger()时，默认返回root这个logger，
    其他自定义logger可以通过 logging.getLogger("name") 方式进行调用。
    当通过logging.getLogger("name.name1"),如果name存在，name1不存在，则 logger name.name1 的配置继承自 name

（3）handlers 定义handlers的信息，通过keys进行指定。里面可以指定我们日志的输出方式、日志的级别、日志的格式等。

（4）formatters表示设置日志的格式。

（5）logger-XXX对loggers中声明的logger进行逐个配置，且要一一对应,
    在所有的logger中，必须制定lebel和handlers这两个选项，
    对于非roothandler，还需要添加一些额外的option，其中qualname表示它在logger层级中的名字，在应用代码中通过这个名字制定所使用的handler，
    即 logging.getLogger("fileAndConsole")，handlers可以指定多个，中间用逗号隔开，
    比如handlers=fileHandler,consoleHandler，同时制定使用控制台和文件输出日志。
    propagate 通常设为零，这样，当我们在handlers中设置多个处理器时，不会多次打印日志信息。

（6）handler_xxx在handler中，必须指定class和args这两个option，
    常用的class包括
        StreamHandler（仅将日志输出到控制台）、
        FileHandler（将日志信息输出保存到文件）、
        RotaRotatingFileHandler（将日志输出保存到文件中，并设置单个日志wenj文件的大小和日志文件个数），
    args表示传递给class所指定的handler类初始化方法参数，它必须是一个元组（tuple）的形式，即便只有一个参数值也需要是一个元组的形式；
    里面指定输出路径，比如输出的文件名称等。
    level与logger中的level一样，
    formatter指定的是该处理器所使用的格式器，这里指定的格式器名称必须出现在formatters这个section中，
    且在配置文件中必须要有这个formatter的section定义；如果不指定formatter则该handler将会以消息本身作为日志消息进行记录，而不添加额外的时间、日志器名称等信息；

（7）在这个配置文件中设置了三种日志的输出方式，root对应控制台输出、file对应配置文件输出、fileAndConsole对应着文件和控制台同时输出

"""


# import logging.config
#
# # 读取 logging.ini 配置文件
# logging.config.fileConfig('logging.ini')
#
# # 创建一个logger
# logger = logging.getLogger("fileAndConsole")
# logger.debug("logger debug")
# logger.info("logger info")
# logger.warning("logger warning")
# logger.error("logger error")
# logger.critical("logger critical")

# 结果
# 2021-04-21 22:54:07 MainThread test_logging_file.py[line:8   ] DEBUG      logger debug
# 2021-04-21 22:54:07 MainThread test_logging_file.py[line:9   ] INFO       logger info
# 2021-04-21 22:54:07 MainThread test_logging_file.py[line:10  ] WARNING    logger warning
# 2021-04-21 22:54:07 MainThread test_logging_file.py[line:11  ] ERROR      logger error
# 2021-04-21 22:54:07 MainThread test_logging_file.py[line:12  ] CRITICAL   logger critical



# import logging.config
# # 读取 logging.ini 配置文件
# logging.config.fileConfig('logging.ini')
# # 创建一个logger
# logger = logging.getLogger("test." + __name__)
# logger.debug("logger debug")

# #结果：
# 2021-04-21 15:27:50 test.__main__ MainThread test_logging_file.py[line:34  ] DEBUG      logger debug
"""
logger = logging.getLogger("test." + __name__)
    通过获取名字为 "test." + __name__ 的logger, 在本次运行中获取名字为 test.__main__ 的logger
    logger test.__main__ 在 logging.ini 文件中并没有实际配置，则其配置继承自 test 的配置。
    
root file test 的图表示

对于propagate属性的说明
"""

# import logging.config
# # 读取 logging.ini 配置文件
# logging.config.fileConfig('logging.ini')
# # 创建一个logger
# logger = logging.getLogger("file")
# logger.info("logger debug")

"""
logging.ini
    [logger_file]
    level=DEBUG
    handlers=fileHandler
    qualname=file
    propagate=1

执行结果：
file_log.log
    2021-04-21 22:00:58 MainThread test_logging_file.py[line:85  ] INFO       logger debug
控制台：
    2021-04-21 22:00:58 MainThread test_logging_file.py[line:85  ] INFO       logger debug

理论上logger_file 只会把日志信息打入到file_log.log 文件中，但是因为logging.ini 文件中设置了 propagate=1
日志记录会向上层logger传递。
如果将propagate 改为 0 ，控制台将不打印信息。
"""

import logging.config
# 读取 logging.ini 配置文件
logging.config.fileConfig('logging.ini')
# 创建一个logger
logger = logging.getLogger("testTR")
logger.info("logger debug")









