class Device:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom

    def crash(self):
        print(self.model,"has crashed")

computer = Device("HP",2008)
computer.crash()
laptop = Device("Lenovo",2009)
laptop.crash()


