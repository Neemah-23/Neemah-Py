temperature = 29

if temperature < 25:
    print("It is cold")

elif temperature > 25:
     print("It is hot")

else:
     print("Normal temperature")


# A simple program to return the largest number among three numbers
first = 90
second = 45
third = 60

if first > second and first > third:
    print(first,"is the largest number")
elif second > first and second > third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")

# Write a python programme that checks whether a number is even or odd

num = 20

if num % 2 == 0:
    print(num,"is even")

else:
    print(num,"is odd")
