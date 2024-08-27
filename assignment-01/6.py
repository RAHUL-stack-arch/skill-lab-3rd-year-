#swapping with 3rd number
a = int(input("input the number in a : "))
b = int(input("input the number in b : "))
print(f"num1 = {a}")
print(f"num2 = {b}")
c = a
a = b
b = c
print("after swap")
print (f"num1 = {a}")
print(f"num2 = {b}")


#swapping without 3rd number
print("swapping without 3rd var")
a = a+b
b = a-b
a = a-b
print (f"num1 = {a}")
print(f"num2 = {b}")

