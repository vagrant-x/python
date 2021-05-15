
# try:
#     # age_str = input("====>")
#     # age = int(age_str)
#
#     # l1 = []
#     # l1[2]
#
#     d1 = {}
#     d1["name"]
#
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print("KeyError:", e)
# except Exception as e:
#     print("其他未知错误")


# try:
#     age_str = input("====>")
#     age = int(age_str)
# except Exception as e:
#     print("其他未知错误")


# # 异常的其他结构
# s = "a"
# s = 1
# try:
#     int(s)
# except ValueError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except Exception as e:
#     print("捕获未知异常")
# else:
#     print("try 包含的代码块没有异常，执行else 里面的代码")
# finally:
#     print("执行finally 的代码，通常用于释放资源")


# # 主动触发异常
# try:
#     raise TypeError("这个异常是主动触发的")
# except TypeError as e:
#     print(e)


# # 自定义异常
# class MyException(BaseException):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return "<MyException:{}>".format(self.msg)
#
# try:
#     raise MyException("自定义异常")
# except MyException as e:
#     print(e)


# 断言 assert
# 在程序某处判断结果，如果判断结果为 False; 抛出 AssertionError， 效果相当于 if 进行判断，再抛出异常

# assert 1 == 2

if 1 != 2:
    raise AssertionError
