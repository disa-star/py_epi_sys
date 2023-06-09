
import numpy as np

# Example two-dimensional NumPy array
arr = np.array([[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]])

# Convert the array to a dictionary
d = {}
for row in arr:
    if row[0] not in d:
        d[row[0]] = [row[1]]
    else:
        d[row[0]].append(row[1])

print(d)



'''# 半血狂暴(攻击者p1看到被攻击者p2半血后伤害加倍)
import restart as res
import copy

# 初始设置：时机,人物和属性
attack = res.event()
get_hurt = res.event()
hp = res.attribution(valuable = True, limit = [0,20], value = 20)
melee = res.attribution(valuable = True, limit = [0,20],value = 10)

def half_blood(owner,repeat,world_status): 
    if world_status['event_id_now'] == attack.id:
        if world_status['attackee'] == owner:
            blood = res.universal_id_dict[owner].attribution_dict[hp.id].limit[-1]
            res.universal_id_dict[owner].attribution_dict[hp.id].add_value(-world_status[
                'damage'],world_status)
            if res.universal_id_dict[owner].attribution_dict[hp.id].value <= 1/2 * blood:
                return 0,world_status
    return 0,world_status
half_blood_atom = res.atom(half_blood)
def half_blood_anger(owner,repeat,world_status):
    if world_status['event_id_now'] == get_hurt.id:
        res.universal_id_dict[owner].attribution_dict[melee.id].add_value(
        res.universal_id_dict[owner].attribution_dict[melee.id].value,world_status)
    return 0,world_status
anger_atom = res.atom(half_blood_anger)

do_attack = res.action(reg_atom_dict={attack.id:[half_blood_atom.id]},event_list=[
    attack.id,get_hurt.id])

half_blood_angry = res.attribution(valuable = False, reg_atom_dict={get_hurt.id:[anger_atom.id]})


player = res.unit(init_attribution ={hp.id:{'value':20,'limit':[0,20],'attach_ctn':1},
                                    melee.id:{'value':10,'attach_ctn':1}})
p1 = copy.deepcopy(player)
p1.after_deepcopy
#p1.after_change_attribution_dict()
p1.attribution_dict[half_blood_angry.id].attach()
p2 = copy.deepcopy(player)
p2.after_deepcopy

p1.act(do_attack.id,{'attacker':p1.id,
                    'attackee':p2.id,
                    'damage':p1.attribution_dict[melee.id].value})

#print(p1.attribution_dict[hp.id].__dict__)
print(p2.attribution_dict[hp.id].__dict__)'''