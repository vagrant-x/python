from socket import *
import subprocess

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BUFFER_SIZE = 1024
KEY_UTF8 = "utf-8"
KEY_GBK = "gbk"
KEY_BACKLOG_SIZE = 3

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(KEY_IP_PORT)

while True:
    try:
        cmd, addr = udp_server.recvfrom(KEY_BUFFER_SIZE)

        res = subprocess.Popen(cmd.decode(KEY_UTF8), shell=True,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        err_res = res.stderr.read()
        if err_res:
            cmd_res = err_res
        else:
            cmd_res = res.stdout.read()

        if not cmd_res:
            cmd_res = "执行成功".encode("gbk")
        print("length = {}".format(len(cmd_res)))
        udp_server.sendto(cmd_res, addr)
    except Exception as e:
        print(e)
        break

udp_server.close()

"""
证明 upd 不会出现粘包现象：
    在windows 上测试，报错： 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
    在 ubuntu 上测试，服务端返回2559 个字节，但是客户端只从数据报中拿了1024个并打印出来   
"""