print(" 迭代器 生成器 列表解释器")

"""
    迭代器 生成器 列表解释器
        
一、递归和迭代
    递归：在函数定义中使用函数自身的方法。（A调用A）
    迭代：利用变量的原值推算处变量的一个新值。（A不停调用B）
    
二、什么是迭代器协议
    1、迭代器协议：对象必须提供一个next方法，执行该方法要买返回一个迭代中的下一项，
           要么就引起一个 StopIteration 异常（只能往后走，不能往前走）
    2、可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个__iter__() 方法）
    3、协议是一种约定，可迭代对象实现了迭代器协议，python的内部工具（入for循环，sum,min，max函数等）
    使用迭代器协议访问对象。
    
    4、for循环调用可迭代对象
    for循环的本质：循环所有对象，全部使用迭代器协议。
    问题：for循环的本质是遵循迭代器协议去访问对象，那么for循环的对象肯定都是迭代器了!!
        那既然这样，for循环可以遍历（字符串、列表、元组、字典、集合、文件对象），那这些数据类型肯定都是迭代器对象。
        但是，定义的一个列表 l = [1, 2] 没有 l.next() 方法。这不矛盾了？？？
    其实：（字符串、列表、元组、字典、集合、文件对象）都是可迭代对象，只不过在for循环时，
        调用了他们内部的__iter__()方法，生成一个迭代器对象。
    然后，for循环调用迭代器对象的__next__方法取值，而且for循环会捕获 StopIteration 异常，以终止迭代。
    
四、为什么要用for循环
    序列类型字符串、列表、元组都有下标，他们可以通过下标进行访问，但是对于非序列类型如字典、集合、文件等无法通过下标访问。
    for循环基于迭代器协议提供了统一的可以遍历对象的方法，即在遍历之前，先调用对象的__iter__ 方法生成一个迭代器，
    然后使用迭代器协议去实现循环访问，这样所有的对象都可以通过for循环进行访问。
    
"""



"""
    
二、迭代器
    递归：在函数定义中使用函数自身的方法。（A调用A）
    迭代：利用变量的原值推算处变量的一个新值。（A不停调用B
1、概念
    迭代器，被用于迭代的对象。利用变量的原值推算处变量的一个新值。（A不停调用B）

2、为什么要有迭代器？什么是可迭代对象？什么是迭代器对象？
   为什么要有迭代器？
   对于序列类型：字符串、列表、元组，我们可以使用索引的方式迭代取出其包含的元素。但对于字典、集合、文件等类型是没有索引的，若还想取出其内部包含的元素，则必须找出一种不依赖于索引的迭代方式，这就是迭代器
   
   什么是可迭代对象？
   可迭代对象指的是内置有 __iter__ 方法的对象，即 obj.__iter__, 如下
"""
# "python".__iter__()
# (1,2,).__iter__()
# {1,2}.__iter__()
# [1,2].__iter__()
# {"a": 1}.__iter__()
# open("test.txt").__iter__()

"""
    什么是迭代器对象？
    可迭代对象执行 obj.__iter__()得到的结果就是迭代器对象；
    而迭代器对象指的是既内置有__iter__ 有内置有 __next__ 方法的对象。
"""
# #文件类型的迭代器对象
# open("test.txt").__iter__()
# open("test.txt").__next__()

"""
    注意：迭代器对象是可迭代对象；可迭代对象不一定是迭代器对象。
3、迭代器对象的使用
"""
# dic = {"a": 1, "b": 2}
# iter_dic = dic.__iter__()  # 得到字典的迭代器对象，该迭代器对象既有 _iter__ 又有 __next__
# print(iter_dic is iter_dic.__iter__())  # True ，迭代器调用 __iter__ 得到的对象还是本身
#
# print(iter_dic.__next__())  # a
# print(iter_dic.__next__())  # b
# # print(iter_dic.__next__())  # StopIteration 抛出异常

"""
4、for 循环调用迭代器
    for循环的工作原理：
    #1 执行in后面对象的dic.__iter__() 方法，得到一个迭代器对象 iter_dic
    #2 执行next(iter_dic), 将得到的值赋值给k,然后执行循环体代码
    #3 重复过程2，直到捕抓到异常 StopIteration,结束循环
"""
# dic = {"a": 1, "b": 2}
# for k in dic:
#     print(dic[k])
# 结果：
#     1
#     2

