import socket
import struct
import sys
import os
import json
from tools import type_tools
from tools import file_tools

KEY_IP_PORT = ("127.0.0.1", 8000)
KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024
KEY_USER = "user"
KEY_PW = "password"
KEY_OPTION = "option"
KEY_CMD = "cmd"
KEY_STATUS = "status"
KEY_MSG = "msg"
KEY_FILE_NAME = "filename"
KEY_FILE_SIZE = "filesize"
EY_FILE_MD5 = "filemd5"

class FTPClient:

    def __init__(self, user, password, address=KEY_IP_PORT, connet=True):
        self.server_address = address
        self.user = user
        self.password = password
        self.isconnet = False
        self.user_curr_path = user.upper()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if connet:
            try:
                self.client_connet()
                self.isconnet = True
            except Exception as e:
                self.client_close()
                self.isconnet = False
                print("客户端链接异常，关闭客户端。")
                raise

    def client_connet(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def recv_head(self):
        """
        接收头，并解析为字典
        :return:
        """
        # 接收自定义头长度
        head_length_bytes = self.socket.recv(4)
        head_length = struct.unpack("i", head_length_bytes)
        # 接收自定义头并解析
        head_bytes = self.socket.recv(head_length[0])
        head_json = head_bytes.decode(KEY_UTF8)
        # print("接收的头 {}".format(head_json))
        head_dic = json.loads(head_json)
        print("接收的头 status=[{}], msg=[{}]".format(head_dic[KEY_STATUS], head_dic[KEY_MSG]))
        return head_dic

    def send_head(self, head):
        """
        封装头，发送
        :param head:
        :return:
        """
        # 发送
        head_json_str = json.dumps(head)
        head_bytes = head_json_str.encode(KEY_UTF8)
        head_bytes_len = struct.pack("i", len(head_bytes))
        self.socket.send(head_bytes_len)
        self.socket.send(head_bytes)

    def run(self):
        if not self.isconnet:
            print("客户端未连接，请重新连接客户端")
            return
        # 验证客户端是否有权限登陆
        if not self.client_auth():
            print("认证失败，退出执行")
            return
        # 登录成功后才能进行输入操作
        while True:
            try:
                inp = input("{}>>>".format(self.user_curr_path)).strip()
                print("客户端输入内容：{}".format(inp))
                if not inp: break
                if inp == "quit": break

                args_list = inp.split()
                cmd = args_list[0]
                if cmd == "put":
                    self.upload_file(args_list)
                elif cmd == "get":
                    self.download_file(args_list)
                elif cmd == "cd" or cmd == "ls":
                    self.send_cmd(cmd, inp)
                else:
                    print("该命令暂时不支持")
            except Exception as e:
                print(e)
                self.client_close()
                raise
        self.client_close()

    def send_cmd(self, first_cmd, cmd):
        """
        发送需要执行的命令
        :param first_cmd: 客户端启动成功后输入的第一个命令
        :return:
        """
        # 发送
        data = {
            KEY_OPTION: first_cmd,
            KEY_CMD: cmd
        }
        self.send_head(data)
        # cmd_bytes = cmd.encode(KEY_UTF8)
        # cmd_len_bytes = struct.pack("i", cmd_bytes)
        # self.socket.send(cmd_len_bytes)
        # self.socket.send(cmd.encode(KEY_UTF8))
        # 接收：
        recv_msg = self.socket.recv(4)
        res_length = struct.unpack("i", recv_msg)
        recv_msg = self.socket.recv(res_length[0])
        print(recv_msg.decode(KEY_UTF8))
        recv_dic = json.loads(recv_msg.decode(KEY_UTF8))
        if first_cmd == "cd":
            self.user_curr_path = recv_dic[KEY_MSG]
        elif first_cmd == "ls":
            print(recv_dic[KEY_MSG])


    def upload_file(self, args):
        """
        根据用户指定的文件执行上传操作
        :param args:
        :return:
        """
        # 提取需要上传的文件名
        filename = args[1]
        if not os.path.exists(filename):
            print("文件不存在")
            return
        filesize = os.path.getsize(filename)
        file_base_name = os.path.basename(filename)
        file_md5 = file_tools.get_file_md5(filename)
        # 封装发送文件的头, 转换为bytes 发送 bytes 的长度，内容
        head = {
            KEY_OPTION: "put",
            KEY_FILE_NAME: file_base_name,
            KEY_FILE_SIZE: filesize,
            EY_FILE_MD5: file_md5
        }
        self.send_head(head)
        # head_json_str = json.dumps(head)
        # print("上传文件发送报文头内容： {}".format(head_json_str))
        # head_bytes = head_json_str.encode(KEY_UTF8)
        # head_bytes_len = struct.pack("i", len(head_bytes))
        # self.socket.send(head_bytes_len)
        # self.socket.send(head_bytes)
        recv_head = self.recv_head()
        if recv_head[KEY_STATUS] == 0:
            print(recv_head[KEY_MSG])
            send_size = 0
            with open(filename, "rb") as f:
                for line in f:
                    self.socket.send(line)
                    send_size += len(line)
                    file_tools.show_progress_bar("上传文件[{}]".format(filename),  send_size, filesize)
                else:
                    print("\r", end="\r\n")
                    print("文件 {} 发送成功".format(filename))

    def download_file(self, args):
        """
        根据用户指定的文件执行下载操作
        :param args:
        :return:
        """
        filename = args[1]
        head = {
            KEY_OPTION: "get",
            KEY_FILE_NAME: filename
        }
        # 发送：头和头数据
        head_json_str = json.dumps(head)
        head_bytes = head_json_str.encode(KEY_UTF8)
        head_bytes_len = struct.pack("i", len(head_bytes))
        self.socket.send(head_bytes_len)
        self.socket.send(head_bytes)
        # 接收：
        recv_msg = self.socket.recv(4)
        res_length = struct.unpack("i", recv_msg)
        recv_msg = self.socket.recv(res_length[0])
        res_data = type_tools.json_bytes_2_dict(recv_msg)
        # 文件存在，开始接收文件
        if res_data[KEY_STATUS] == 0 or res_data[KEY_STATUS] == "0":
            filesize = res_data[KEY_FILE_SIZE]
            server_file_md5 = res_data[EY_FILE_MD5]
            with open(filename, "wb") as f:
                recv_size = 0
                while filesize > recv_size:
                    msg = self.socket.recv(KEY_BUFFER_SIZE)
                    f.write(msg)
                    recv_size += len(msg)
                    file_tools.show_progress_bar("下载文件[{}]".format(filename),  recv_size, filesize)
                print("\r", end="\r\n")
            # 获取md5 并进行校验
            file_md5 = file_tools.get_file_md5(filename)
            if file_md5 == server_file_md5:
                print("下载文件通过md5校验，下载成功")
            else:
                print("下载文件没有md5校验，下载失败，删除文件")
                os.remove(filename)

    def client_auth(self):
        """
        客户端认证方法
        :return:
        """
        # 发送验证信息
        data = {
            KEY_OPTION: "login",
            KEY_USER: self.user,
            KEY_PW: self.password
        }
        data_bytes = type_tools.dict_2_json_bytes(data)
        data_len_bytes = struct.pack("i", len(data_bytes))
        self.socket.send(data_len_bytes)
        self.socket.send(data_bytes)
        # 接收验证信息
        recv_msg = self.socket.recv(4)
        print("recv_msg {}".format(recv_msg))
        res_length = struct.unpack("i", recv_msg)
        recv_msg = self.socket.recv(res_length[0])
        res_data = type_tools.json_bytes_2_dict(recv_msg)
        if res_data[KEY_STATUS] == 0 or  res_data[KEY_STATUS] == "0":
            print("用户 {} 认证成功".format(self.user))
            return True
        return False


if __name__ == '__main__':
    print(sys.argv)
    user = sys.argv[1]
    pw = sys.argv[2]
    ip = sys.argv[3]
    port = sys.argv[4]
    addr = (sys.argv[3], int(sys.argv[4]))
    print("启动客户端。。。")
    client = FTPClient(user, pw, addr)
    client.run()
