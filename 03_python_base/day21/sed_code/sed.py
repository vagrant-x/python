# 查询文件中数据方法
def file_handler(backend_data):
    res = []
    with open("haproxy.conf", "r") as read_f:  # 使用读权限打开文件
        tag = False
        for readline in read_f:  # 遍历文件每一行
            if readline == backend_data:
                tag = True
                continue
            if tag and readline.startswith("backend"):
                break
            if tag:
                print(readline, end="")
                res.append(readline)
    return res

# 修改文件数据方法
def file_change_handler(backend_data, res):
    tag = False
    with open("haproxy.conf", "r") as read_f, \
            open("haproxy.conf.bak", "w") as write_f:  # 打开文件
        for readline in read_f:
            if backend_data == readline:
                res.insert(0, backend_data)  # 把backend 插入到第一个位置
                write_f.writelines(res)  # 将列表所有数据一次性写入文件
                tag = True
                continue
            if tag and readline.startswith("backend"):
                tag = False
            if not tag:
                write_f.write(readline)
    # # 打开代码，相当于修改文件操作
    # import os
    # os.remove("haproxy.conf")
    # os.rename("haproxy.conf.bak", "haproxy.conf")


# 查询
def fetch(data):
    print("\033[1;10m这是查询方法，输入的数据\033[0m data = {}".format(data))
    backend_data = "backend {}\n".format(data)
    res = file_handler(backend_data)
    return res

# 添加
def add():
    pass

# 修改
def change(data):
    print("这是change函数，data = {}".format(data))
    backend = data[0]["backend"]
    format_str = "{0}server {1} {1} weight {2} maxconn {3}\n"  # 根据文件要求格式拼接数据
    old_server_record = format_str.format(" "*8, data[0]['record']['server'],
                                        data[0]['record']['weight'], data[0]['record']['maxconn'])
    new_server_record = format_str.format(" "*8, data[1]['record']['server'],
                                        data[1]['record']['weight'], data[1]['record']['maxconn'])
    print("用户想要修改的记录是：{}".format(old_server_record))
    res = fetch(backend)
    print("change 查询结果：{}".format(res))
    if not res or old_server_record not in res:
        print("寻找的数据不存在")
    else:
        index = res.index(old_server_record)  # 找到旧数据在列表中索引
        res[index] = new_server_record  # 修改为新数据
        backend_data = "backend {}\n".format(backend)
        file_change_handler(backend_data, res)
        print("修改完成")

# 删除
def delete():
    pass


msg = """
    1: 查询
    2：添加
    3：修改
    4：删除
    5：退出
    """
msg_dic = {
    "1": fetch,
    "2": add,
    "3": change,
    "4": delete,
}

if __name__ == '__main__':
    while True:
        print(msg)
        choice = input("请输入下一步操作：").strip()
        if not choice:
            continue
        if choice == "5":
            break
        data = input("请输入你的数据：").strip()
        if choice != "1":
            data = eval(data)
        res = msg_dic[choice](data)  # 根据选择的数据调用对应方法
        print("最终结果：{}".format(res))

# [{'backend':'www.oldboy1.org','record':{'server':'2.2.2.4','weight':20,'maxconn':3000}},{'backend':'www.oldboy1.org','record':{'server':'2.2.2.5','weight':30,'maxconn':4000}}]

