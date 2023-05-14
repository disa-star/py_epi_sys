import socket
import json
from QQ import Group_function
import time
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

qq = Group_function(12345678) #（）内填qq机器人所在群
#具体功能
qq.G_send() #发群消息

qq.G_t_send(x = 'type') 
#合并后发群消息, x可看作发送键, 默认为'type'

'''
input = 
1
2
type
则会发送消息：
1
2
'''

qq.G_picture(file= '1.jpg')
#发群图片  e.g file = '1.jpg', (引号不可省略)
#图片需放在 go-cqhttp文件 的 data文件 的 images文件 中

# qq.G_send(), qq.G_t_send(x = 'type'), qq.G_picture(file= '1.jpg') 目前只能同时运行一个
#调用e.g(另两个类似)
def send():
    while 1:
        qq.G_t_send('x')
        time.sleep(1)


qq.Auto_reply(message,data)
#调用方法如下
def auto(): 
    while 1:
        data = rev_msg()
        if data['post_type'] == 'message' and data['message_type'] == 'private' :
            qq.Auto_reply(data['message'],data)
        time.sleep(1)
# 该调用方法将自动回复限定于私聊中（且需有好友关系）
#若想限定在群众只需将 data['message_type'] == 'private' 改为 == 'group'
#自动回复内容还未设定


qq.Get_group_list() #获取群成员id