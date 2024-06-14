 #Inbuilt functions

y = min(23,56,1000,5643)
print("The minimum number is",y)

x =max(90,2,79,14)
print("The maximum number is",x)

z = pow(2,3)
print(z)

# User-defined Functions

def school():
    print("eMobilis")

school() # Calling a function

def multiply():
    num1 = 5
    num2 = 6
    print(num1 * num2)
multiply()

# Parameters and arguments
def add(a,b):
    print(a + b)
add(5,6)
add(10,6)
add(5,10)
add(9,7)

def Employee(fullname,age,salary,contact,position):
    print(fullname,age,salary,contact,position)
Employee("Job Kamau",45,500000,57008311,"MD")
Employee("Grace Chebet",34,500000,57008311,"MD")
Employee("Shantel Makena",18,500000,12174257,"MD")
Employee("Carlos Pyeko",21,500000,58170654,"MD")
