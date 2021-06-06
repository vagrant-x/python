# import pymysql
#
# # 设置连接数据库参数
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# cursor.execute("select 1")  # 设置查询对象
# data = cursor.fetchone()  # 获取查询数据
# print(data)
# cursor.close()  # 关闭数据库连接


# # 插入数据
# import pymysql
#
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# sql = """
# insert into user(id, username, age, password) values (null, 'ddd', 21, "444444")
# """
# cursor.execute(sql)  # 执行sql语句
# db.commit()  # 提交数据
# db.close()  # 关闭数据库


# # fetchone
# import pymysql
#
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# sql = """
# select * from user
# """
# cursor.execute(sql)
# result = cursor.fetchone()  # 获取一条数据
# print(result)
# cursor.close()
# db.close()


# fetchall
# import pymysql
#
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# sql = """
# select * from user where id < 4
# """
# cursor.execute(sql)
# result = cursor.fetchall()  # 获取所有满足条件的数据
# print(result)  #
# cursor.close()
# db.close()



# # fetchmany
# import pymysql
#
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# sql = """
# select * from user where id < 4
# """
# cursor.execute(sql)
# result = cursor.fetchmany(2)  # 获取所有满足条件的数据
# print(result)  #
# cursor.close()
# db.close()


# # delete data
# import pymysql
#
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# sql = """
# delete from user where id = 4
# """
# cursor.execute(sql)
# db.commit()
# db.close()


# delete data
# import pymysql
#
# db = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="root",
#     database="xhkdb",
#     port=3306
# )
# cursor = db.cursor()
# sql = """
# update user set username="AAA" where id = 1
# """
# cursor.execute(sql)
# db.commit()
# db.close()

def test(a:int, b:str) -> str:

    print(a, b)
    return 1000

if __name__ == '__main__':
    res = test('test', 'abc')
    print(type(res))