
# Parent Class/Base class/Super class
class Animal:
    hasScales = True

    def sound(self):
        print("Animal is speaking")

 # Child Class/Sub Class/Derived Class
class Duck(Animal):
     hasWebbedFeet = True

     def move(self):
         print("Duck is swimming")

class Caterpillar(Duck):
     def move(self):
         print("Caterpillar is wriggling")

a = Animal()

d = Duck()

c = Caterpillar()
c.