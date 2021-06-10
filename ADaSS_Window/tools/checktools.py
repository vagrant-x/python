import re


def check_ip(ip_str):
    """
    检查传入ip是否正确
    :param ip_str:
    :return:
    """
    res = re.fullmatch(r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)($|(?!\.$)\.)){4}$", ip_str)
    return True if res else False


def check_vid_pid(vid_pid):
    """
    检查传入 vid_pid 是否正确
    :param vid_pid:
    :return:
    """
    res = re.fullmatch(r"\w{4}:\w{4}", vid_pid)
    return True if res else False


if __name__ == '__main__':
    # print(check_ip("10.8.1.256"))
    print(check_vid_pid("w23D:12va"))