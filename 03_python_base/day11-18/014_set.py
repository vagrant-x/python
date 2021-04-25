set
print("test set")

#集合（set）是一个无序的不重复元素序列。
#可以使用大括号 {} 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

#创建集合
print({"1", "2", "3"})  # {'2', '3', '1'}
print(set("123"))  # {'2', '3', '1'}
print(set((1, 2, 3)))  # {1, 2, 3}
print(set([11,22,33]))  # {33, 11, 22}

#add 添加元素到集合
s1 = {"1", "2", "3"}
s1.add("4")
print(s1)  # {'1', '4', '3', '2'}
s1.add("abc")
print(s1)  # {'abc', '1', '4', '2', '3'}

#clear 清空集合中所有元素
s1 = {"1", "2", "3"}
s1.clear()
print(s1)  # set()

#discard 从一个集合中删除指定元素,如果元素不成在,什么都不做
s1 = {"1", "2", "3"}
print(s1.discard("4"))  # None
print(s1)  # {'2', '1', '3'}
print(s1.discard("1"))  # None
print(s1)  # {'2', '3'}

#remove 删除指定元素,如果元素不存在,抛 KeyError
s1 = {"a", "c", "3"}
s1.remove("a")
print(s1)  # {'3', 'c'}
# print(s1.remove("aa"))  # KeyError: 'aa'

#pop 随意返回集合的一个元素,如果集合为空,抛 KeyError
s1 = {"a", "c", "3"}
print(s1.pop())  # 3

#update 根据两个集合的合集,更新自身
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s1.update(s2)
print(s1)  # {'1', 'c', 'a', '3', '2'}

#copy 浅拷贝一个集合
s1 = {"1", "2", "3"}
s2 = s1.copy()
print(s2)  # {'2', '1', '3'}


#difference 差集 返回两个集合的不同元素,原来集合不变
s1 = {"1", "2", "3"}
s2 = {"1", "2", "4"}
print(s1.difference(s2))  # {'3'}
print("差集:", s1-s2)  # 差集: {'3'}

# difference_update 从一个集合中移除与另一个集合相同的元素
s1 = {"1", "2", "3"}
s2 = {"1", "2", "4"}
s1.difference_update(s2)
print(s1)  # {'3'}

#intersection 交集 返回两个集合的交集
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s3 = s1.intersection(s2)
print(s3)
print("交集:", s1 & s2)  # {'2'}

#intersection_update 根据和另一个集合的交集更新自身
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s1.intersection_update(s2)
print(s1)  # {'2'}

#isdisjoint  如果两个集合的交集为空,返回 True,否则返回 Fasle
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s3 = {"a", "b", "c"}
print(s1.isdisjoint(s2))  # False
print(s1.isdisjoint(s3))  # True

#issubset 判断一个集合是否是另一个的子集
s1 = {"a", "c", "3"}
s2 = {"a", "c"}
print(s1.issubset(s2))  # False
print(s2.issubset(s1))  # True

#issuperset 判断一个集合是否包含另一个的子集
s1 = {"a", "c", "3"}
s2 = {"a", "c"}
print(s1.issuperset(s2))  # True
print(s2.issuperset(s1))  # False

#symmetric_difference 交叉补集 返回两个集合的对称差(两个集合中不同部分的合集)
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s3 = s1.symmetric_difference(s2)
print(s3)  # {'1', 'a', 'c', '3'}
print("交叉补集:", s1 ^ s2)  # {'1', 'c', '3', 'a'}

#symmetric_difference_update 两个集合的对称差(两个集合中不同部分的合集),并更新集合
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s1.symmetric_difference_update(s2)
print(s1)  # {'a', '3', 'c', '1'}

#union 合集 返回两个集合的合集
s1 = {"1", "2", "3"}
s2 = {"a", "2", "c"}
s3 = s1.union(s2)
print(s3)  # {'a', '1', 'c', '3', '2'}
print("合集:", s1 | s2)  # {'3', '2', 'c', '1', 'a'}


# 不可变集合
fs = frozenset("python")
print(fs)  # frozenset({'o', 'n', 'y', 'h', 'p', 't'})