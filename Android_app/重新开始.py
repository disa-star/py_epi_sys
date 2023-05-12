import copy
universal_id_dict = {}
attribution_model_dict = {}
#定义atom末位为00
#event为01
#action为02
#attribution为03
#unit为04
class id_control():
    def __init__(self,id=0):
        global universal_id_dict
        assert self.num != None
        #决定id
        #正则化id
        id = id*100 + self.num
        if id <= 0:
            self.id = self.get_valid_id()
        else:
            if self.id_validation_check(id):
                #正则化id
                self.id = id
            else:
                self.id = self.get_valid_id()
        del id
        universal_id_dict[self.id] = self
        return self
    #检验id是否合法
    def id_validation_check(self,id):
        if id in universal_id_dict.keys():
            return False
        else:
            return True
    #获取合法id
    def get_valid_id(self):
        for i in range(1,10000):
            id = i*100 + self.num
            if self.id_validation_check(id):
                return id
            else:
                pass
        else:
            raise "10000以下的id都被使用了,请手动设置id"
        
    def __del__(self):
        del universal_id_dict[self.id]

    def btn_change_description(self,description:dict):
        self.description = description


class atom(id_control):
    
    def __init__(self,func,id=0,*args,**kwargs):
        global universal_id_dict        
        #载入描述
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        #载入挂载函数
        self.func = func
        assert isinstance(id,int) 
        self.num = 0
        super().__init__(self,id=id)
    
    def btn_rebond(self,func):
        self.func = func
    #atom不负责存储注册信息
    def register_to_event(self,event_id,owner_id=None):
        universal_id_dict[event_id].atom_list_append(atom_id=self.id,owner_id=owner_id)
    
    def resgin_from_event(self,event_id,owner_id=None):
        universal_id_dict[event_id].atom_list_pop(atom_id=self.id,owner_id=owner_id)













class event(id_control):
    def __init__(self,id=0,*args,**kwargs):
        #载入描述
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        
        self.atom_list = []

        global universal_id_dict
        assert isinstance(id,int) 
        self.num = 1
        super().__init__(self,id=id)
    
    def atom_list_append(self,atom_id,owner_id):
        for i,atom_info in enumerate(self.atom_list):
            if atom_id == atom_info['atom_id'] and owner_id == atom_info['owner_id']:
                self.atom_list[i]['repeat'] += 1
                break
        else:
            self.atom_list.append({'atom_id':atom_id,
                                'owner_id':owner_id,
                                'repeat':1})
            
    def atom_list_pop(self,atom_id,owner_id):
        for i,atom_info in enumerate(self.atom_list):
            if atom_id == atom_info['atom_id'] and owner_id == atom_info['owner_id']:
                self.atom_list[i]['repeat'] -= 1
                break
        else:
            pass

        for i,atom_info in enumerate(self.atom_list):
            if atom_info['repeat'] <= 0:
                del self.atom_list[i]

    def run(self,world_status:dict):
        for atom_info in self.atom_list:
            world_status['event_id_now'] = self.id
            ops,world_status = universal_id_dict[atom_info['atom_id']].func(
                owner=atom_info['owner_id'],
                repeat=atom_info['repeat'],
                world_status=world_status)
            
            if ops == 0:
                pass
            elif ops == 1:
                #直接退出这次事件
                break
            elif ops >= 2:
                #不但退出这次事件,并且直接退出上层激发事件列的行动
                return ops-1,world_status
        return 0,world_status

    def btn_run(self):
        #禁止使用
        pass

    








