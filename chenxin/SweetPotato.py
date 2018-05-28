#! /usr/bin/evn python3
# coding=utf-8

class SweetPotato:
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = " shengde"
        self.condiments = []

    def __str__(self):
        return "potato state is %s(%d),add condiments are %s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cooked_time):
        self.cookedLevel += cooked_time
        if self.cookedLevel >=0 and self.cookedLevel < 3:
            self.cookedString = "shengde"
        elif self.cookedLevel >=3 and self.cookedLevel < 5:
            self.cookedString = "bansheng"
        elif self.cookedLevel >=5 and self.cookedLevel <= 8:
            self.cookedString = "shule"
        elif self.cookedLevel > 8:
            self.cookedString = "hule"

    def addCondiments(self,item):
        self.condiments.append(item)


digua = SweetPotato()
print(digua)

digua.cook(1)
print(digua)
digua.addCondiments("dasuan")
digua.cook(1)
print(digua)
digua.addCondiments("tang")
digua.cook(1)
print(digua)
digua.addCondiments("yan")
digua.cook(1)
print(digua)
digua.addCondiments("lajiao")
digua.cook(1)
print(digua)
digua.addCondiments("ziran")
digua.cook(1)
print(digua)

digua.cook(1)
print(digua)

digua.cook(1)
print(digua)

digua.cook(1)
print(digua)

digua.cook(1)
print(digua)

digua.cook(1)
print(digua)


