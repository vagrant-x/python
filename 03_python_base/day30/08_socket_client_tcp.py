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

    recv_size = 0
    recv_msg = b''
    while recv_size < length:
        # 判断剩下的是否大于 1024，如果小于1024， 按照实际接收
        if length - recv_size >= KEY_BUFFER_SIZE:
            recv_msg += tcp_client.recv(KEY_BUFFER_SIZE)
        else:
            recv_msg += tcp_client.recv(length - recv_size)
        recv_size = len(recv_msg)
    print(recv_msg.decode("gbk"))
    print("length = {}".format(recv_size))
tcp_client.close()
