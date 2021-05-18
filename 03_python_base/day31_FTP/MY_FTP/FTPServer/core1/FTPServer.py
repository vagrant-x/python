import socketserver
import os
import struct
import logging

logger = logging.getLogger("fileAndConsole." + __file__)


class FtpServerHandle(socketserver.BaseRequestHandler):

    def handle(self):
        pass


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