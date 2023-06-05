
import pickle
import restart as res


#attack = res.event()

'''
with open("my_function.pickle", "wb") as f:
        pickle.dump(attack, f)

'''
with open("my_function.pickle", "rb") as f:
    ddd = pickle.load(f)
res.universal_id_dict[ddd.id]=ddd

print(ddd.id)
universal_id_dict ={1:3}
res.universal_id_dict = {2:45}


ddd.test()



print(res.universal_id_dict)
ddd = 666
print(res.universal_id_dict)


##
#
#
'''
with open("my_function.pickle", "rb") as f:
    ddd = pickle.load(f)
ddd.on_load()
'''
