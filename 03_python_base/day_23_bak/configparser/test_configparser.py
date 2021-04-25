"""
configparser 模块


"""
# import configparser
# config = configparser.ConfigParser()
#
# config['DEFAULT'] = {"ServerAliveInterval": '45',
#                      "Compression": 'yes',
#                      "COmpressionLevel": "9"}
#
# config["bitbucket.org"] = {}
# config["bitbucket.org"]['User'] = 'hg'
#
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret["Port"] = '50022'
# topsecret["ForwardX11"] = "no"
#
# config["DEFAULT"]["ForwardX11"] = "yes"
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

"""
现在我们已经创建一个配置文件并将数据保存到里面。现在让我们使用这些数据。
"""
# import configparser
#
# config = configparser.ConfigParser()
# print(config.sections())  # []
#
# config.read("example.ini")
# print(config.sections())  # ['bitbucket.org', 'topsecret.server.com']  ## DEFAULT 并没有打印
#
# # 通过 config 查看 是否有 section
# print("DEFAULT" in config)  # True
# print("DEFAULT" in config.sections())  # False
# print("bitbucket.org" in config.sections())  # True
# print("bytebong.org" in config)  # False
#
# # 获取指定section下的值
# print(config['bitbucket.org']['User'])  # hg
# print(config['DEFAULT']['Compression'])  # yes
#
# # 读取整个section
# topsecret = config['topsecret.server.com']
# print(topsecret['ForwardX11'])  # no
# print(topsecret['Port'])  # 50022
#
# # 所有的section都会继承default section 的值
# print("---->key:")
# for key in config['bitbucket.org']:
#     print(key)
# # ---->key:
# # user
# # serveraliveinterval
# # compression
# # compressionlevel
# # forwardx11
#
# print(config['bitbucket.org']['ForwardX11'])  # yes

"""
从上面的例子可以看出：
（1） DEFAULT section 中的值将作为其他 section 的默认值。
（2） section中的key 是不区分大小写，并且以小写保存的。

## 支持的数据类型
配置解析器将所有的数据保存为string 类型；这意味着我们需要其他类型，需要我们自己进行转换。
由于这种需求比较普遍，配置解析器提供了将获取的数据转换为整形，浮点型，布尔型的方法。
整形：getint()
浮点型：getfloat()
布尔型：getboolean()
"""
# print("-----------------> 数据类型：")
# print(topsecret.getboolean('ForwardX11'))  # False ## 配置文件中是 no
# print(config['bitbucket.org'].getboolean('ForwardX11'))  # True  ## 基础自DEFAULT
# print(config.getboolean('bitbucket.org', "Compression"))  # True  ## 基础自DEFAULT
#
# print(type(config.getint('topsecret.server.com', "port"))) # <class 'int'>

"""
FallBack Values
像操作字典一样，可以使用 section 的 get() 方法并提供一个默认值。

"""
# import configparser
#
# config = configparser.ConfigParser()
# config.read("example.ini")
# topsecret = config['topsecret.server.com']
#
# print(topsecret.get("Port"))  # 50022
# print(topsecret.get("Cipher"))  # None  ## 原来没有这个值
# print(topsecret.get('Cipher', '3des-cbc'))  # 3des-cbc
#
# """
# ##注意：DEFAULT 中的默认值优先级高于 fallback values
#     如在 example.ini 文件中， CompressionLevel 这个key只有在 DEFAULT section 中，
#     如果我们获取 topsecret.server.com section 中的 CompressionLevel， 我们将或获取到 DEFAULT中的值，而不是 fallback values
# """
# print(topsecret.get("CompressionLevel", '3'))  # 9
#
# # 还有一点需要注意，解析器级别的get（）方法提供了一个定制的、更复杂的接口，用于向后兼容
# # 当使用这个方法是，可以使用 fallback 关键字提供 fallback value
# print(config.get("bitbucket.org", 'monster', fallback="No such things as monsters"))  # No such things as monsters
#
# # fallback 关键字参数可以用户 getint(), getfloat(), getboolean()
# print("batchMode" in topsecret)  # False
# print(topsecret.getboolean("BatchMode", fallback=True))  # True
# config["DEFAULT"]['BatchMode'] = 'no'
# print(topsecret.getboolean('BatchMode', fallback=True))  # False

