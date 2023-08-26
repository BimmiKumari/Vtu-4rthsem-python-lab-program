#funtion declaration
def fn(n):
 if n == 1:
  return 0
 elif n == 2:
  return 1
 else:
   return fn(n - 1) + fn(n - 2)


#main program & function call
num = int(input("Enter a Number:"))
if num > 0:
 print("fibbo sum is ", fn(num))
else:
 print("Error in input")
