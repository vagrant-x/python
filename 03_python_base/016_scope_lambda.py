print(" test scope , lambda ")

# scope

name = "xu_glpbal"
def foo():
    name = "xu_foo"
    def bar():
        name = "xu_bar"
        def tt():
            print(name)
        return tt
    return bar
bar = foo()
tt = bar()
tt()  # xu_bar

# ================== lambda ==================
# 匿名函数和普通函数的对比
def sum_func(a, b, c):
    return a + b + c
# 将匿名函数对象赋值给 sum_lambda
sum_lambda = lambda a, b, c: a + b + c
print(sum_func(1, 2, 3))  # 6
print(sum_lambda(1, 2, 3))  # 6


# 匿名函数的多种形式
# 无参数
lambda_a = lambda :100
print(lambda_a())  # 100

# 一个参数
lambda_b = lambda num: num * 10
print(lambda_b(1))  # 10

# 多个参数
lambda_c = lambda a, b, c: a + b + c
print(lambda_c(1, 10, 100))  # 111

# 表达式分支
lambda_d = lambda x: x if x > 5 else x + 1
print(lambda_d(4))  # 5
print(lambda_d(6))  # 6


# lambda 作为一个参数传递
def sub_func(a, b, func):
    print("a = ", a)
    print("b = ", b)
    print("a - b = ", func(a, b))
sub_func(3, 2, lambda a, b: a - b)
# 结果：
#     a =  3
#     b =  2
#     a - b =  1


# lambda函数与python内置函数配合使用

#sorted是Python中对列表排序的内置函数，我们使用lambda来获取排序的key
member_list = [
    {"price": 9},
    {"price": 999},
    {"price": 99}
]
new_list = sorted(member_list, key=lambda dict_: dict_["price"])
print(new_list)  #  [{'price': 9}, {'price': 99}, {'price': 999}]


number_list = [100, 77, 69, 31, 44, 56]
num_sum = list(map(lambda x: {str(x): x}, number_list))
print(num_sum)  # [{'100': 100}, {'77': 77}, {'69': 69}, {'31': 31}, {'44': 44}, {'56': 56}]
# map是Python中用来做映射的一个内置函数，接收两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象，map会遍历可迭代对象的值，然后将值依次传递给函数执行。我们使用lambda来实现map中的函数参数。


# lambda 作为函数的返回值
def discount_func(discount):
    return lambda price: discount * price

p = discount_func(0.8)
print(p)  # <function discount_func.<locals>.<lambda> at 0x00000241352BAC10>
print(p(100))  # 80.0
# 匿名函数可以作为一个函数的返回值，上面函数discount_func返回一个设定了折扣的匿名函数对象，调用这个对象，传入价格，就可以得到折扣后的价格



