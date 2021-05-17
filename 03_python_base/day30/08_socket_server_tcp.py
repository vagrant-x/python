from socket import *
import subprocess
import struct

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_UTF8 = "utf-8"
KEY_BUFFER_SIZE = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(KEY_IP_PORT)
tcp_server.listen(KEY_BACKLOG)

while True:
    conn, addr = tcp_server.accept()
    print("服务端接收到的请求的addr = {}".format(addr))

    while True:
        try:
            cmd = conn.recv(KEY_BUFFER_SIZE)
            if not cmd: break
            print("执行命令：{}".format(cmd.decode(KEY_UTF8)))

            # 执行命令，得到命令执行结果
            res = subprocess.Popen(cmd.decode(KEY_UTF8), shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            err_res = res.stderr.read()
            if err_res:
                cmd_res = err_res
            else:
                cmd_res = res.stdout.read()

            # 返回命令执行结果
            if not cmd_res:
                cmd_res = "执行成功".encode(KEY_UTF8)
            cmd_length = len(cmd_res)
            cmd_length_b = struct.pack("i", cmd_length)  # 将返回内容的长短转换成4个字节的形式
            conn.send(cmd_length_b)  # 将长度先发送
            conn.send(cmd_res)
        except Exception as e:
            print("出现异常： {}".format(e))
            break
    conn.close()
    print("addr = {} 退出链接".format(addr))
