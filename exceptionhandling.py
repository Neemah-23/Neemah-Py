try:
    x = 20
    print(x)
except:
       print("An error occurred")

finally:
       print("Success")

num1 = 39
num2 = 13
try:
  print(num1/num2)
except :
   print("ZeroDivision error occurred")
finally:
   print("Success")
