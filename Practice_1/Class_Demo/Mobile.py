class Mobile:
    x=""
    y=0.0
    z=""
    # def __init__(self):
    #         print("hi")
    def __init__(self,Brand,Size,Color):
        # print("parameterized constructor")
        self.x=Brand
        self.y=Size
        self.z=Color
    #
    def returnsize(self):
        print('{} is {} inch and it is {} in color'.format(self.x,self.y,self.z))
    # def color(self):
    #     print('it is red {}'.format(self.z))
#
mob1=Mobile("honor", 6.5,"red")
mob1.returnsize()
# mob1.color()

# mob3=Mobile("Nokia",6,"blue")
# mob3.returnsize()
#
# mob2= Mobile()
# mob2.x="samsung"
# mob2.y=5.5
# mob2.z="red"
# mob2.returnsize()
# print(mob2.x + ' '+ 'is'+' ' + str(mob2.y) + ' '+'inch.'+' '+ 'it is'+' '+ mob2.z)
