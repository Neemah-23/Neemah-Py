# A python programme to check whether a number is prime or not

num = int(input("Enter num:"))
NUMBER_BOOL = False
if num == 1:
   print("not  prime number.")
elif num > 1:
   for i in range(2,num):
      if (num % i) == 0:
         NUMBER_BOOL = True
         break

if NUMBER_BOOL:
   print("not prime")
else:
   print("prime")

