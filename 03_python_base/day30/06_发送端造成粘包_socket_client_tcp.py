from socket import *

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_UTF8 = "utf-8"
KEY_GBK = "gbk"
KEY_BUFFER_SIZE = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(KEY_IP_PORT)

tcp_client.send("123".encode(KEY_UTF8))
tcp_client.send("abc".encode(KEY_UTF8))
tcp_client.send("ABC".encode(KEY_UTF8))