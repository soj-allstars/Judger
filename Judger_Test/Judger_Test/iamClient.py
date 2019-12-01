import socket


while 1:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('47.106.140.231',9999))
    print('----')
    re_data = "123"
    client.send(re_data.encode("utf8"))
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))
    client.close()
