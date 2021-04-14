"""
time 模块
三种时间表示：
    在python中，通常有这几种方式表示时间：
    时间戳（timestamp):通常来说，时间戳表示的是1970年1月1日00:00:00 开始按秒计算的偏移量，运行 type(time.time()), 返回的是float 类型
    格式化的时间字符串
    元组（struct_time): struct_time 元组共有9个元素：（年，月， 日，时，分，秒，一周中第几天，一年中第几天，夏令时）
"""
import time

#1 time()：返回当前时间的时间戳
print(time.time())  # 1618128926.9447072
print(type(time.time()))  # <class 'float'>

# 2 localtime([secs])
# 将一个时间戳转换为当前时区的 struct_time。secs 参数没提供时，默认使用当前时间
print(time.localtime())  # time.struct_time(tm_year=2021, tm_mon=4, tm_mday=11, tm_hour=16, tm_min=16, tm_sec=12, tm_wday=6, tm_yday=101, tm_isdst=0)
print(time.localtime(3661.0))  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=9, tm_min=1, tm_sec=1, tm_wday=3, tm_yday=1, tm_isdst=0)
# 注意：3661s 本来应该是1970年1月1日，01:01:01,但是返回的对象中 tm_hour=9,是因为测试的时候是在东八区，相对于世界标准时间差8小时，所以 tm_hour=9

# 3 gmtime([secs]) 和 localtime() 方法类似，gmtime() 方法是将一个时间戳转换为 UTC 时区（0时区）的 struct_time
print(time.gmtime())  # time.struct_time(tm_year=2021, tm_mon=4, tm_mday=11, tm_hour=8, tm_min=26, tm_sec=26, tm_wday=6, tm_yday=101, tm_isdst=0)
print(time.gmtime(3661.0))  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=1, tm_sec=1, tm_wday=3, tm_yday=1, tm_isdst=0)

# 4 mktime(t) 是将一个 struct_time 转换为时间戳
print(time.mktime(time.localtime()))  # 1618129704.0

# 5 asctime([t])
# 把一个表示时间的元组或者 struct_time 表示为这种形式： "Thu Jan  1 09:01:01 1970"
# 如果没有参数，将会把time.localtime() 作为参数传入。
print(time.asctime())  # Sun Apr 11 16:30:06 2021
print(time.asctime(time.localtime(3661.0)))  # Thu Jan  1 09:01:01 1970
print(time.asctime((2021, 4, 11, 7, 25, 12, 6, 101, 0)))  # Sun Apr 11 07:25:12 2021

# 6 ctime([secs])
# 把一个时间戳转换为 time.asctime() 的形式。如果参数未给出或者为 None的时候，会将默认 time.time() 为参数。
# 他的作用相当于 time.asctime(time.localtime(secs))
print(time.ctime())  # Sun Apr 11 16:37:17 2021
print(time.ctime(time.time()))  # Sun Apr 11 16:37:17 2021

# 7 strftime(format[,t])
# 把一个代表时间的元组或者 struct_time (如由 time.localtime() 和 time.gmtime() 返回) 转化为格式化的时间字符串。
# 如果没有传入 t ，将传入 time.localtime()。
print(time.strftime("%Y-%m-%d %X", time.localtime()))  # 2021-04-11 16:40:14
print(time.strftime("%Y-%m-%d %H::%M::%S", time.localtime()))  # 2021-04-11 16::41::27

# 8 time.strptime(string[, format])
# 把一个格式化时间字符串转化为 struct_time。 和 strftime() 是逆操作。
# 如果没有设置格式化字符串，默认为： "%a %b %d %H:%M:%S %Y"
print(time.strptime("2021-04-11 16:40:14", "%Y-%m-%d %X"))  # time.struct_time(tm_year=2021, tm_mon=4, tm_mday=11, tm_hour=16, tm_min=40, tm_sec=14, tm_wday=6, tm_yday=101, tm_isdst=-1)
print(time.strptime("Thu Jan  1 09:01:01 1970"))  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=9, tm_min=1, tm_sec=1, tm_wday=3, tm_yday=1, tm_isdst=-1)

# 9 sleep(secs)
# 线程执行到这里，等待secs 秒后继续执行，单位为秒
time.sleep(1)

# 查看time 模块方法的使用方法
print(help(time.asctime))