import socket
import json
import time
import requests

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


#function（发）
def reply(msg,data): 
    url ='http://127.0.0.1:5700/send_msg'
    msg_type = data['message_type']
    if msg_type =='group':
        g_id = data['group_id']
        paramas = {
        'message_type': msg_type,
        'group_id': g_id,
        'message': msg
        }
    else:
        u_id = data['user_id']
        paramas = {
        'message_type': msg_type,
        'user_id': u_id,
        'message': msg
        }
    requests.get(url, params=paramas)


def g_send(g_id,msg):  #群发送
    url ='http://127.0.0.1:5700/send_msg'
    paramas = {
        'message_type': 'group',
        'group_id': g_id,
        'message': msg
        }
    requests.get(url, params=paramas)

def u_send(u_id,msg):   # 个人发送
    url ='http://127.0.0.1:5700/send_msg'
    paramas = {
        'message_type': 'private',
        'user_id': u_id,
        'message': msg
        }
    requests.get(url, params=paramas)
def private_function(message,data): #待完善 #菜单
    if message == '1':
        reply('属性',data)
    elif message == '2':
        reply('背包',data)
    else:
        reply('输入1查看属性；输入2查看背包',data)

def get_group_list(g_id): #获取群成员id
    url ='http://127.0.0.1:5700/get_group_member_list'
    paramas = { 'group_id': g_id }
    response = requests.get(url, params=paramas).json()
    dic = {}
    for i in response['data']:
        dic[i['nickname']] = str(i['user_id'])
    return dic

def g_picture(g_id, file): #群发图片 e.g file = '1.jpg'
    msg = '[CQ:image,file={0}]'.format(file)
    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(g_id, msg))

def t_send(g_id): #合并发送
    i = 0
    list = []
    msg = ''
    while i == 0:
        str = input()
        if str != "type":
            list.append(str)
        else: 
            i = 1
    for j in list:
        msg = msg + str(j) + '\n'
    g_send(g_id,msg)

def t_send(g_id, x = 'type'): #合并发送 # x为发送快捷键
    i = 0
    list = []
    msg = ''
    while i == 0:
        word = input()
        if word != x:
            list.append(word)
        else: 
            i = 1
    for j in list:
        msg = msg + str(j) + '\n'
    g_send(g_id,msg)


def main(): #需根据实际情况改
    while 1:
        data = rev_msg()
        if data['post_type'] == 'message' and data['message_type'] == 'private':
            private_function(data['message'],data)
        time.sleep(1)


if __name__ == '__main__':
    main()