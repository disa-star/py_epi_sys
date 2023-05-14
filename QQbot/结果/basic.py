import requests
class function:
    #function（发）
    def __init__(self):
        pass

    def reply(self,msg,data): 
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


    def g_send(self,g_id,msg):  #群发送
        url ='http://127.0.0.1:5700/send_msg'
        paramas = {
            'message_type': 'group',
            'group_id': g_id,
            'message': msg
            }
        requests.get(url, params=paramas)

    def u_send(self,u_id,msg):   # 个人发送
        url ='http://127.0.0.1:5700/send_msg'
        paramas = {
            'message_type': 'private',
            'user_id': u_id,
           'message': msg
            }
        requests.get(url, params=paramas)
    def private_function(self,message,data): #待完善 #菜单
        if message == '1':
            self.reply('属性',data)
        elif message == '2':
            self.reply('背包',data)
        else:
            self.reply('输入1查看属性；输入2查看背包',data)

    def get_group_list(self,g_id): #获取群成员id
        url ='http://127.0.0.1:5700/get_group_member_list'
        paramas = { 'group_id': g_id }
        response = requests.get(url, params=paramas).json()
        list = []
        for i in response['data']:
            list.append(i['user_id'])
        return list

    def g_picture(self,g_id, file): #群发图片 e.g file = '1.jpg'
        msg = '[CQ:image,file={0}]'.format(file)
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(g_id, msg))

    def t_send(self,g_id, x = 'type'): #合并发送 # x为发送快捷键
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
        self.g_send(g_id,msg)