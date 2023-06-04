# python项目报告

## **Section I** 立项缘由

TRPG是指桌上角色扮演游戏（Tabletop Role-playing game）的缩写，是一种以对话和想象为主要手段的角色扮演游戏。TRPG最早起源于20世纪70年代的美国，随后传入日本并在日本得到了广泛的发展和推广。TRPG的玩家通常会扮演一个虚构的角色，通过对话和想象来完成游戏中的任务和冒险。TRPG通常需要一些特殊的骰子来决定游戏中的随机事件和结果。

一场典型的TRPG游戏往往涉及到以下几点:
- 玩家之间交互
- 主持人与玩家的交互
  - 主持人询问玩家的决策
  - 主持人汇报玩家行动的结果
  - 主持人播报玩家所处的环境和遭遇
  - 主持人生成骰子的判定
- 主持人记录玩家的数值信息
  - 记录玩家拥有的装备
  - 记录玩家的数值信息
  - 记录玩家的属性信息

然而，主持人一个人需要处理和多个玩家的交流，并且记录每个玩家所控制角色的状态，这个任务工作量大且不说，主持人容易因为疏忽和遗忘从而给玩家造成不好的游戏体验。同样，主持人判定与数值有关的事件时也容易出现运算速度较慢的情况，因此，我们组想就此开发一个帮助主持人推进TRPG游戏进行的辅助工具

---

## **Section II** 项目目标

我们为实现一个**好用的**主持人辅助工具，我们需要从下面的方面着手
- 便于主持人快速地操作(因此我们需要一个GUI)
- 这个工具理应适用于大部分的TRPG游戏(因此需要编辑器界面)

因此，本项目按照用户使用可以被分成
- 操作界面
  - 能够快速地进行各种角色之间的数值操作(比如以攻击力造成伤害)
  - 能够进行一些直接的改动(如修改血量攻击力)
  
- 编辑界面
  - 能够自定义事件
  - 能够自定义角色
  - 能够自定义角色有多少属性和数值

## **Section III** 项目实现

因为我们需要能够实现更为自由的TRPG规则构建并且快速获得信息回报，我们讲此处的项目实现分为三个部分
- 逻辑后端: 负责构建一个可扩展性强的组织方式
- qq机器人端: 负责连接qq发送消息
- web端: 负责提供便于操作的GUI并连接上述所有部分

### **Part I** 逻辑后端部分实现

逻辑后端实现了五大类
- 所有类共有的属性和方法
  - 一个以字典方式存储的描述(便于被web端使用)
  - 一个永远不重复的id
  - 全局共享一个 **id->对象内存地址** 的映射表
- atom类
  - 此类用于存放实现逻辑处理的函数
  - 其中的函数负责处理world_status字典
- event类
  - 此类用于储存由atom所存储的函数的列表
  - 在使用event.run()方法的时候，该类会依次调用所有他存储的函数
- attribution类
  - 此类用于存储所有的附着在人物身上的属性
  - 有数值属性如血量防御力等，也有非数值属性如中毒亢奋等
  - 可以存储一个由event构成的列表，在数值改变的时候，对这个列表的每个event依次使用event.run()
- action类
  - 此类用于存储一个执行的动作
  - 负责存储一个event构成的列表，在使用action.do()的时候依次对其中的event使用event.run()
  - 负责生成world_status
- unit类
  - 负责挂载许多attirbution的深拷贝
  - 是执行action的主体

使用例:
```python
import copy
#定义atom末位为00
#event为01
#action为02
#attribution为03
#unit为04
attack = res.event()
after_attack = res.event()
hp = res.attribution(valuable=True,limit=[0,20],value=10)
melee = res.attribution(valuable=True,limit=[0,999],value=5)

def blood_steal_realize(owner,repeat,world_status):
    if world_status['event_id_now'] == after_attack.id:
        if world_status['attacker'] == owner:
            res.universal_id_dict[owner].attribution_dict[hp.id].add_value(world_status['damage'],world_status)
    return 0,world_status
blood_steal_atom = res.atom(blood_steal_realize)
def damage_settlement(owner,repeat,world_status):
    if world_status['event_id_now'] == attack.id:
        res.universal_id_dict[world_status['attackee']].attribution_dict[hp.id].add_value(-world_status['damage'],world_status)
    return 0,world_status
damage_atom = res.atom(damage_settlement)

do_attack = res.action(reg_atom_dict={attack.id:[damage_atom.id]},event_list=[attack.id,after_attack.id])

player = res.unit(init_attribution = {hp.id:{'value':21,'limit':[0,35],'attach_ctn':1},
                                      melee.id:{'value':7,'attach_ctn':1}})
p1 = copy.deepcopy(player)
p1.after_deepcopy()

blood_steal = res.attribution(valuable=False,reg_atom_dict={after_attack.id:[blood_steal_atom.id]})
p1.after_change_attribution_dict()

p1.attribution_dict[blood_steal.id].attach()
p2 = copy.deepcopy(player)
p2.after_deepcopy()
p1.act(do_attack.id,{'attacker':p1.id,
                     'attackee':p2.id,
                     'damage':p1.attribution_dict[melee.id].value})
print(p1.attribution_dict[hp.id].__dict__)
print(p2.attribution_dict[hp.id].__dict__)
```

>以上的代码实现了*吸血* 的效果，p1用攻击力对p2造成了伤害，并且p1恢复了相当于造成伤害量的血量

