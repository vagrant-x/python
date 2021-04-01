print("===== 列表解析=====")
"""
列表解析：
    把一个表达式映射遍一个序列,将其结果收集到一个新的列表并返回。
    
"""
l = [ord(i) for i in "abc"]
print(l)  # [97, 98, 99]

# 1 增加测试
# 输出0-5的偶数
# 通过filter实现
lf = list(filter(lambda x:x %2 == 0, range(5)))
print(lf)  # [0, 2, 4]
# 通过列表解析实现
ll = [x for x in range(5) if x % 2 == 0]
print(ll)  # [0, 2, 4]

#2 列表解析循环嵌套
l = [(x, y) for x in range(3) for y in range(2)]
print(l)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# 嵌套的 for 循环中附加if
l = [(x, y) for x in range(4) if x % 2 == 0 for y in range(2) if y % 2 == 1]
print(l)  # [(0, 1), (2, 1)]