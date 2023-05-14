import basic
bs = basic.function()
class Group_function:
    def __init__(self,g_id):
        self.g_id = g_id
    
    def Get_group_list(self):
        bs.get_group_list(self.g_id)

    def G_send(self):  #群内发送文字
        msg = input()
        bs.g_send(self.g_id,msg)

    def G_t_send(self, x): #默认为输入type
        bs.t_send(self.g_id, x)
    
    def G_picture(self, file): #群发图片 e.g file = '1.jpg'
        bs.g_picture(self.g_id, file)
    
    def Auto_reply(self,message,data):
        bs.private_function(message,data)
