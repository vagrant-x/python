import socketserver
import os
import struct
import logging
import json
from core1 import db
from tools import system_tools
from tools import file_tools

KEY_USER = "user"
KEY_PASSWORD = "password"
KEY_DISK_SIZE = "disk_size"
KEY_USED_SIZE = "used_size"

KEY_UTF8 = "utf-8"
KEY_BACKLOG = 5
KEY_BUFFER_SIZE = 1024

KEY_STATUS = "status"
KEY_MSG = "msg"

KEY_OPTION = "option"
KEY_CMD = "cmd"
KEY_FILE_NAME = "filename"
KEY_FILE_SIZE = "filesize"
KEY_FILE_MD5 = "filemd5"

logger = logging.getLogger("fileAndConsole." + __file__)


class FtpServerHandle(socketserver.BaseRequestHandler):

    def handle(self):
        # 保存用户的当前目录结构， 用户能访问到的根目录是由自己用户名创建在home文件下的文件夹
        self.path_dir = []


        while True:
            head = self.recv_head()
            cmd = head[KEY_OPTION]
            if cmd == "login":
                user = head[KEY_USER]
                pw = head[KEY_PASSWORD]
                status, msg = self.authentication(user, pw)
                # 向路径列表中添加一个用户根目录
                if not status:
                    self.path_dir.append(user.upper())
                    home_path = system_tools.get_home()
                    user_path = os.path.join(home_path, user.upper())
                    if not os.path.exists(user_path):
                        os.mkdir(user_path)
                self.send_status_msg(status, msg)
            elif cmd == "put":
                self.upload_file(head)
            elif cmd == "get":
                self.download_file(head)
            elif cmd == "cd":
                status, msg = self.exe_cd(head)
                self.send_status_msg(status, msg)
            elif cmd == "ls":
                status, msg = self.exe_ls(head)
                self.send_status_msg(status, msg)
            else:
                logger.info("暂时不支持[{}]操作".format(cmd))

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
        logger.info("接收的头 {}".format(head_json))
        head_dic = json.loads(head_json)
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
        self.request.send(head_bytes_len)
        self.request.send(head_bytes)

    def send_status_msg(self,status, msg):
        data = {
            "status": status,
            "msg": msg
        }
        self.send_head(data)

    def authentication(self, user, password):
        """
        用户认证
            成功返回 status:0, msg: 验证成功
            失败返回： statut: -1
        :param user:
        :param password:
        :return:
        """
        user_data = db.get_user_data(user)
        msg = ""
        status = -1
        if user_data is None:
            msg = "用户 {} 不存在".format(user)
            # logger.info(msg)
            self.login = False
        else:
            if password == user_data[KEY_PASSWORD]:
                # 记录用户的基本信息
                self.user = user
                self.password = password
                self.dick_size_bytes = user_data[KEY_DISK_SIZE]
                self.used_dick_size_bytes = user_data[KEY_USED_SIZE]
                self.login = True
                msg = "验证成功"
                status = 0
            else:
                msg = "用户[{}]密码[{}]不正确".format(user, password)
                # logger.info(msg)
        return status, msg

    def upload_file(self, head_dic):
        """
        客户端上传文件到服务端处理方法
        :param head_dic:
        :return:
        """
        filename = head_dic[KEY_FILE_NAME]
        filesize =head_dic[KEY_FILE_SIZE]
        file_md5 = head_dic[KEY_FILE_MD5]
        logger.info("用户总空间：{}， 已经使用：{}".format(
            self.dick_size_bytes, self.used_dick_size_bytes))
        if self.used_dick_size_bytes + filesize > self.dick_size_bytes:
            status = -1
            msg = "用户磁盘空间不足，无法上传"
            self.send_status_msg(status,msg)
            return
        else:
            status = 0
            msg = "用户磁盘空间足够"
            self.send_status_msg(status,msg)
        recv_size = 0
        abs_filename = os.path.join(system_tools.get_home(), *self.path_dir, filename)
        with open(abs_filename, "wb") as f:
            while filesize > recv_size:
                if filesize - recv_size >KEY_BUFFER_SIZE:
                    size = KEY_BUFFER_SIZE
                else:
                    size = filesize - recv_size
                recv_msg = self.request.recv(size)
                f.write(recv_msg)
                recv_size += len(recv_msg)
        save_file_md5 = file_tools.get_file_md5(abs_filename)
        if save_file_md5 == file_md5:
            # 更新已经使用内存到程序并写入文件（db）
            self.used_dick_size_bytes += filesize
            db.set_user_used_data(self.user, self.used_dick_size_bytes)
            logger.info("服务端保存文件[{}]成功".format(filename))
        else:
            # 校验失败，删除保存文件
            os.remove(abs_filename)
            logger.info("服务端保存文件[{}]失败， md5校验失败".format(filename))


    def download_file(self, head_dic):
        """
        客户端从服务端下载文件方法
        :param head_dic:
        :return:
        """
        filename = head_dic[KEY_FILE_NAME]
        filename = os.path.join(system_tools.get_home(), *self.path_dir, filename)
        if os.path.exists(filename):
            # 组织发送响应头
            file_md5 = file_tools.get_file_md5(filename)
            filesize = os.path.getsize(filename)
            rep_head = {
                KEY_STATUS: 0,
                KEY_MSG: "文件存在",
                KEY_FILE_SIZE: filesize,
                KEY_FILE_MD5: file_md5
            }
            self.send_head(rep_head)
            # 发送文件内容
            with open(filename, "rb") as f:
                for line in f:
                    self.request.send(line)
                else:
                    logger.info("发送文件[{}]完成，发送大小为：{}".format(filename, filesize))
        else:
            status = -1
            msg = "文件不存在"
            self.send_status_msg(status, msg)

    def exe_cd(self, head):
        cmd = head[KEY_CMD]
        cmd_list = cmd.strip().split()
        status = 0
        msg = "\\".join(self.path_dir)
        if len(cmd_list) < 2:
            return status, msg
        elif ".." == cmd_list[1]:
            if len(self.path_dir) == 1:
                msg = self.path_dir[0]
            else:
                self.path_dir.pop()
                msg = "\\".join(self.path_dir)
            return status, msg
        else:
            # 拼接路径并判断是否存在
            cd_dir = cmd_list[1]
            home_path = system_tools.get_home()
            curr_path = os.path.join(home_path, *self.path_dir)
            file_list = os.listdir(curr_path)
            if cd_dir in file_list:
                self.path_dir.append(cd_dir)
                status = 0
                msg = "\\".join(self.path_dir)
            else:
                status = -1
                msg = "文件夹[{}]不存在".format(cd_dir)
            return status, msg


    def exe_ls(self, head):
        """
        处理 ls 命令， 返回 状态码和执行结果
            执行成功： status = 0, msg = 所有文件
            执行失败： status = -1, msg 失败原因
        :param head:
        :return:
        """
        cmd = head[KEY_CMD]
        if cmd == "ls":
            home_path = system_tools.get_home()
            curr_path = os.path.normpath(os.path.join(home_path, *self.path_dir))
            file_list = os.listdir(curr_path)
            file_list_str = "  ".join(file_list)
            status = 0
            msg = file_list_str
        else:
            status = -1
            msg = "未知命令"
        logger.info("status = {}, msg = {}".format(status, msg))
        return status, msg


class FTPServer():
    def __init__(self, address=("127.0.0.1", 8000), handle=FtpServerHandle):
        self.address = address
        self.handle = handle

    def start(self):
        logger.info("启动 FTP 服务")
        ss = socketserver.ThreadingTCPServer(self.address, self.handle)
        ss.serve_forever()


if __name__ == '__main__':
    pass