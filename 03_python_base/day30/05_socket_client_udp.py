from socket import *
import subprocess

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BUFFER_SIZE = 1024
KEY_UTF8 = "utf-8"
KEY_GBK = "gbk"
KEY_BACKLOG_SIZE = 3

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    cmd = input(">>>").strip()
    if not cmd: break
    if cmd == "quit":
        break
    udp_client.sendto(cmd.encode(KEY_UTF8), KEY_IP_PORT)
    data, addr = udp_client.recvfrom(KEY_BUFFER_SIZE)
    print(data.decode(KEY_GBK))

udp_client.close()