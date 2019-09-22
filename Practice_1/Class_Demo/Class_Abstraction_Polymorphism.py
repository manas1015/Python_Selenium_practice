
class Cars:

    def __init__(self, name):
        self.name = name

    #Abstract method
    def drive(self):
        raise NotImplementedError("Sub class must be implemnt the drive method")


class ElectricCar(Cars):

    def drive(self):
        print( self.name +" Electric Car is driving")
    def save(self):
        print(self.name +'Electric car saves petrol')


class SportsCar(Cars):

    def drive(self):
        print(self.name + " Sports car is running...")

eCar = ElectricCar('Maruti')
eCar.drive()
eCar.save()
sCar = SportsCar("ferrari")
sCar.drive()




#
# car1 = Cars("Maruti")
# car1.drive()