"""
支持 ini 文件结构
    （1）section中的键值对通过 = 或 : 进行分割。
    （2）section中的key 是忽略大小写。
    （3）key 和 value 中前后空格将被删除。
    （4）值可以被忽略不写。
    （5）值可以夸多行，只要他的缩进保持一致
    （6）使用 # 或 ; 进行注释
"""
# import configparser
#
# print(configparser)
# config = configparser.ConfigParser()
# config.read("example1.ini")
#
# print(config.get("Multiline Values", "chorus"))
# print(config.get("Sections Can Be Indented", "multiline_values"))


"""
插值：
class configparser.BasicInterpolation
    ConfigParser使用的默认实现，它允许值包含引用同一节中其他值 或 DEFAULT section中的值的 格式字符串。
    下面两行代码效果是一样的：
        config = configparser.ConfigParser()
        config = configparser.ConfigParser(interpolation=configparser.BasicInterpolation())

# example2.ini
# [Paths]
# home_dir: /Users
# my_dir: %(home_dir)s/lumberjack
# my_pictures: %(my_dir)s/Pictures
# 
# # use a %% to escape the % sign (% is the only character that needs to be escaped)
# [Escape]
# gain: 80%%   

import configparser

print(configparser)
# config = configparser.ConfigParser()
config = configparser.ConfigParser(interpolation=configparser.BasicInterpolation())
config.read("example2.ini")

print(config.get("Paths", "my_pictures"))  # /Users/lumberjack/Pictures
print(config.get("Escape", "gain"))  # 80%

 
class configparser.ExtendedInterpolation
    通过 ${section:option} 引用其他section 的值，如果省略 section: 默认使用当前section 或是 DEFAULT中的值。 


# example3.ini

# [Paths]
# home_dir: /Users
# my_dir: ${home_dir}/lumberjack
# my_pictures: ${my_dir}/Pictures
#
# # use a $$ to escape the $ sign ($ is the only character that needs to be escaped)
# [Escape]
# cost: $$80
#
#
#
# [Common]
# home_dir: /Users
# library_dir: /Library
# system_dir: /System
# macports_dir: /opt/local
#
# [Frameworks]
# Python: 3.2
# path: ${Common:system_dir}/Library/Frameworks/
#
# [Arthur]
# nickname: Two Sheds
# last_name: Jackson
# my_dir: ${Common:home_dir}/twosheds
# my_pictures: ${my_dir}/Pictures
# python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}


# ==============================================================



"""
# example.ini 文件内容：
# [DEFAULT]
# serveraliveinterval = 45
# compression = yes
# compressionlevel = 9
# forwardx11 = yes
#
# [bitbucket.org]
# user = hg
#
# [topsecret.server.com]
# port = 50022
# forwardx11 = no

import configparser

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read("example.ini")

# print(config.get("Arthur", "python_dir"))  # /System/Library/Frameworks//Python/Versions/3.2
# print(config.get("Escape", "cost"))  # $80

"""
defaults()
    返回DEFAULT section包含全部实例的字典
print(config.defaults())  # OrderedDict([('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes')])

sections()
    返回除了 DEFAULT section 之外的 其他section 列表
print(config.sections())  # ['bitbucket.org', 'topsecret.server.com']

add_section(section)
    添加一个section到实例中。
config.add_section("test_section")
print(config.sections())  # ['bitbucket.org', 'topsecret.server.com', 'test_section']

has_section(section)
    判断section名是否存在，DEFAULT 默认不存在
print(config.has_section("DEFAULT"))  # False
print(config.has_section("bitbucket.org"))  # True

options(section)
    返回section 下的key, 包含 DEFAULT 里面的
print(config.options("bitbucket.org"))  # ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']

has_option(section, option)
    判断 option 是否存在
print(config.has_option("DEFAULT", "compression"))  # True
print(config.has_option("DEFAULT", "compression_11"))  # False

read(filenames, encoding=None)
    读取配置文件
config.read("example.ini", "utf-8")

查询值
get(section, option, *, raw=False, vars=None[, fallback])
getint(section, option, *, raw=False, vars=None[, fallback])
getfloat(section, option, *, raw=False, vars=None[, fallback])
getboolean(section, option, *, raw=False, vars=None[, fallback])

items(section, raw=False, vars=None)
    返回指定section的 key/value 列表
print(config.items("topsecret.server.com"))
# 结果[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'no'), ('port', '50022')]

set(section, option, value)
config.set("topsecret.server.com", "new_key", "k_2021")
print(config.items("topsecret.server.com"))
# 结果： [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'no'), ('port', '50022'), ('new_key', 'k_2021')]

write(fileobject, space_around_delimiters=True)
    将配置写入到文件
config.write(open("example5.ini", "w"))

remove_option(section, option)
    删除指定 section 下的 option
    
remove_section(section)
    删除指定 section 
"""

