class Group_function:
    def __init__(self, g_id):
        self.g_id = g_id

    def u_send(self, u_id):   # 个人发送
        import requests
        msg = input()
        url = 'http://127.0.0.1:5700/send_msg'
        paramas = {
            'message_type': 'private',
            'user_id': u_id,
            'message': msg
            }
        requests.get(url, params=paramas)

    def Get_group_list(self):  # 获取群内成员id
        import requests
        url = 'http://127.0.0.1:5700/get_group_member_list'
        paramas = {'group_id': self.g_id}
        response = requests.get(url, params=paramas).json()
        g_list = []
        for i in response['data']:
            g_list.append(i['user_id'])
        return g_list

    def Get_messgae_and_auto_reply(self):  # 获取qq消息
        import socket
        import json
        import requests
        ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ListenSocket.bind(('127.0.0.1', 5701))
        ListenSocket.listen(100)
        HttpResponseHeader = '''HTTP/1.1 200 OK\r\n
        Content-Type: text/html\r\n\r\n
        '''

        def request_to_json(msg):
            for i in range(len(msg)):
                if msg[i] == "{" and msg[-1] == "\n":
                    return json.loads(msg[i:])
            return None

        def rev_msg():  # 收
            Client, Address = ListenSocket.accept()
            Request = Client.recv(1024).decode(encoding='utf-8')
            rev_json = request_to_json(Request)
            Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
            Client.close()
            return rev_json

        def reply(msg, Data):
            url = 'http://127.0.0.1:5700/send_msg'
            msg_type = Data['message_type']
            if msg_type == 'group':
                g_id = Data['group_id']
                paramas = {
                    'message_type': msg_type,
                    'group_id': g_id,
                    'message': msg
                }
            else:
                u_id = Data['user_id']
                paramas = {
                    'message_type': msg_type,
                    'user_id': u_id,
                    'message': msg
                }
            requests.get(url, params=paramas)

        g_list = self.Get_group_list()

        while 1:
            data = rev_msg()
            if data['post_type'] == 'message':
                if data['message_type'] == 'private' and data['self_id'] in g_list:
                    message = data['message']
                    if message == '1':
                        reply('属性', data)
                    elif message == '2':
                        reply('背包', data)
                    else:
                        reply('输入1查看属性；输入2查看背包', data)
                if data['message_type'] == 'group' and data['group_id'] == self.g_id:
                    result = '群聊（{0}）：{1}：{2}'.format(data['group_id'], data['sender']['nickname'], data['message'])
                    print(result)

    def G_send(self):  # 群内发送文字
        import requests
        msg = input()
        url = 'http://127.0.0.1:5700/send_msg'
        paramas = {
            'message_type': 'group',
            'group_id': self.g_id,
            'message': msg
            }
        requests.get(url, params=paramas)

    def G_t_send(self, x='type'):  # 合并后发送消息，默认为输入type
        i = 0
        m_list = []
        msg = ''
        while i == 1:
            word = input()
            if word != x:
                m_list.append(word)
            else:
                i = 1
        for j in m_list:
            msg = msg + str(j) + '\n'
        self.G_send(msg)
    
    def G_picture(self):  # 群发图片
        import requests
        file = input()
        msg = '[CQ:image,file={0}]'.format(file)
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(self.g_id, msg))

    def G_ban(self):  # 禁言
        import requests
        url = 'http://127.0.0.1:5700/set_group_whole_ban'
        paramas = {
            'group_id': self.g_id,
            'enable': 'true'
        }
        requests.get(url, params=paramas)

    def G_ban_cancel(self):  # 解除禁言
        import requests
        url = 'http://127.0.0.1:5700/set_group_whole_ban'
        paramas = {
            'group_id': self.g_id,
            'enable': 'false'
        }
        requests.get(url, params=paramas)
