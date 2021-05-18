import socket
import struct

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024


class FTPClient:

    def __init__(self, user, password, address=KEY_IP_PORT, connet=True):
        self.server_address = address
        self.user = user
        self.password = password
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if connet:
            try:
                self.client_connet()
            except Exception as e:
                self.client_close()
                print("客户端链接异常，关闭客户端。")

    def client_connet(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        # 验证客户端是否有权限登陆

        # 登录成功后才能进行输入操作
        while True:
            try:
                inp = input(">>>").strip()
                if not inp: break
                if inp == "quit": break

                args_list = inp.split()
                cmd = args_list[0]
                if cmd == "put":
                    self.upload_file(args_list)
                elif cmd == "get":
                    self.download_file(args_list)
                elif cmd == "cd" or cmd == "ls":
                    self.send_cmd(inp)
                else:
                    print("该命令暂时不支持")
            except Exception as e:
                print(e)
                self.client_close()
                break
        self.client_close()

    def send_cmd(self, cmd):
        """
        发送需要执行的命令
        :param cmd: 客户端启动成功后输入的命令
        :return:
        """
        pass

    def upload_file(self, args):
        """
        根据用户指定的文件执行上传操作
        :param args:
        :return:
        """
        pass

    def download_file(self, args):
        """
        根据用户指定的文件执行下载操作
        :param args:
        :return:
        """
        pass

    def client_auth(self):
        """
        客户端认证方法
        :return:
        """
        pass


if __name__ == '__main__':
    print("启动客户端。。。")
    client = FTPClient(KEY_IP_PORT)
    client.run()
