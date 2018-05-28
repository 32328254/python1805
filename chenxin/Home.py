#! /usr/bin/evn python3
#coding=utf-8

class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_item = []

    def __str__(self):
        msg = "all area is %s"%self.area
        msg += "left area is %s"%self.left_area
        msg += "home's info is %s"%self.info
        msg += "home's address is %s"%self.addr
        msg += "home has items: %s"%(str(self.contain_item))
        return  msg

    def add_item(self,item):
        self.left_area -= item.get_area()
        self.contain_item.append(item.get_name)

class Bed:
    def __init__(self,new_name,new_area):
        self.area = new_area
        self.name = new_name

    def __str__(self):
        return "%s area is %d"%(self.name,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name


fangzi = Home(120,"three room","beijing")
print fangzi

bed1 = Bed("ximeng",4)
print bed1
fangzi.add_item(bed1)
print fangzi

bed2 = Bed("mengjia",6)
print bed2
fangzi.add_item(bed2)
print fangzi