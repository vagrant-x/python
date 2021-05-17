from socket import *

KEY_IP_PORT = ("127.0.0.1", 8000)
KYE_UTF8 = "utf-8"
KYE_BUFFER_SIZE = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)  # 创建客户端套接字

while True:
    msg = input(">>>").strip()
    udp_client.sendto(msg.encode(KYE_UTF8), KEY_IP_PORT)  # 发送消息
    data, addr = udp_client.recvfrom(KYE_BUFFER_SIZE)  # 接收消息
    print("NTP 返回时间：{}".format(data.decode(KYE_UTF8)))

udp_client.close()  # 关闭套接字

