import math

a = int(input("Enter the principle = "))
b = int(input("Enter the rate = "))
c = int(input("Enter the time in years = "))

print(f"Simple interest = {(a*b*c)/100}")
print(f"Compound interest = {float((a * math.pow((1 + b * 0.01),c)) - a): .2f}")