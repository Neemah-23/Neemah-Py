# Datatype

number = 78 # Int
num = 45.09 # Float
greeting = "How are you doing?" # str
Is_Programming_Interesting = True # bool
devices = ["laptop","computer","tablet","phone"] # List
browser = ("opera","firefox","safari","brave") # Tuple
countries = {"Uganda","Tanzania","Kenya"} # Set
employee = {
    "firstname" : "Jane",
    "age" : 29,
    "nationality" : "Kenyan",
    "emailaddress" : "jane@gmail.com"
} # Dictionary

print(Is_Programming_Interesting)
print(num)
print(countries)
print(employee["firstname"])

# Determining a datatype
print(type(countries))
print(type(employee))


# Typecasting is the process of converting one data type to another
print(int(num))
print(float(number))