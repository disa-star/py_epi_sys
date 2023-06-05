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
        
        if id <= 0:
            self.id = self.get_valid_id()
        else:
            id = id*100 + self.num
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

    def refresh_id(self):
        if universal_id_dict[self.id] is not self:
            self.id = self.get_valid_id()
            universal_id_dict[self.id] = self

    def on_load(self):
        if self.id in universal_id_dict.keys():
            self.refresh_id()
        else:
            universal_id_dict[self.id] = self


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
        super().__init__(id=id)
    
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
        super().__init__(id=id)
        
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
        #用于遗传action_id
        if 'action_id_now' in world_status.keys():
            action_prev = world_status['action_id_now']
        else:
            action_prev = None
        if 'action_starter' in world_status.keys():
            starter_prev = world_status['action_starter']
        else:
            starter_prev = None      
            
        for atom_info in self.atom_list:
            if action_prev != None:
                world_status['action_id_now'] = action_prev
            if starter_prev != None:
                world_status['action_starter'] = starter_prev
            world_status['event_id_now'] = self.id
            ops,world_status = universal_id_dict[atom_info['atom_id']].func(
                owner=atom_info['owner_id'],
                repeat=atom_info['repeat'],
                world_status=world_status)
            #删除阶段
            del world_status['event_id_now']
            if action_prev == None:
                del world_status['action_id_now']
            if starter_prev == None:
                del world_status['action_starter']
            if ops == 0:
                pass
            elif ops == 1:
                #直接退出这次事件
                break
            elif ops >= 2:
                #不但退出这次事件,并且直接退出上层激发事件列的行动
                return ops-1,world_status
        return 0,world_status

    




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
        else:
            self.reg_atom_dict = []

        if self.valuable:
            if 'limit' in kwargs.keys():
                self.limit = kwargs['limit']  
            else:
                self.limit = [0,0]
            if 'value' in kwargs.keys():
                self.value = kwargs['value']
            else:
                self.value = 0
            if 'event_list_on_value_change' in kwargs.keys():
                self.event_list_on_value_change = kwargs['event_list_on_value_change']
            else:
                self.event_list_on_value_change = {}
            if 'event_list_on_limit_change' in kwargs.keys():
                self.event_list_on_limit_change = kwargs['event_list_on_limit_change']
            else:
                self.event_list_on_limit_change = {}
        self.owner = None
        self.attach_ctn = 0
        self.num = 3

        global universal_id_dict,attribution_model_dict
        assert isinstance(id,int) 
        super().__init__(id=id)
        attribution_model_dict[self.id] = self

    def on_load(self):
        if self.id in attribution_model_dict.keys():
            if attribution_model_dict[self.id] is not self:
                self.refresh_id()
                attribution_model_dict[self.id] = self
            else:
                pass
        else:
            attribution_model_dict[self.id] = self
        return super().on_load()

    def __del__(self):
        pass

    def delete(self):
        del universal_id_dict[self.id]
        del attribution_model_dict[self.id]
        del self

    def set_limit(self,lim:list,world_status:dict):
        assert self.valuable == True
        world_status['limit_change_attribution'] = self.id
        world_status['limit_change_unit'] = self.owner
        world_status['lim_change_to'] = lim
        for event_id in self.event_list_on_limit_change:
            ops,world_status = universal_id_dict[event_id].run(world_status)
            #同样,下面为了接收event run出来的结果
            if ops == 0:
                pass
            elif ops == 1:
                break
            elif ops >= 2:
                universal_id_dict[world_status['limit_change_unit']].attribution_dict[world_status['limit_change_attribution']].set_limit_commit(world_status['lim_change_to'])
                del world_status['limit_change_attribution'],world_status['limit_change_unit'],world_status['lim_change_to']
                return ops-1,world_status
            
        universal_id_dict[world_status['limit_change_unit']].attribution_dict[world_status['limit_change_attribution']].set_limit_commit(world_status['lim_change_to'])
        del world_status['limit_change_attribution'],world_status['limit_change_unit'],world_status['lim_change_to']
        return 0,world_status
    
    #套皮函数
    def change_limit(self,delta:list,world_status:dict):
        lim = [self.limit[0]+delta[0],self.limit[1]+delta[1]]
        self.set_limit(lim,world_status)

    def add_value(self,delta:int,world_status:dict):
        assert self.valuable == True
        world_status['value_change_attribution'] = self.id
        world_status['value_change_unit'] = self.owner
        world_status['value_change_by'] = delta
        for event_id in self.event_list_on_value_change:
            ops,world_status = universal_id_dict[event_id].run(world_status)
            #同样,下面为了接收event run出来的结果
            if ops == 0:
                pass
            elif ops == 1:
                break
            elif ops >= 2:
                universal_id_dict[world_status['value_change_unit']].attribution_dict[world_status['value_change_attribution']].change_value_commit(world_status['value_change_by'])
                del world_status['value_change_attribution'],world_status['value_change_unit'],world_status['value_change_by']
                return ops-1,world_status
            
        universal_id_dict[world_status['value_change_unit']].attribution_dict[world_status['value_change_attribution']].change_value_commit(world_status['value_change_by'])
        del world_status['value_change_attribution'],world_status['value_change_unit'],world_status['value_change_by']
        return 0,world_status
    
    #套皮
    def set_value(self,value:int):
        delta = value - self.value
        self.add_value(delta)

    def set_owner(self,owner_id,*args,**kwargs):
        self.owner = owner_id
        if self.valuable:
            if 'value' in kwargs:
                self.value = kwargs['value']
            if 'limit' in kwargs:
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

    #这之下是安全的btn系列函数
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
    #这之上是安全的btn系列函数

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


