import os


def get_root_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# if __name__ == '__main__':
#     print(get_root_path())
