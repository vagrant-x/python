class Person:
    sex = '男'

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("{} 正在打 {}".format(self.name, ball))

# 如果实例中没有添加属性，将会到类中查找，
# 在执行 p1.sex = "女" 之前，查找p1.sex ，在实例中找不到，到 class中查找
# 在执行 p1.sex = "女" 之后，在实例的作用域中有 sex 这个属性，并且不会影响到类的sex属性
p1 = Person("xu1")
print(p1.sex)  # 男
p1.sex = "女"
print("类：{}".format(Person.sex))  # 类：男
print("实例：{}".format(p1.sex))  # 实例：女
print(p1.__dict__)  # {'name': 'xu1', 'sex': '女'}



counter = "China"
class Person:
    sex = '男'

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("{} 正在打 {}".format(self.name, ball))

# 实例中寻找 counter,并没有找到；再到类中寻找 counter 也没有该属性
p2 = Person("xu2")
print(p2.counter)  # AttributeError: 'Person' object has no attribute 'counter'



counter = "China——-----------module"
class Person:
    sex = '男'
    counter = "China----------- class"
    def __init__(self, name):
        self.name = name
        print("__init___ {}".format(counter))  # __init___ China——-----------module

    def play_ball(self, ball):
        print("{} 正在打 {}".format(self.name, ball))

# print("__init___ {}".format(counter)) 中的 counter 并不是 实例或是类中的属性，
# 在 init 中没有定义，会到定义类的作用域中寻找，找到module 中定义的 counter
print(Person.__dict__)
print(Person.counter)  # China----------- class
p3 = Person("xu3")
print(p3.counter)  # China----------- class


class Person:
    sex = '男'
    cards = ["card1", "card2"]

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("{} 正在打 {}".format(self.name, ball))

p4 = Person("xu4")
print(p4.cards)  # ['card1', 'card2']

# p4.cards = ["c1", "c2", "c3"]
# print(p4.__dict__)  # {'name': 'xu4', 'cards': ['c1', 'c2', 'c3']}
# print(Person.cards)  # ['card1', 'card2']

# 修改实例属性 cards，属性来自类作用域，如果该属性是可变的，修改的效果将作用于类属性
p4.cards.append("new_card")
print(p4.__dict__)  # {'name': 'xu4'}
print(Person.cards)  # ['card1', 'card2', 'new_card']