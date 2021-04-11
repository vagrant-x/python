import sys
import os
print("添加前：{}".format(sys.path))
# 如果注释下面两行，将报错 No module named 'module_test1'， 解释器找不到 module_test1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print("添加后：{}".format(sys.path))  # 添加后：[...此次与添加前相同..., 'D:\\08_python\\02_workspace\\resposities\\python_base\\03_python_base\\day21\\module1']
import module_test1
print(module_test1.add(1, 2))  # 3

