from socket import *
import struct

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_UTF8 = "utf-8"
KEY_GBK = "gbk"
KEY_BUFFER_SIZE = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(KEY_IP_PORT)

while True:
    # 发送
    cmd = input(">>>").strip()
    if not cmd: break
    if cmd == "quit":
        break
    tcp_client.send(cmd.encode(KEY_UTF8))
    # 接收
    length_res = tcp_client.recv(4)
    length = struct.unpack("i", length_res)[0]
    res = tcp_client.recv(length)
    print(res.decode("gbk"))
tcp_client.close()
