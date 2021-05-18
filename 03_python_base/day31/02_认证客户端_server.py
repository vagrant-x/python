from socket import *
import hmac
import struct
import os


KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024
KEY_SECRET = b'1a2b3c4d5e'


def conn_auth(conn):
    """
    检查链接是否合法
    :param conn:
    :return:
    """
    print("开始认证客户端链接。。。")
    msg = os.urandom(32)
    conn.sendall(msg)
    hmac_md5 = hmac.new(KEY_SECRET, msg)  # 第三个参数digestmod默认md5
    digest = hmac_md5.digest()
    respone = conn.recv(len(digest))
    flag = hmac.compare_digest(digest, respone)
    if flag:
        result_bytes = struct.pack("i", 0)  # 认证成功，发送0
    else:
        result_bytes = struct.pack("i", 1)  # 认证成功，发送1
    conn.sendall(result_bytes)  # 发送认证结果给客户端
    return flag


def data_handle(conn, buffer_size=1024):
    """
    处理链接数据传输
    :param conn:
    :param buffer_size:
    :return:
    """
    if not conn_auth(conn):
        print("客户端认证失败，关闭链接")
        conn.close()
        return
    while True:
        try:
            recv_msg = conn.recv(buffer_size)
            if not recv_msg:
                break
            conn.send("服务端返回信息：<{}>".format(recv_msg.decode(KEY_UTF8)).encode(KEY_UTF8))
        except Exception as e:
            print(e)
            break


def server_handle(ip_port, buffer_size, backlog=5):
    """
    处理连接请求
    :param ip_port:
    :param buffer_size:
    :param backlog:
    :return:
    """
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ip_port)
    server.listen(backlog)

    while True:
        conn, addr = server.accept()
        print("新链接客户端：{}".format(addr))
        data_handle(conn, buffer_size)


if __name__ == '__main__':
    print("启动服务端。。。")
    server_handle(KEY_IP_PORT, KEY_BUFFER_SIZE, KEY_BACKLOG)
