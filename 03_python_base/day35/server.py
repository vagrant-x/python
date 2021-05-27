######################### server ###############################io多路复用
import socket
import select

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(3)
inp = [sk,]
while True:
    r, w, e = select.select(inp, [], [], 5)
    for i in r:
        conn, addr = i.accept()
        print("conn = {}".format(conn))
        print("hello")
    print(">>>>>")


#***********************server.py###################
import socket
import select

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))
sk.listen(3)
inp = [sk,]

while True:
    r, w, e = select.select(inp, [], [])
    for obj in r:
        if obj == sk:
            conn, addr = obj.accept()
            print("conn = {}".format(conn))
            inp.append(conn)
        else:
            data = obj.recv(1024)
            print(data.decode("utf-8"))
            res = input(">>>>").strip()
            obj.sendall(res.encode("utf8"))
    print("=======>{}".format(r))
