class Person:
    Name = ""
    Age = 0
    Sex = ""
    Height = 0.0

    def __init__(self):
        print("Default Constructor")

    # def __init__(self, name, age):
    #     print("My Parameterized constructor")
    #     self.Name = name
    #     self.Age = age


    def walking(self):
        print(self.Name + " is walking currently")
    def info(self):
        print(self.Name +' '+ 'is studying' +' '+'and his age is:'+ str(self.Age))
    #
    # def returnAge(self):
    #     print('{} is {} years old'.format(self.Name, self.Age))


Faizal = Person()
Faizal.Name = "Faizal"
Faizal.Age = 29
Faizal.walking()

# Manas = Person("Manas", 32)
# # Manas.Sex = 'Male'
# Manas.returnAge()
#
# Rakesh = Person("Rakesh", 32)
# # Rakesh.Sex = 'Male'
# Rakesh.returnAge()

# balaji = Person()
# balaji.name = "bala"
# balaji.age = 30
# balaji.sex = "Male"
# balaji.Height = 5.11
# balaji.walking()
Ram=Person()
Ram.Name="sriram"
Ram.Age=26
Ram.info()






