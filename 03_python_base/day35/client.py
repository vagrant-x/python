############################ client ############################io多路复用
import socket

client = socket.socket()
client.connect(("127.0.0.1", 8080))

while True:
    inp = input(">>>>>").strip()
    client.send(inp.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))


#####################  client ##########################client.py
import socket

client = socket.socket()
client.connect(("127.0.0.1", 8080))

while True:
    inp = input(">>>>>>").strip()
    client.send(inp.encode("utf8"))
    data = client.recv(1024)
    print("客户端返回信息：{}".format(data.decode("utf8")))