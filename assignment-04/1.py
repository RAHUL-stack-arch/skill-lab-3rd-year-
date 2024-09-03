a = input("Enter the string = ")

b = []

for x in a:
    if x in b:
        print(f"{x} is duplicate")
    b.append(x)