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

data1 = conn.recv(15)
print("data1 = {}".format(data1))
data2 = conn.recv(15)
print("data2 = {}".format(data2))
data3 = conn.recv(15)
print("data3 = {}".format(data3))

"""
理想接收
data1 = b'123'
data2 = b'abc'
data3 = b'ABC'

服务端每次接收5个字节的情况（之一）：
    data1 = b'123ab'
    data2 = b'cABC'
    data3 = b''
    
服务端每次接收15个字节的情况（之一）：
    data1 = b'123abc'
    data2 = b'ABC'
    data3 = b''

    data1 = b'123abcABC'
    data2 = b''
    data3 = b''
"""