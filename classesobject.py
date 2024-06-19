# Class is a blueprint of object
# Object is an instance of a class

class Person:
    #Properties/Variables/Characteristics/Attributes
    name = "James"
    age = 45
    gender = "Female"

    #Methods/Function/Behavior
    def move(self):
        print("Person is walking")

farmer = Person()
farmer.move()
print(farmer.gender)