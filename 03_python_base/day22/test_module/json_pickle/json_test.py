"""
json 模块
    用eval内置方法可以将一个字符串转成python对象，不过，eval方法是有局限性的，对于普通的数据类型，json.loads和eval都能用，
    但遇到特殊类型的时候，eval就不管用了,所以eval的重点还是通常用来执行一个字符串表达式，并返回表达式的值。

序列号
    把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
    反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

json
    如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
    比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
    JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

"""
import json

dic = {'name': 'xu', "age": 18}
dic_json = json.dumps(dic)
print(type(dic_json))  # <class 'str'>
# 注意: json序列号后，所有的 单引号 变成 双引号
print(dic_json)  # {"name": "xu", "age": 18}

# 将序列化后的字符串写入文件
with open("json_file", "w") as wirte_f:
    wirte_f.write(dic_json)   #-------------------等价于json.dump(dic, wirte_f)


# 将文件中的内容读取出来并反序列化
with open("json_file", "r") as read_f:
    dic_str = read_f.read()
print(dic_str)

dic = json.loads(dic_str)  # {"name": "xu", "age": 18}   #-------------------等价于 dic = json.dump(dic, read_f)
print(dic["name"])  # xu



# ====================== pickle ==========================
"""
pickle 模块
    Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python
"""
import pickle

dic = {'name': 'xu', "age": 18}
dic_bytes = pickle.dumps(dic)
print(type(dic_bytes))  # <class 'bytes'>
print(dic_bytes)  # b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x02xu\x94\x8c\x03age\x94K\x12u.'

# 将 pickle 序列号的对象写入文件
with open("pickle_json", "wb") as write_f:
    write_f.write(dic_bytes)  #------------------- 等价于pickle.dump(dic,write_f)


# 从 pickle_json 文件中读取内容反序列化
with open("pickle_json", "rb") as read_f:
    dic_bytes = read_f.read()

dic = pickle.loads(dic_bytes) #------------------- 等价于data=pickle.load(read_f)
print(dic["name"])  # xu
