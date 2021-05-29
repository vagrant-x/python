import socket
import sys
import os

BADE_DIR = os.path.dirname(os.path.abspath(__file__))


class SelectFtpClient:
    def __init__(self):
        self.argv = sys.argv
        if len(self.argv) > 2:
            self.addr = (self.argv[1], int(self.argv[2]))
        else:
            self.addr = ("127.0.0.1", 8080)
        self.create_socket()
        self.command_fanout()

    def create_socket(self):
        try:
            self.socket = socket.socket()
            self.socket.connect(self.addr)
            print("连接FTP服务器成功")
        except Exception as e:
            print("连接FTP服务器出现异常：{}".format(e))

    def command_fanout(self):
        while True:
            inp = input(">>>").strip()
            if inp == "exit": break
            if not inp: continue

            inp_list = inp.split()
            print("输入的命令是：{}".format(inp))
            cmd = inp_list[0]
            if hasattr(self, cmd):
                fun = getattr(self, cmd)
                fun(inp_list)
            else:
                print("客户端不支持命令：{}".format(cmd))

    def put(self, cmd_list):
        if len(cmd_list) < 2:
            print("调用 put 参数错误：{}".format(str(cmd_list)))
            return
        file_path = cmd_list[1]
        if os.path.exists(file_path):
            filename = os.path.basename(file_path)
            filesize = os.path.getsize(file_path)
            fileInfo = "{}|{}|{}".format(cmd_list[0], filename, filesize)
            print("发送文件信息： {}".format(fileInfo))
            self.socket.send(fileInfo.encode("utf8"))  # 发送文件信息
            res_status = self.socket.recv(1024)  # 接收返回
            if res_status.decode("utf8").startswith("OK"):
                hasSend = 0
                with open(filename, "rb") as f:
                    while filesize > hasSend:
                        data = f.read(1024)
                        data_size = len(data)
                        self.socket.send(data)
                        hasSend += data_size
                        s = str(int(hasSend*100/filesize)) + "%"
                        print("文件已经发送：{}".format(s))
        else:
            print("文件 {} 不存在".format(cmd_list[1]))

    def get(self, cmd_list):
        if len(cmd_list) < 2:
            print("调用 put 参数错误：{}".format(str(cmd_list)))
            return
        file_path = cmd_list[1]
        filename = os.path.basename(file_path)
        fileInfo = "{}|{}|{}".format(cmd_list[0], filename, 0)
        print("发送文件信息： {}".format(fileInfo))
        self.socket.send(fileInfo.encode("utf8"))  # 发送文件信息

        res_status = self.socket.recv(1024)  # 接收返回
        res_str = res_status.decode("utf8")
        print("服务端返回信息：{}".format(res_str))
        if res_str.startswith("YES"):
            res_list = res_str.split("|")
            filesize = int(res_list[1])
            # 再发送一次下载文件请求信息，发出发送数据，否则服务不会出发get 方法
            fileInfo = "{}|{}|{}".format(cmd_list[0], filename, filesize)
            self.socket.send(fileInfo.encode("utf8"))

            hasRecv = 0
            with open(filename, "wb") as f:
                while hasRecv < filesize:
                    data = self.socket.recv(1024)
                    f.write(data)
                    hasRecv += len(data)
                    s = str(int(hasRecv * 100 / filesize)) + "%"
                    print("文件已经接收：{}".format(s))
            print("文件{}接收完成".format(filename))
        else:
            print("下载文件失败，服务返回信息：{}".format(res_str))

if __name__ == '__main__':
    print("启动客户端。。。")
    client = SelectFtpClient()