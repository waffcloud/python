# -- coding: utf8 --
import socket,sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个socket
s.connect(('127.0.0.1', 10021))                       #建立连接
while True:                                           #接受多次数据
    data = sys.stdin.readline().strip()                 #接收数据
    if data == 'quit':                                #如果为'quit',则退出
        break
    s.send(data.encode())                             #发送编码后的数据
    print(s.recv(1024))               #打印接收到的大写数据
s.send(b'quit')                                       #放弃连接
s.close()