# 用户列表
user_list = [
    {'name': 'xu1', 'passwd': '123'},
    {'name': 'xu2', 'passwd': '123'},
    {'name': 'xu3', 'passwd': '123'},
    {'name': 'xu4', 'passwd': '123'},
]
# 当前登录的用户
current_dic = {"username": None, "login": False}

"""
    注意：带参数的装饰器会比没有带参数的装饰器多嵌套一层函数（多了auth）
        调用方式是 @auth(auth_type="type1")， 返回 auth_fun，
        也就是说 @auth(auth_type="type1")相当于 @auth_fun
        但是 auth_fun 函数所在的嵌套作用域多了一个 auth_type 的变量
"""
def auth(auth_type="type1"):
    def auth_fun(func):
        def wrapper(*args, **kwargs):
            if auth_type == "type1":
                if current_dic["username"] and current_dic['login']:
                    res = func(*args, **kwargs)
                    return res
                username = input("请输入用户名:")
                pw = input("请输入密码:")
                for u in user_list:
                    if u["name"] == username and u["passwd"] == pw:
                        current_dic["username"] = username
                        current_dic["login"] = True
                        res = func(*args, **kwargs)
                        return res
                else:
                    print("用户没有注册！")
            elif auth_type == "type2":
                print("不用授权直接登录: type = {}".format(auth_type))
                res = func(*args, **kwargs)
                return res
            else:
                print("其他type没有实现")
        return wrapper
    return auth_fun


"""
    auth_fun = @auth(auth_type="type1") 
    auth_fun 所在的嵌套与将有一个 auth_type 变量
    然后通过 @auth()方法返回的对象注解 index,相当于 @auth_fun 注解index 方法，最后得到 wrapper 对象
"""
@auth(auth_type="type1")
def index():
    print("this is index")


@auth(auth_type="type2")
def home():
    print("this is home page")


@auth(auth_type="type3")
def shopping_car():
    print("this is shopping car")


home()  # 注意：auth_type="type2"，这个方法无需登录可以直接执行
index()  # 注意：auth_type="type1"，需要登录
shopping_car()  # 注意：auth_type="type3"，没有做处理
# 结果：
#     不用授权直接登录: type = type2
#     this is home page
#     请输入用户名:xu1
#     请输入密码:123
#     this is index
#     其他type没有实现
