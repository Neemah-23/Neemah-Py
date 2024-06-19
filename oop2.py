class Car:
    def __init__(self,model,color,manufacturer,yop):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yop

    def speed(self):
        print("The manufacturer of",self.model,"is", self.manufacturer)

car1 = Car("M12","white","BMW",2024)
car1.speed()
car2 = Car("M12","black","Lexus",2022)
car3 = Car("M12","grey","Mercedes",2017)
car4 = Car("M12","salmon","Toyota",2014)

