import selectors
import socket

sel = selectors.DefaultSelector()

def my_accept(sock, mask):
    conn, addr = sock.accept()
    print("accepted: {} from {}".format(conn, addr))
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, my_read)

def my_read(conn, mask):
    try:
        data = conn.recv(1024)
        if not data: raise Exception  # 检查连接是否断开
        print("send {} to {}".format(repr(data), conn))
        conn.send(data)
    except Exception as e:
        print("clising {}".format(conn))
        sel.unregister(conn)
        conn.close()

sock =socket.socket()
sock.bind(("127.0.0.1", 8080))
sock.listen(1000)
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, my_accept)
print("启动 selectors socket 服务。。。")
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data  # data 是 my_accept 或 my_read
        callback(key.fileobj, mask)  # key.fileobj 是 sock 或 conn