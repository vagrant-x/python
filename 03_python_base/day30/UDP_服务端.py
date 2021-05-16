from socket import *

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_UTF8 = "utf-8"
KEY_BUFFER_SIZE = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)  # 创建一个服务器的套接字
udp_server.bind(KEY_IP_PORT)  # 绑定ip和地址

print("UDP SERVER ...")
while True:
    data, addr = udp_server.recvfrom(KEY_BUFFER_SIZE)  # 接收消息
    print("data = {}, addr = {}".format(data.decode(KEY_UTF8), addr))
    res_msg = "UDP SERVER return:<{}>".format(data.decode(KEY_UTF8)).encode(KEY_UTF8)
    udp_server.sendto(res_msg, addr)  # 发送消息

udp_server.close()  # 关闭服务器套接字

