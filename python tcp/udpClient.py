# -- coding: utf8 --
import socket,sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 10022)       #服务器端地址
while True:
    data = sys.stdin.readline().strip()  #获得数据
    if not data or data == 'quit':
        break
    s.sendto(data.encode(), addr)    #发送到服务端
    recvdata, addr = s.recvfrom(1024)  #接收服务器端发来的数据
    print(recvdata.decode('utf-8'))    #解码打印
s.close()            #关闭socket