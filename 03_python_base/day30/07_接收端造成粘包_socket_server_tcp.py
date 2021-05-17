from socket import *
import subprocess

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_UTF8 = "utf-8"
KEY_BUFFER_SIZE = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(KEY_IP_PORT)
tcp_server.listen(KEY_BACKLOG)

conn, addr = tcp_server.accept()

data1 = conn.recv(1)
print("data1 = {}".format(data1))
data2 = conn.recv(2)
print("data2 = {}".format(data2))
data3 = conn.recv(3)
print("data3 = {}".format(data3))

"""
服务端获取结果（由于客户端第一次发送的数据大于第一次接收的数据，导致数据残留）：
    data1 = b'1'
    data2 = b'23'
    data3 = b'abc'
    
"""