import socketserver

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_BACKLOG = 3
KEY_UTF8 = "utf-8"
KEY_BUFFER_SIZE = 1024

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("conn is :{}".format(self.request))
        print("addr is :{}".format(self.client_address))

        while True:
            try:
                # 接收数据
                data = self.request.recv(KEY_BUFFER_SIZE)
                if not data: break  # 客户端端口链接有可能一直返回 b""
                print("服务端接收到{}的数据：{}".format(self.client_address, data))
                # 发送数据
                self.request.sendall("服务返回数据<{}>".format(data).encode(KEY_UTF8))
            except Exception as e:
                print(e)
                break


if __name__ == '__main__':
    print("启动服务。。。")
    s = socketserver.ThreadingTCPServer(KEY_IP_PORT, MyServer)  # 多线程
    # s = socketserver.ForkingTCPServer(KEY_IP_PORT, MyServer)  # 多进程
    s.serve_forever()
    print("关闭服务。。。")