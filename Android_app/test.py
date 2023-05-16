'''
import pickle

def func():
     global a
     print(f'在func中的global a为{a}')

a = 0
if 1 == 1:
    #必须要确保 定义的类和即将要加载的类是一致的
    class test():
        def __init__(self):
            global a
            #pickle会在一开始记住init的部分和self的子属性
            self.a = a
            global func
            self.func = func
        def print(self):
            #这里pickle哪怕在没有global的时候都会记住global a
            #并且 必须要是a这个变量才能使用
            global a
            print(f'self.a={self.a}\n     a={a}')
else:
    class test():
        pass

if 1 == 0:
    a = 123
    
    
    my_function = test()
    with open("my_function.pickle", "wb") as f:
        pickle.dump(my_function, f)
    del my_function
    def my_function():
        pass

with open("my_function.pickle", "rb") as f:
    ld = pickle.load(f)

print(ld)
for a in range(0,5):
    #a = 2
    ld.print()
ld.func()
'''
a = {1:2,3:4}
print(a[1])

import numpy as np

a = np.array([1,3,4])
print(np.percentile(a,50))