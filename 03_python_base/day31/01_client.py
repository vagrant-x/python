from socket import *

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_UTF8 = "utf-8"
KEY_GBK = "gbk"
KEY_BUFFER_SIZE = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(KEY_IP_PORT)

while True:
    # 发送
    msg = input(">>>").strip()
    if not msg: break
    if msg == "quit":
        break
    tcp_client.send(msg.encode(KEY_UTF8))
    # 接收
    recv_msg = tcp_client.recv(KEY_BUFFER_SIZE)
    print(recv_msg.decode(KEY_UTF8))
tcp_client.close()
