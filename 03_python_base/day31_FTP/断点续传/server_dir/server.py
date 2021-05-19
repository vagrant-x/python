import socketserver
import os
import struct
import json

KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024

KEY_STATUS = "status"
KEY_MSG = "msg"

KEY_OPTION = "option"
KEY_FILE_NAME = "filename"
KEY_FILE_SIZE = "filesize"
KEY_SEND_SIZE = "send_size"


class ServerHandle(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            head = self.recv_head()
            option = head[KEY_OPTION]
            if option == "download_file":
                """
                {
                    option: 请求执行的操作
                    filename: 文件名
                    filesize: 文件大小
                    send_size: 已经发送文件大小
                    msg: 消息
                }
              """
                print("执行下载文件操作")
                filename = head[KEY_FILE_NAME]
                send_size = head[KEY_SEND_SIZE]  # 下载文件已经传输的字节数
                if os.path.exists(filename) and os.path.isfile(filename):
                    filesize = os.path.getsize(filename)
                    if filesize == send_size:
                        statut = -2
                        msg = "下载的文件[{}]已经发送完毕，无需重新下载".format(filename)
                        self.send_status_msg(statut, msg)
                    else:
                        head = {
                            KEY_STATUS: 0,
                            KEY_MSG: "下载文件",
                            KEY_FILE_SIZE: filesize
                        }
                        self.send_head(head)  # 发送头信息
                        with open(filename, "rb") as f:
                            # 默认方式，从文件的其实开始计算字节的位置,并将光标移动 send_size 个字节
                            f.seek(send_size)
                            curr_send_size = send_size
                            while filesize > curr_send_size:
                                msg = f.read(KEY_BUFFER_SIZE)
                                print("读取msg长度: {}".format(len(msg)))
                                self.request.sendall(msg)
                                curr_send_size += len(msg)
                            else:
                                print("文件下载完成")
                else:
                    statut = -1
                    msg = "下载的文件[{}]不存在".format(filename)
                    self.send_status_msg(statut, msg)
            else:
                statut = -1
                msg = "不支持[{}]选项".format(option)
                self.send_status_msg(statut, msg)

    def recv_head(self):
        """
        接收头，并解析为字典
        :return:
        """
        # 接收自定义头长度
        head_length_bytes = self.request.recv(4)
        head_length = struct.unpack("i", head_length_bytes)
        # 接收自定义头并解析
        head_bytes = self.request.recv(head_length[0])
        head_json = head_bytes.decode(KEY_UTF8)
        print("接收的头 {}".format(head_json))
        head_dic = json.loads(head_json)
        return head_dic

    def send_head(self, head):
        """
        封装头，发送
        :param head:
        :return:
        """
        head_json_str = json.dumps(head)
        print("发送头：{}".format(head_json_str))
        head_bytes = head_json_str.encode(KEY_UTF8)
        head_bytes_len = struct.pack("i", len(head_bytes))
        self.request.send(head_bytes_len)
        self.request.send(head_bytes)

    def send_status_msg(self,status, msg):
        data = {
            "status": status,
            "msg": msg
        }
        self.send_head(data)


if __name__ == '__main__':
    print("启动服务。。。")
    address = ("127.0.0.1", 8000)
    ss = socketserver.ThreadingTCPServer(address, ServerHandle)
    ss.serve_forever()