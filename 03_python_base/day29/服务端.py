import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # 创建服务器套接字
server.bind(("127.0.0.1", 8000))  # 给套接字绑定地址信息
server.listen(backlog=3)  # backlog 处理创建连接的最大等待数
conn, add = server.accept()  # 接受客户端链接
print("conn = {}, add = {}".format(conn, add))

msg = conn.recv(1024)  # 接收数据
print("服务端接收到的消息：{}".format(msg))
conn.send(msg.upper())  # 发送数据

conn.close()  # 关闭已经创建的连接
server.close()  # 关闭服务器套接字

