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

def rev_msg():# json or None
    Client, Address = ListenSocket.accept()
    Request = Client.recv(1024).decode(encoding='utf-8')
    rev_json=request_to_json(Request)
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json

def reply(msg):
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

def private_function(message): #待完善
    if message == '菜单':
        reply('暂无')
    if message != '菜单':
        reply('[CQ:face,id=14]')

def g_send(g_id,msg):
    url ='http://127.0.0.1:5700/send_msg'
    paramas = {
        'message_type': 'group',
        'group_id': g_id,
        'message': msg
        }
    requests.get(url, params=paramas)

def u_send(u_id,msg):
    url ='http://127.0.0.1:5700/send_msg'
    paramas = {
        'message_type': 'private',
        'user_id': u_id,
        'message': msg
        }
    requests.get(url, params=paramas)

def regular(hour, minute, g_id, msg, now_hour, now_minute):
    if now_hour == hour and  now_minute == minute:
        g_send(g_id,msg)
        time.sleep(20)

if __name__ == '__main__':
    while 1==1:
        data = rev_msg()
        print(data)
        now_time = time.localtime()
        now_hour, now_minute = now_time[3],now_time[4]
        if data['post_type'] == 'message':
            reply('你真帅')
        regular(13,59,452967867,'太巨啦', now_hour, now_minute)
        time.sleep(0.1)