class Person:

    name = ""
    age = 0
    sex = ""
    def __init__(self, Name, Age, Sex):
        print("Parent Cons is invoked...")
        self.name = Name
        self.age = Age
        self.sex = Sex

    def walking(self):
        print(self.name + " is walking....")
        # def walking(self):
        #     print(self.name + 'is reading')


class Student(Person):

    regNo = 0
    jYear = 0
    dep = ""
    def __init__(self,Name,Age,Sex,RegNO, Jyear, Dep):
        super().__init__(Name, Age, Sex)
        print("Child cons is invoked....")
        self.dep = Dep
        self.jYear = Jyear
        self.regNo = RegNO

    def printStudentDetails(self):
        print(self.name +"\n"+ str(self.age) +"\n"+ self.sex +"\n"+str(self.regNo) +"\n"+ str(self.jYear) +"\n"+ self.dep)


s1 = Student("Balaji", 29, "M", 123, 2019, "MEch")
s1.printStudentDetails()

s2=Person("dada", 0 ," ")
s2.walking()

