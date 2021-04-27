"""
类的装饰器

"""

#
# def deco(func):
#     print("--------> deco")
#     return func
#
#
# @deco
# def test():
#     print("===> 执行 test")
#
# # test()
#
#
# @deco
# class Foo:
#     pass


def Typed(**kwargs):
    def deco(obj):
        for k, v in kwargs.items():
            setattr(obj, k, v)
        return obj
    return deco


@Typed(x=1, y=2)  # 1、Typed(x=1, y=2) ==> deco   2、@deco ==> Foo = deco(Foo)
class Foo:
    pass


# 通过类装饰器给类添加属性
print(Foo.__dict__)  # {......, 'x': 1, 'y': 2}
print(Foo.x)
