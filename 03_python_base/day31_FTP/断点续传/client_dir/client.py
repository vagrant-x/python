import socket
import os
import struct
import json

KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024

KEY_STATUS = "status"
KEY_MSG = "msg"

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_OPTION = "option"
KEY_FILE_NAME = "filename"
KEY_FILE_SIZE = "filesize"
KEY_SEND_SIZE = "send_size"

class Client:

    def __init__(self, address=KEY_IP_PORT, connet=True):
        self.server_address = address
        self.isconnet = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if connet:
            try:
                self.socket.connect(self.server_address)
                self.isconnet = True
            except Exception as e:
                self.socket.close()
                self.isconnet = False
                print("客户端链接异常，关闭客户端。")
                raise

    def recv_head(self):
        """
        接收头，并解析为字典
        """
        # 接收自定义头长度
        head_length_bytes = self.socket.recv(4)
        head_length = struct.unpack("i", head_length_bytes)
        # 接收自定义头并解析
        head_bytes = self.socket.recv(head_length[0])
        head_json = head_bytes.decode(KEY_UTF8)
        head_dic = json.loads(head_json)
        print("客户端接收的数据头 status=[{}], msg=[{}]".format(head_dic[KEY_STATUS], head_dic[KEY_MSG]))
        return head_dic

    def send_head(self, head):
        """
        封装头，发送
        """
        head_json_str = json.dumps(head)
        print("客户端请求数据头：{}".format(head_json_str))
        head_bytes = head_json_str.encode(KEY_UTF8)
        head_bytes_len = struct.pack("i", len(head_bytes))
        self.socket.send(head_bytes_len)
        self.socket.send(head_bytes)

    def run(self):
        if not self.isconnet:
            print("客户端未连接，请重新连接客户端")
            return
        while True:
            try:
                inp = input(">>>").strip()
                print("客户端输入内容：{}".format(inp))
                if not inp: break
                if inp == "quit": break

                cmd_list = inp.split()
                if cmd_list[0] == "get":
                    # 判断客户端文件是否存在
                    filename = cmd_list[1]
                    send_size = 0
                    open_type = "wb"
                    if os.path.exists(filename) and os.path.isfile(filename):
                        send_size = os.path.getsize(filename)
                        open_type = "ab"
                    # 封装请求数据
                    head = {
                        KEY_OPTION: "download_file",
                        KEY_FILE_NAME: filename,
                        KEY_SEND_SIZE: send_size
                    }
                    self.send_head(head)
                    res_head = self.recv_head()
                    if res_head[KEY_STATUS] == 0:
                        filesize = res_head[KEY_FILE_SIZE]
                        recv_size = send_size
                        print("打开文件模式[{}]".format(open_type))
                        with open(filename, open_type) as f:
                            while filesize > recv_size:
                                if filesize - recv_size > KEY_BUFFER_SIZE:
                                    size = KEY_BUFFER_SIZE
                                else:
                                    size = filesize - recv_size
                                msg = self.socket.recv(size)
                                f.write(msg)
                                recv_size += len(msg)
                                print("当前文件长度: {}".format(recv_size))
                        print("文件下载成功")
                    else:
                        print("下载失败，返回信息：{}".format(str(res_head)))
                else:
                    print("客户端暂时不支持[{}]操作".format(cmd_list[0]))

            except Exception as e:
                self.socket.close()
                raise
        self.socket.close()



if __name__ == '__main__':
    print("启动客户端。。。")
    client = Client(KEY_IP_PORT)
    client.run()
