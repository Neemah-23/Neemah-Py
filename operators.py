# Arithmetic Operators - Simple Calculation
num1 = 56
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2) # Modulus returns the remainder after division

# Comparison operators - Compare values.
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) # Equal to
print(num1 != num2) # Not equal to

# Assignment operators -    used to assign values to variables
a = 200
print(a)
a += 20
print(a)

# Logic operators - and, or, not
x = 100
print( x < 250 and x > 1000)
print( x < 250 or x > 1000)
print( not(x < 250 or x > 1000))

# Operator precedence - Order in which operations get executed

output = ( 100-4 * 3/1)
print(output)
print(int(output))

# Write a simple python programme that returns the area of a trapezium

# A = 1/2*(a+b)*h

a = 18
b = 24
h = 4
Area = 1/2*(a+b)*h
print("The area of the trapezium is",Area)