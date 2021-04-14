"""
random 模块
    返回随机生成的实数
"""
import random

print(random.random())  # 随机返回 0 到 1 之间的浮点数 例如：0.5072104946318795
print(random.randint(1, 10))  # 随机返回 1 到 10 (包含10) 之间的整数 例如：6
print(random.randrange(1, 10))  # 随机返回 1 到 10 （不包含10） 之间的整数 例如：3
print(random.choice(["a", "b", "c"]))  # 随机从列表中选取一个元素返回 例如 b
print(random.sample(("a", "b", "c", 1, 2, 3), 2))  # 更加指定返回数量，从传入对象中随机选取元素，以列表返回， 例如： [3, 'b']
print(random.uniform(1.1, 5))  # 产生指定区间的浮点数 例如 2.7892068065251006

a = [1, 2, 3, 4, 5, 6]
random.shuffle(a)  # 将原来列表的顺序打乱，
print(a)  # 例如 [1, 5, 2, 6, 3, 4]

# 通过random 生成指定长度的验证码（存在数字和大写字母）
import random
def v_code(len):
    res = ""
    for i in range(len):
        num = str(random.randint(0, 9))
        alf = chr(random.randint(65, 90))
        sub = random.choice((num, alf))
        res += sub
    return res
print(v_code(4))  # 例如 28AR