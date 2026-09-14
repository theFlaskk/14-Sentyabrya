class SingletonFive():
    __instances = []
    
def __new__(cls, *args, **kwargs):
        if len(cls.__instances) < 5:
            obj = super().__new__(cls)
            cls.__instances.append(obj)
            return obj

        return cls.__instances[-1]

def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]