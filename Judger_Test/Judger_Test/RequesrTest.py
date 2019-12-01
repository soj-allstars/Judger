from module1 import count_words_at_url
from redis import Redis
from rq import Queue
import time
import socket

host = '192.168.1.8'
port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind((host,port))
server.listen(5)
print("----")
while True:
    conn,addr = server.accept()  # conn表示链接；addr表示地址；返回的结果是一个元组
    msg = conn.recv(1024)   # 接受信息，1024表示接收1024个字节的信息
    print("客户端发来的消息是:%s" %msg.decode('utf-8'))
    conn.send(msg.upper())  # 发送的消息

conn.close()
server.close()
pass

#q = Queue(connection=Redis())
#result = q.enqueue(
#            count_words_at_url, 'https://www.baidu.com')


