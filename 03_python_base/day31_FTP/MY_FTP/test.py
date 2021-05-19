import os


list = ["home", "dir1", "dir2"]
print(os.path.join(*list))

print(os.listdir(os.getcwd()))