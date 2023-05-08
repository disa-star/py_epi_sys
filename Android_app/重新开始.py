class event():
    def __new__(cls,*args,**kwargs):
        return object.__new__(cls)
    def __init__(self,*args,**kwargs):
        