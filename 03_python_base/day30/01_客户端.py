from socket import *

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BUFFER_SIZE = 1024
KEY_UTF8 = "utf-8"

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(KEY_IP_PORT)

while True:
    msg = input(">>>").strip()
    if not msg: continue
    print("客户端发送数据：{}".format(msg))
    tcp_client.send(msg.encode(KEY_UTF8))
    ret_msg = tcp_client.recv(KEY_BUFFER_SIZE)
    print("客户端接收到的数据：{}".format(ret_msg.decode(KEY_UTF8)))

tcp_client.close()
