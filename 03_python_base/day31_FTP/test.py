import sys

def auth1(**data):
    print(type(data))
    print(data)

def auth2(data):
    print(type(data))
    print(data)


if __name__ == '__main__':
    data = {"a": 1, "b": 2 }
    auth1(**data)
    auth2(data)
