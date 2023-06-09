import restart as res
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
#
def blood_steal_realize(owner,repeat,world_status):
    if world_status['event_id_now'] == after_attack.id:
        if world_status['attacker'] == owner:
            res.universal_id_dict[owner].attribution_dict[hp.id].add_value(world_status['damage'],world_status)
    return 0,world_status
#
blood_steal_atom = res.atom(blood_steal_realize)
#
def damage_settlement(owner,repeat,world_status):
    if world_status['event_id_now'] == attack.id:
        res.universal_id_dict[world_status['attackee']].attribution_dict[hp.id].add_value(-world_status['damage'],world_status)
    return 0,world_status
#
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