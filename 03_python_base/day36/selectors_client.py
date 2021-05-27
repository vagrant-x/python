import socket

client = socket.socket()
client.connect(("127.0.0.1", 8080))

while True:
    cmd = input(">>>").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))

client.close()