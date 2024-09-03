a = input("Enter the string = ")
b = []

for x in a:
    b.append(x)

b.reverse()

for i in range (0,len(b)):
    c = "".join(b)

if a == c:
    print("it is palindrom")
else:
    print("not a plaindrom")




