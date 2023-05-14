import socket
import json
import time
from threading import Thread
from QQ import Group_function

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1', 5701))
ListenSocket.listen(100)
HttpResponseHeader = '''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
'''

def request_to_json(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="\n":
            return json.loads(msg[i:])
    return None

def rev_msg(): #收
    Client, Address = ListenSocket.accept()
    Request = Client.recv(1024).decode(encoding='utf-8')
    rev_json=request_to_json(Request)
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json

def auto(): 
    while 1:
        data = rev_msg()
        if data['post_type'] == 'message' and data['message_type'] == 'private' :
            qq.Auto_reply(data['message'],data)
        time.sleep(1)

def send():
    while 1:
        qq.G_t_send('x')
        time.sleep(1)

#并行
if __name__ == '__main__':
    qq = Group_function(452967867)
    threads = [Thread(target=auto),Thread(target=send)]  # 这里是创建2个线程，放到一个列表里
    for t in threads:
        t.start()  # 启动线程
    for t in threads:
        t.join()  # 线程等待
