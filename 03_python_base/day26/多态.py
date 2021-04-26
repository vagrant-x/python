"""
多态
    多态：由不同的类实例化得到的对象，调用同一个方法，执行的逻辑不同。
    多态的概念指出了对象如何通过他们共同的属性和动作来操作以及访问，而不需要考虑他们的具体类。
    多态表明了动态（运行时）绑定的存在，允许重载及运行时类型确定和验证。

"""


class H2O:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def turn(self):
        if self.temperature < 0:
            print("[{}]温度太低结冰了".format(self.name))
        elif 0 <= self.temperature < 100:
            print("[{}]液化变成水".format(self.name))
        elif self.temperature >= 100:
            print("[{}]温度太高变成水蒸气".format(self.name))


class Water(H2O):
    pass


class Ice(H2O):
    pass


class Steam(H2O):
    pass


w = Water("水", 40)
i = Ice("冰", -4)
s = Steam("水蒸气", 110)

# w.turn()
# i.turn()
# s.turn()


# 不同实例调用相同的方法，执行不同的行为
def turn(obj):
    obj.turn()


turn(w)
turn(i)
turn(s)


