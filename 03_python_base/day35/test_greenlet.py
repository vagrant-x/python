"""
1、greenlet 初体验
2、greenlet module 与 class
3、Switch not call
4、Greenlet 生命周期
5、Greentlet Traceing
6、greenlet 使用建议
7、总结

"""
#
# # 1、greenlet 初体验
# from greenlet import greenlet
# def fun1():
#     print(12)
#     gr2.switch()
#     print(34)
#
# def fun2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1 = greenlet(fun1)
# gr2 = greenlet(fun2)
# gr1.switch()

"""
结果：
    12
    56
    34
"""


# 2、greenlet module 与 class
# 3、Switch not call
# from greenlet import greenlet
# def fun1(x, y):
#     z = gr2.switch(x + y)
#     print("fun1: {}".format(z))
#
# def fun2(u):
#     print("fun2: {}".format(u))
#     gr1.switch(10)
#
# gr1 = greenlet(fun1)
# gr2 = greenlet(fun2)
# print(gr1.switch("hello", "  world"))
# """
# 结果：
#     fun2: hello  world
#     fun1: 10
#     None
# """

# import greenlet
# def fun1(x, y):
#     print("{}, {}".format(id(greenlet.getcurrent()),id(greenlet.getcurrent().parent)))
#     z = gr2.switch(x + y)
#     print("back z = {}".format(z))
#
# def fun2(u):
#     print("{}, {}".format(id(greenlet.getcurrent()), id(greenlet.getcurrent().parent)))
#     return  "hehe"
#
# if __name__ == '__main__':
#     gr1 = greenlet.greenlet(fun1)
#     gr2 = greenlet.greenlet(fun2)
#     print("main_id = {}, gr1_id = {}, gr2_id = {}".format(id(greenlet.getcurrent()),
#             id(gr1), id(gr2)))
#     print(gr1.switch("hello", "world"), "back to main")
# """
# 结果：
#     main_id = 3197756783256, gr1_id = 3197756783608, gr2_id = 3197762760776
#     3197756783608, 3197756783256
#     3197762760776, 3197756783256
#     hehe back to main
# """

# import greenlet
# def fun1(x, y):
#     try:
#         z = gr2.switch(x + y)
#     except Exception:
#         print("catch Exception in fun1")
#
# def fun2(u):
#     assert False
#
# gr1 = greenlet.greenlet(fun1)
# gr2 = greenlet.greenlet(fun2)
# try:
#     gr1.switch("hello", "world")
# except:
#     print("catch Exception in main")
# """
# 结果：
#     catch Exception in main
# """

# 4、Greenlet 生命周期
# from greenlet import greenlet
# def fun1():
#     gr2.switch(1)
#     print("fun1 finished")
#
# def fun2(x):
#     print("fun2 first x = {}".format(x))
#     z = gr1.switch()
#     print("fun2 back z = ".format(z))
#
# if __name__ == '__main__':
#     gr1 = greenlet(fun1)
#     gr2 = greenlet(fun2)
#     gr1.switch()
#     print("gr1 si dead?: {}, gr2 is dead?: {}".format(gr1.dead, gr2.dead))
#     gr2.switch()
#     print("gr1 si dead?: {}, gr2 is dead?: {}".format(gr1.dead, gr2.dead))
#     print(gr2.switch(10))
# """
# 结果：
#     fun2 first x = 1
#     fun1 finished
#     gr1 si dead?: True, gr2 is dead?: False
#     fun2 back z =
#     gr1 si dead?: True, gr2 is dead?: True
#     10
# """



# 5、Greentlet Traceing
# import greenlet
# def test_greenlet_tracing():
#     def callback(event, args):
#         print("event = {}, from {} to {}".format(event,id(args[0]), id(args[1])))
#
#     def dummy():
#         gr2.switch()
#
#     def dummyException():
#         raise Exception("excep in coroutine")
#
#     main = greenlet.getcurrent()
#     gr1 = greenlet.greenlet(dummy)
#     gr2 = greenlet.greenlet(dummyException)
#     print("main_id = {}, gr1_id = {}, gr2_id = {}".format(id(main),id(gr1), id(gr2)))
#     oldtrace = greenlet.settrace(callback)
#     try:
#         gr1.switch()
#     except:
#         print("Exception")
#     finally:
#         greenlet.settrace(oldtrace)
#
# test_greenlet_tracing()
# """
# 结果：
#     main_id = 2149705792152, gr1_id = 2149705792504, gr2_id = 2149711704136
#     event = switch, from 2149705792152 to 2149705792504
#     event = switch, from 2149705792504 to 2149711704136
#     event = throw, from 2149711704136 to 2149705792152
#     Exception
# """




# 6、greenlet 使用建议
from greenlet import greenlet, GreenletExit
huge = []
def show_leak():
    def fun1():
        gr2.switch()

    def fun2():
        huge.extend([x for x in range(100)])
        try:
            gr1.switch()
        finally:
            print("finish switch del huge")
            del huge[:]

    gr1 = greenlet(fun1)
    gr2 = greenlet(fun2)
    gr1.switch()
    gr1 = gr2 = None
    print("length of huge is {}".format(len(huge)))

if __name__ == '__main__':
    show_leak()
"""

上述代码的switch流程：main greenlet --> gr1 --> gr2 --> gr1 --> main greenlet, 很明显gr2没有正常结束（在第10行刮起了）。
执行[ gr1 = gr2 = None ]之后gr1,gr2的引用计数都变成0，那么会在 fun2 的 gr1.switch() 抛出GreenletExit异常，
因此finally语句有机会执行。
同时，在文章开始介绍Greenlet module的时候也提到了，GreenletExit这个异常并不会抛出到parent，所以main greenlet也不会出异常。

　　看上去貌似解决了问题，但这对程序员要求太高了，百密一疏。所以最好的办法还是保证协程的正常结束
结果：
    finish switch del huge
    length of huge is 0
"""


# 7、总结