class action(id_control):
    def __init__(self,id=0,*args,**kwargs):
        assert isinstance(id,int)
        self.num = 2
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        if 'reg_atom_dict' in kwargs.keys():
            self.reg_atom_dict = kwargs['reg_atom_dict']
        if 'event_list' in kwargs.keys():
            self.event_list = kwargs['event_list']
        #稍后实现在action时获得attribution功能
        
        global universal_id_dict
        super().__init__(id=id)

    def setup(self,owner_id):
        for event_id in self.reg_atom_dict:
            for atom_id in self.reg_atom_dict[event_id]:
                universal_id_dict[event_id].atom_list_append(atom_id,owner_id)

    def setdown(self,owner_id):
        for event_id in self.reg_atom_dict:
            for atom_id in self.reg_atom_dict[event_id]:
                universal_id_dict[event_id].atom_list_pop(atom_id,owner_id)

    def do(self,owner_id,world_status:dict):
        self.setup(owner_id)
        for event_id in self.event_list:
            world_status['action_id_now'] = self.id
            world_status['action_starter'] = owner_id
            ops,world_status = universal_id_dict[event_id].run(world_status)
            del world_status['action_id_now']
            if ops == 0:
                pass
            elif ops == 1:
                break
            elif ops >= 2:
                self.setdown(owner_id)
                return ops-1,world_status
        self.setdown(owner_id)
        return 0,world_status



class unit(id_control):
    def __init__(self,id=0,*args,**kwargs):
        global universal_id_dict
        global attribution_model_dict
        assert isinstance(id,int)
        self.num = 4
        super().__init__(id=id)
        if 'description' in kwargs.keys():
            self.description = kwargs['description']
        #初始化全部词缀和默认已拥有词缀
        
        self.attribution_dict = copy.deepcopy(attribution_model_dict)
        for id in self.attribution_dict:
            self.attribution_dict[id].set_owner(self.id)
        if 'init_attribution' in kwargs:
            for id in kwargs['init_attribution']:
                self.attribution_dict[id].set_owner(self.id,**(kwargs['init_attribution'][id]))

        
    #这个是权宜之计
    def after_change_attribution_dict(self):
        temp = copy.deepcopy(attribution_model_dict)
        for id in temp:
            temp[id].set_owner(self.id)
        for id in self.attribution_dict:
            if id not in temp:
                self.attribution_dict[id].attach_to_level(0)
                continue
            #转移信息+全部注销一次
            temp[id].set_owner(self.id,**(self.attribution_dict[id].dict_out_data()))
            self.attribution_dict[id].attach_to_level(0)

        self.attribution_dict = temp
        del temp

    def after_deepcopy(self):
        #如果自己和全局字典的内容不一样
        self.refresh_id()
        for id in self.attribution_dict:
            self.attribution_dict[id].set_owner(self.id)

    def act(self,action_id,world_status):
        universal_id_dict[action_id].do(self.id,world_status)

    #attach系列函数稍后实现
