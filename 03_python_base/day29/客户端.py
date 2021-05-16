import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建客户端套接字

client.connect(("127.0.0.1", 8000))  # 尝试连接服务器

client.send("hello".encode("utf-8"))  # 发送数据

data = client.recv(1024)  # 接收数据
print("客户端接收到的消息：{}".format(data))

client.close()  # 关闭客户端套接字
