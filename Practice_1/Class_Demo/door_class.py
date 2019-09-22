class door:
    # color=""
    # type=""
    # height=0.0
    # lock=""
    def __init__(self,Color,Type,Height ,Lock):
        # print("hi")
        self.color=Color
        self.type=Type
        self.height=Height
        self.lock=Lock
    def door1(self):
        print('it is a {} color door with {} type and height is {}'.format(self.color,self.type , self.height))
        # print('it is a jj color with wood type')
    def door2(self):
        print('This door is {}'.format(self.lock))
    def door3(self):
        print('it is {} color and  {} type with {} inch height'.format(self.color,self.type,self.height))

offie_door1=door("red","iron",8.5," ")
offie_door1.door1()
offie_door2=door(" " ," ",0.0,"locked")
offie_door2.door2()

school_door=door("pink","fiber",10.34," ")
school_door.door1()
offie_door3=door("yellow" ,"fiber",5.9," ")
offie_door3.door3()
school2_door=door("white","plastic",8.8," ")
school2_door.door1()
