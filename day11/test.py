class TheThing():
    def __init__(self):
        self.name = str(self) #此处想获得赋值对象的名称
        print(self.name)

a = TheThing()