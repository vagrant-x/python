import selectors
import socket
import os

BADE_DIR = os.path.dirname(os.path.abspath(__file__))

KEY_UPLOAD = "upload"
KEY_DOWNLOAD = "download"


class SelectFtpServer:
    def __init__(self, addr=("127.0.0.1", 8080)):
        self.dic = {}
        self.addr = addr
        self.socket = socket.socket()
        self.sel = selectors.DefaultSelector()
        self.create_socket()
        self.handle()

    def create_socket(self):
        self.socket.bind(self.addr)
        self.socket.listen(100)
        self.socket.setblocking(False)
        self.sel.register(self.socket, selectors.EVENT_READ, self.accept)

    def handle(self):
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)

    def accept(self, sock, mask):
        conn, addr = sock.accept()
        print("accepted: {} from {}".format(conn, addr))
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn, mask):
        try:
            print(self.dic.get(conn))
            if not self.dic.get(conn):
                data = conn.recv(1024)
                print("...............", data.decode("utf8").split("|"))
                cmd, filename, filesize = data.decode("utf8").split("|")
                self.dic[conn] = {"cmd": cmd,
                                  "filename": filename,
                                  "filesize": filesize,
                                  "hasTrans": 0  # 已经传输大小
                                 }
                if cmd == "put":
                    conn.send(b"OK|0")
                if cmd == "get":
                    file_path = os.path.join(BADE_DIR, KEY_DOWNLOAD, filename)
                    if os.path.exists(file_path):
                        size = os.path.getsize(file_path)
                        res_str = "YES|{}".format(size)
                    else:
                        res_str = "NO|0"
                    conn.send(res_str.encode("utf8"))
            else:
                if self.dic[conn].get("cmd", None):
                    cmd = self.dic[conn].get("cmd")
                    if hasattr(self, cmd):
                        fun = getattr(self, cmd)
                        fun(conn)
                    else:
                        print("命令[{}]不存在".format(cmd))
                        conn.close()
                else:
                    print("没有[cmd]属性")
                    conn.close()
        except Exception as e:
            print("ERROR1: {}".format(e))
            self.sel.unregister(conn)
            conn.close()
            raise

    def put(self, conn):
        filename = self.dic[conn].get("filename")
        print("接收文件名：{}".format(filename))
        filesize = self.dic[conn].get("filesize")
        file_path = os.path.join(BADE_DIR, KEY_UPLOAD, filename)

        data = conn.recv(1024)
        self.dic[conn]["hasTrans"] += len(data)

        with open(file_path, 'ab') as f:
            f.write(data)
        if self.dic[conn]["hasTrans"] == filesize:
            if conn in self.dic.keys():
                self.dic[conn] = {}
            print("文件：{}， 传输完成".format(filesize))

    def get(self, conn):
        print("--------server get")
        filename = self.dic[conn].get("filename")
        print("发送文件名：{}".format(filename))
        file_path = os.path.join(BADE_DIR, KEY_DOWNLOAD, filename)
        filesize = os.path.getsize(file_path)
        self.dic[conn]["filesize"] = filesize

        # if self.dic[conn]["hasTrans"] >= filesize:
        #     if conn in self.dic.keys():
        #         self.dic[conn] = {}
        # else:
        if self.dic[conn]["hasTrans"] < filesize:
            with open(file_path, 'rb') as f:
                # 每次重新进来都需要设置光标位置，否则重复读取前1024字节
                f.seek(self.dic[conn]["hasTrans"])
                data = f.read(1024)
                conn.send(data)
                self.dic[conn]["hasTrans"] += len(data)
            print("文件：{}, 已经发送 {}".format(filesize, self.dic[conn]["hasTrans"]))

        if self.dic[conn]["hasTrans"] >= filesize:
            if conn in self.dic.keys():
                self.dic[conn] = {}
                print("删除监听")



if __name__ == '__main__':
    print("启动服务器。。。")
    server = SelectFtpServer()