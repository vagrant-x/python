import configparser
import os

KEY_NAME = "name"
KEY_PASSWORD = "password"
KEY_DISK_SIZE = "disk_size"
KEY_USED_SIZE = "used_size"

def get_user_data(user):
    """
    查询用户数据，如果用户数据存在，转换为字典的形式返回
    :param user:
    :return:
    """
    config = get_config()
    if user.upper() in config.sections():
        user_upper = user.upper()
        user_data = {
            KEY_NAME: config.get(user_upper, KEY_NAME),
            KEY_PASSWORD: config.get(user_upper, KEY_PASSWORD),
            KEY_DISK_SIZE: config.getint(user_upper, KEY_DISK_SIZE),
            KEY_USED_SIZE: config.getint(user_upper, KEY_USED_SIZE),
        }
        return user_data
    else:
        return None



def set_user_data(user, password, size):
    """
    设置用户
    :param user:
    :param password:
    :param size: 用于拥有的磁盘大小 （单位 m）
    :return:
    """
    config = get_config()
    if user.upper() not in config.sections():
        config.add_section(user.upper())
    config.set(user.upper(), KEY_NAME, user)
    config.set(user.upper(), KEY_PASSWORD, password)
    config.set(user.upper(), KEY_DISK_SIZE, str(size))
    config.set(user.upper(), KEY_USED_SIZE, str(0))
    set_config(config)


def set_config(config):
    """
    保存 config 内容到db.ini 默认db.ini 存在
    :return:
    """
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(root_path, "config")
    filename = os.path.join(config_path, "db.ini")
    config.write(open(filename, 'w'))


def get_config():
    """
    获取config
    config 的数据保存在 config/db.ini 里面，
    如果 config/db.ini 不存在，设置 DEFAULT，创建文件并返回config
    :return:
    """
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(root_path, "config")
    if not os.path.exists(config_path):
        os.mkdir(config_path)
        print("创建新的config文件夹成功")
    filename = os.path.join(config_path , "db.ini")
    if not os.path.isfile(filename):
        print("配置文件 {} 不存在,在 config 文件夹下创建该文件".format(filename))
        config = configparser.ConfigParser()
        config['DEFAULT'] = {KEY_NAME: 'root',
                             KEY_PASSWORD: 'root',
                             KEY_DISK_SIZE: 1024,
                             KEY_USED_SIZE: 0
                             }
        config.write(open(filename, "w"))
        return config
    else:
        print("db.ini 存在")
        config = configparser.ConfigParser()
        config.read(filename)
        return config




if __name__ == '__main__':
    # config = get_config()
    # set_user_data("xu", "124", 100)
    print(get_user_data("xu1"))