class Mobile:
    Brand = ""
    Model = ""
    Size = 0.0
    Color = ""

    def run(self):
        print (self.Brand + " Is a good Phone")

Mob = Mobile()
Mob.Brand = "Samsung"
Mob.Model = "M30"
Mob.Size = "6.2"
Mob.Color = "White"
Mob.run()

print(Mob.Brand,Mob.Model,Mob.Size, Mob.Color)

# class Mobile:
#     Brand = ""
#     Color = ""
#
#     def __init__(self, brand, color):
#         print("My paramatized constructor")
#         self.Brand = brand
#         self.Color = color
#
#     def run(self):
#         print(self.Brand + "is a good mobile")
#
#     def returnBrand(self):
#         print('{} is {} nice'.format(self.Brand,self.Color))
#
# samsung = Mobile("samsung","red")
# print(samsung.Brand,samsung.Color)
# samsung.run()
# samsung.returnBrand()
