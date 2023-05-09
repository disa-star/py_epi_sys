import pickle

a = 0
class test():
        def __init__(self):
            global a
            #pickle会在一开始记住init的部分和self的子属性
            self.a = a
        def print(self):
            #这里pickle哪怕在没有global的时候都会记住global a
            #并且 必须要是a这个变量才能使用
            global a
            print(f'self.a={self.a}\n     a={a}')


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
