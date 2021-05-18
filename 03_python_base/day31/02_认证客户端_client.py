from socket import *
import hmac
import os
import struct


KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024
KEY_SECRET = b'1a2b3c4d5e'


def client_auth(conn):
    """
    认证客户端
    :param conn:
    :return:
    """
    recv_msg = conn.recv(32)
    hmac_md5 = hmac.new(KEY_SECRET, recv_msg)
    digest = hmac_md5.digest()
    conn.sendall(digest)
    result_bytes = conn.recv(4)
    result = struct.unpack("i", result_bytes)
    print("认证返回结果： {}（0:成功，1:失败）".format(result[0]))
    if result[0]:
        return False
    else:
        return True

def client_handle(ip_port, buffer_size):
    """
    处理客户端链接
    :param ip_port:
    :param buffer_size:
    :return:
    """
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(ip_port)
    # 验证客户端是否认证通过
    if not client_auth(client):
        client.close()
        print("客户端认证失败")
        return

    while True:
        inp = input(">>>").strip()
        if not inp:break
        if inp == "quit":break
        client.sendall(inp.encode(KEY_UTF8))
        recv_msg = client.recv(KEY_BUFFER_SIZE)
        print("客户端收到消息：{}".format(recv_msg.decode(KEY_UTF8)))
    client.close()



if __name__ == '__main__':
    client_handle(KEY_IP_PORT, KEY_BUFFER_SIZE)
