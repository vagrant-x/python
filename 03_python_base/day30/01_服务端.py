from socket import *

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_BUFFER_SIZE = 1024
KEY_UTF8 = "utf-8"

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(KEY_IP_PORT)
tcp_server.listen(KEY_BACKLOG)

while True:
    print("服务端开始运行>>>")
    conn, addr = tcp_server.accept()
    while True:
        try:
            data = conn.recv(KEY_BUFFER_SIZE)
            print("服务接收到数据：{}".format(data.decode(KEY_UTF8)))
            conn.send("server return: <{}>".format(data.decode(KEY_UTF8)).encode(KEY_UTF8))
        except Exception:
            break
    conn.close()

tcp_server.close()

