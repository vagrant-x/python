import os
import hashlib

def get_file_md5(filename):
    if not os.path.exists(filename):
        return None
    md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for line in f:
            md5.update(line)
    return md5.hexdigest()



if __name__ == '__main__':
    print(get_file_md5("system_tools.py"))