class attribution(id_control):
    def __init__(self,id=0,*args,**kwargs):
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        if 'valuable' in kwargs.keys():
            self.valuable = kwargs['valuable']
        else:
            self.valuable = False
        if 'reg_atom_dict' in kwargs.keys():
                self.reg_atom_dict = kwargs['reg_atom_dict']

        if self.valuable:
            if 'limit' in kwargs.keys():
                self.limit = kwargs['limit']    
            if 'value' in kwargs.keys():
                self.value = kwargs['value']
            if 'atom_list_on_value_change' in kwargs.keys():
                self.atom_list_on_value_change = kwargs['atom_list_on_value_change']
            if 'atom_list_on_limit_change' in kwargs.keys():
                self.atom_list_on_limit_change = kwargs['atom_list_on_limit_change']
        self.owner = None
        self.attach_ctn = 0
        self.num = 3

        global universal_id_dict,attribution_model_dict
        assert isinstance(id,int) 
        self.num = 1
        super().__init__(self,id=id)
        attribution_model_dict[self.id] = self

    def __del__(self):
        del attribution_model_dict[self.id]
        super().__del__(self)

    def set_owner(self,owner_id,*args,**kwargs):
        self.owner = owner_id
        if self.valuable:
            if 'value' in kwargs.keys():
                self.value = kwargs['value']
            if 'limit' in kwargs.keys():
                self.limit = kwargs['limit']
            self.normalization()
        else:
            pass
        if 'attach_ctn' in kwargs.keys():
                self.attach_to_level(kwargs['attach_ctn']) 

    def normalization(self):
        if self.value > self.limit[1]:
            self.value = self.limit[1]
        elif self.value < self.limit[0]:
            self.value = self.limit[0]

    def set_limit_commit(self,lim:list):
        self.limit = lim
        self.normalization()

    def change_limit_commit(self,lim:list):
        self.limit[0] += lim[0]
        self.limit[1] += lim[1]
        self.normalization()

    def set_value_commit(self,value:int):
        #真正的更新了数值
        self.value = value
        #归一化防止溢出
        self.normalization()

    def change_value_commit(self,delta:int):
        #真正的更新了数值
        self.value += delta
        #归一化防止溢出
        self.normalization()

    def attach(self):
        #这个和action的注册相似,
        if self.attach_ctn == 0:
            for event_id in self.reg_atom_dict:
                for atom_id in self.reg_atom_dict[event_id]:
                    universal_id_dict[event_id].atom_list_append(atom_id,self.owner)   
        else:
            self.attach_ctn += 1

    def unattach(self):
        #这个和action的注销相似,
        self.attach_ctn -= 1
        if self.attach_ctn <= 0:
            self.attach_ctn = 0
            for event_id in self.reg_atom_dict:
                for atom_id in self.reg_atom_dict[event_id]:
                    universal_id_dict[event_id].atom_list_pop(atom_id,self.owner) 

    def attach_to_level(self,level):
        if level<=0:
            self.attach_ctn = 0
            self.unattach()
        else:
            self.attach()
            self.attach_ctn = level

    def attach_by_level(self,delta):
        self.attach_to_level(self.attach_ctn+delta)

    def dict_out_data(self):
        if self.valuable:
            return {'value':self.value,
                    'limit':self.limit,
                    'attach_ctn':self.attach_ctn}





class unit(id_control):
    def __init__(self,id=0,*args,**kwargs):
        assert isinstance(id,int)
        self.num = 4
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        
        self.attribution_dict = copy.deepcopy(attribution_model_dict)
        if 'init_attribution' in kwargs:
            for id in kwargs['init_attribution']:
                self.attribution_dict[id].set_owner(self.id,**(kwargs['init_attribution'][id]))

        global universal_id_dict,attribution_model_dict
        super().__init__(id)
    #这个是权宜之计
    def after_change_attribution_dict(self):
        temp = copy.deepcopy(attribution_model_dict)
        for id in self.attribution_dict:
            #转移信息+全部注销一次
            temp[id].set_owner(self.id,self.attribution_dict[id].dict_out_data())
            self.attribution_dict[id].attach_to_level(0)

        self.attribution_dict = temp
        del temp

    def after_deepcopy(self):
        #如果自己和全局字典的内容不一样
        if self is not universal_id_dict[self.id]:
            self.id = self.get_valid_id()
        for id in self.attribution_dict:
            self.attribution_dict[id].set_owner(self.id)

    def set_limit(self,lim:list,world_status:dict):
        assert self.valuable == True
        world_status['limit_change_attribute'] = self.id
        world_status['lim_change_to'] = lim
        for event_id in self.event_list_on_limit_change:
            ops,world_status = universal_id_dict[event_id].run(world_status)
            #同样,下面为了接收event run出来的结果
            if ops == 0:
                pass
            elif ops == 1:
                break
            elif ops >= 2:
                world_status['limit_change_attribute'].set_limit_commit(world_status['lim_change_to'])

