import pymongo

# 获取连接 mongodb 对象，默认端口：27017
client = pymongo.MongoClient("127.0.0.1", port=27017)

# 获取数据库（如果没有test这个数据库也没关系）
db = client.test

# 获取数据库中的集合（也就是 mysql 中的表）
collection = db.qa


# 1、insert_one 加入一条文档数据到集合中
collection.insert_one({"username":"aaa"})

# 2、insert_many: 加入多条文档数据到集合中
collection.insert_many([{"username":"a2"},{"username":"a1"}])


# 3、find_one: 查找一条文档对象
res = collection.find_one()
print(res)  # {'_id': ObjectId('60bb6e2151ee3420356af4f0'), 'username': 'aaa'}

# 4、find ： 查找所有文档对象
cursor = collection.find()
print(res)  # <pymongo.cursor.Cursor object at 0x000001F7FEE62BA8>
for d in cursor:
    print(d)


# 5、update_one: 更新一条文档对象
collection.update_one({"username":"a1"}, {"$set":{"username":"a1", "age":18}})

# 6、update_many: 更新多条文档对象
collection.update_many({"username":"a1"}, {"$set":{"username":"a1", "age":18}})


# 7、delete_one: 删除一条文档对象
# collection.delete_one({"username":"a1", "age":18})

# 8、delete_many: 删除多条文档对象
# collection.delete_many({"username":"aaa"})