"""
5、迭代器的优缺点
    优点：
        提供一种统一的、不依赖于索引的迭代方式
        惰性计算，节省内存
    缺点：
        无法获取长度（只有next完毕才知道到底几个值）
        一次性、只能往后走，不能回退
        
三、生成器
# 1、什么是生成器函数
#     在Python中使用了 yield 的函数被称为生成器（generator）。跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
#     在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
#     调用一个生成器函数，返回的是一个 generator 对象。
#     
# """
# # 定义一个生成器函数
# def gensquares(N):
#     for i in range(N):
#         yield i ** 2
#
# # 调用生成器函数
# # for i in gensquares(5):
# #     print(i, end=" : ")  # 0 : 1 : 4 : 9 : 16 :
# #     print()
#
# # 通过生成器函数获取生成器对象
# # 生成器对象有一个 __next__ 方法，可以开始这个函数，或者从它上次yield值后的地方恢复执行，
# # 在产生一系列值后，再次调用将抛出 StopIteration 异常
# x = gensquares(3)
# print(x)  # <generator object gensquares at 0x00000233E21105E8>
# # print(x.__next__())  # 0
# # print(x.__next__())  # 2
# # print(x.__next__())  # 4
# # print(x.__next__()) # StopIteration
#
#
# # 通过 yield 实现斐波那契数列
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if(counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
# f = fibonacci(10)
# print(dir(f))  # [......, 'close', 'send', 'throw']
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         print("退出")  # 0 1 1 2 3 5 8 13 21 34 55 退出
#         break
#
# # send 方法
# """
#     通过调用 next() 或 __next__() 方法，可以实现从外界控制生成器的执行。
#     除此之外，通过send() 方法，还可以向生成器中传值，send() 方法可以带一个参数，也可以不带任何参数（用None 表示）。
#     其中，当使用不带参数的 send() 方法时，它和 next() 函数的功能完全相同。
#     注意，虽然 send(None) 的功能是 next() 完全相同，但更推荐使用 next()，不推荐使用 send(None)
#     注意，带参数的 send(value) 无法启动执行生成器函数。也就是说，程序中第一次使用生成器调用 next() 或者 send() 函数时，不能使用带参数的 send() 函数。
# """
# def intNum():
#     print("开始执行")
#     for i in range(5):
#         yield i
#         print("继续执行")
#
# num = intNum()
# print(num.send(None))
# print(num.send(None))
# # 结果：
# #     开始执行
# #     0
# #     继续执行
# #     1
#
# """
#     这里重点讲解一些参数的 send(value) 的用法，其具备 next() 函数的部分功能，即将暂停在 yield 语句处的程序继续执行，
#     但与此同时，该函数还会将 value 值作为 yield 语句返回值赋值给接收者。
#
# """
# def getStr():
#     value1 = yield "string 1"
#     value2 = yield value1
#     yield value2
#
# g = getStr()
# print(g.send(None))
# print(g.send("第二次获取结果"))
# print(g.send("第三次获取结果"))
# # 结果：
# #     string 1
# #     第二次获取结果
# #     第三次获取结果
#
# """
# 分析一下此程序的执行流程：
# 1) 首先，构建生成器函数，并利用器创建生成器（对象）g 。
#
# 2) 使用生成器 g 调用无参的 send() 函数，其功能和 next() 函数完全相同，因此开始执行生成器函数，即执行到第一个 yield "string 1" 语句，该语句会返回 "string 1" 字符串，然后程序停止到此处（注意，此时还未执行对 value1 的赋值操作）。
#
# 3) 下面开始使用生成器 g 调用有参的 send() 函数，首先它会将暂停的程序开启，同时还会将其参数“第二次获取结果”赋值给当前 yield 语句的接收者，也就是 value1 变量。程序一直执行完 yield value1 再次暂停，因此会输出“第二次获取结果”。
#
# 4） 最后依旧是调用有参的 send() 函数，同样它会启动餐厅的程序，同时将参数“第三次获取结果”传给 value2，然后执行完 yield value2 后（输出 第三次获取结果），程序执行再次暂停。
#
# 因此，该程序的执行结果为：
# string 1
# 第二次获取结果
# 第三次获取结果
# """
#
# # clsoe 方法
# """
#     当程序在生成器函数中遇到 yield 语句暂停运行时，此时如果调用 close() 方法， 会阻止生成器函数继续执行，
#     该函数会在程序停止运行的位置抛出 GeneratorExit 异常
#     注意，虽然通过捕获 GeneratorExit 异常，可以继续执行生成器函数中剩余的代码，带这部分代码中不能再包含 yield 语句，否则程序会抛出 RuntimeError 异常
#     另外，生成器函数一旦使用 close() 函数停止运行，后续将无法再调用 next() 函数或者 __next__() 方法启动执行，否则会抛出 StopIteration 异常。
# """
#
# def getStr1():
#     try:
#         yield "string 11"
#     except GeneratorExit:
#         print("捕获到 GeneratorExit")
#
# g1 = getStr1()
# print(next(g1))
# g1.close()
#
# # 结果：
# #     string 11
# #     捕获到 GeneratorExit
#
#
# """
#     throw
#     生成器 throw() 方法的功能是，在生成器函数执行暂停处，抛出一个指定的异常，之后程序会继续执行生成器函数后续的代码，直到遇到下一个yield 语句。
#     注意，如果到剩余代码执行完毕没有遇到下一个 yield 语句，则程序会抛出 StopIteration 异常。
#
# """
# def getStr2():
#     try:
#         yield "string 22"
#         print("继续执行")  # 下面调用时这里没有执行
#     except ValueError:
#         print("捕获到 ValueError")
#
# g2 = getStr2()
# print(next(g2))
# g2.throw(ValueError)
# print("再次调用-----------》")
#
# # 结果：
# #     string 22
# #     捕获到 ValueError
# #         exec(compile(contents+"\n", file, 'exec'), glob, loc)
# #       File "D:/018_iterator_generator.py", line 244, in <module>
# #         g2.throw(ValueError)
# #     StopIteration
#
# # 显然，一开始生成器函数在 yield "string 22" 处暂停执行，当执行 throw() 方法时，它会先抛出 ValueError 异常，然后继续执行后续代码找到下一个 yield 语句，该程序中由于后续不再有 yield 语句，因此程序执行到最后，会抛出一个 StopIteration 异常。




