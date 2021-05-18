import os
import socketserver
import struct
import json

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024


class MyHandle(socketserver.BaseRequestHandler):

    SERVER_DIR = "upload_files"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def handle(self):
        # 接收自定义头长度
        head_length_bytes = self.request.recv(4)
        head_length = struct.unpack("i", head_length_bytes)
        # 接收自定义头并解析
        head_bytes = self.request.recv(head_length[0])
        head_json = head_bytes.decode(KEY_UTF8)
        print(head_json)
        head_dic = json.loads(head_json)

        # 判断是否支持该操作
        cmd = head_dic["cmd"]
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            func(head_dic)

    def put(self, head_dic):
        upload_dir = os.path.normpath(os.path.join(self.BASE_DIR, self.SERVER_DIR))
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)
            print("创建文件夹：{}".format(upload_dir))
        # 获取文件名并拼接全路径
        filename = head_dic['filename']
        filename = os.path.normpath(os.path.join(self.BASE_DIR,
                                                 self.SERVER_DIR,
                                                 filename))
        # 获取文件大小并保存文件
        filesize = head_dic["filesize"]
        recv_size = 0
        with open(filename, 'wb') as f:
            while filesize > recv_size:
                if filesize - recv_size > KEY_BUFFER_SIZE:
                    size = KEY_BUFFER_SIZE
                else:
                    size = filesize - recv_size
                recv_msg = self.request.recv(size)
                # recv_size += size
                recv_size += len(recv_msg)
                f.write(recv_msg)
                print("recv_size = {}, realsize = {}".format(recv_size, len(recv_msg)))


if __name__ == '__main__':
    print("启动FTP服务。。。")
    s = socketserver.ThreadingTCPServer(KEY_IP_PORT, MyHandle)
    s.serve_forever()
