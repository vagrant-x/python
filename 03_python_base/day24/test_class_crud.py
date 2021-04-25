class Person:
    sex = '男'

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("{} 正在打 {}".format(self.name, ball))

# 查看
print(Person.sex)  # 男

# 修改
Person.sex = "女"
print(Person.sex)  # 女

p1 = Person("xu")
print(p1.__dict__)  # {'name': 'xu'}
print(p1.sex)  # 女

# 增加
Person.nation = "汉"
print(Person.nation)  # 汉

# 删除
del Person.sex
print(Person.__dict__)


##===========方法================
def eat_food(self, food):
    print(" {} 正在吃 {}".format(self.name, food))

# 添加方法
p2 = Person("xu")
Person.eat_food = eat_food
p2.eat_food("潮汕牛肉火锅")  #  xu 正在吃 潮汕牛肉火锅


# ============= 实例属性增删改查 ====================
class Person:
    sex = '男'

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("{} 正在打 {}".format(self.name, ball))

# 查看
p3 = Person("xu3")
print(p3.sex)  # 男

# 增加
p3.age = 18
print(p3.__dict__)  # {'name': 'xu3', 'age': 18}
print(p3.age)  # 18

# 修改
p3.name = "xu_3"
print(p3.name)  # xu_3

# 删除
del p3.name
print(p3.__dict__)  # {'age': 18}