# 用户列表
user_list = [
    {'name': 'xu1', 'passwd': '123'},
    {'name': 'xu2', 'passwd': '123'},
    {'name': 'xu3', 'passwd': '123'},
    {'name': 'xu4', 'passwd': '123'},
]
# 当前登录的用户
current_dic = {"username": None, "login": False}


# 验证用户是否登录的装饰器
#   如果用户没有登录，让用户输入账号密码，校验通过记录用户状态
def auth_fun(func):
    def wrapper(*args, **kwargs):
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
    return wrapper


@auth_fun
def index():
    print("this is index")


@auth_fun
def home():
    print("this is home page")


@auth_fun
def shopping_car():
    print("this is shopping car")


index()  # 输入用户密码
home()  # index 已经登录，无需在输入
shopping_car()  # index 已经登录，无需在输入
# 结果：
#     请输入用户名:xu1
#     请输入密码:123
#     this is index
#     this is home page
#     this is shopping car
