"""
__getattribute__
    查找属性的时候，都会先执行__getattribute__，如果调用 __getattribute__ 找不到属性，默认抛出 AttributeError
    解释器捕获 AttributeError 并转而调用 __getattr__
"""
class Foo:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, item):
        print("===> getattr : {}".format(item))

    def __getattribute__(self, item):
        print("===> getattribute : {}".format(item))
        raise AttributeError("[{}] 不存在".format(item))

f = Foo(100)

# 没有重写 __getattr__ 和 __getattribute__
print(f.x)  # 100
print(f.x1)  # AttributeError: 'Foo' object has no attribute 'x1'

# 重写 __getattr__ 和 __getattribute__
print(f.x1)
# 结果：
#     ===> getattribute : x1
#     ===> getattr : x1
#     None
