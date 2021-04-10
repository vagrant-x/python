def father(name):
    print("father name: %s" % name)
    def son():
        print("son name: %s" % name)
    son()
father("xu1")

# 结果：
#     father name: xu1
#     son name: xu1