def intNum():
    print("进去生成器函数")
    for i in range(5):
        s = yield i
        print("传入参数为： {}".format(s))


if __name__ == '__main__':
    gen = intNum()
    print("gen = {}".format(gen))

    print(gen.send(None))
    print(gen.send("a"))
    print(gen.send("b"))
    print(gen.send("c"))
    print(gen.send("d"))
    print(gen.send("e"))

