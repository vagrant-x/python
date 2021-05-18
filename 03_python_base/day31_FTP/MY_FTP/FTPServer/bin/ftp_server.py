import sys
import os
import logging.config

# 把项目的根目录添加到 sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core1 import FTPServer  # 有提示错误，但是能正常解析到
from core1 import db


def logging_config():
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(root_path, "config")
    logging_file = os.path.join(config_path, 'logging.ini')
    logging.config.fileConfig(logging_file)


if __name__ == '__main__':
    logging_config()
    logger = logging.getLogger("fileAndConsole.main")
    logger.info("执行 ftp_server.py..")
    fs = FTPServer.FTPServer()
    fs.start()