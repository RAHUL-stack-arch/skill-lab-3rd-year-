city = {"bokaro","ranchi","bhubneswar","kolkata"}

a = input("input to search that it is present or not in set city")
i=0
for x in city:
    if(x == a):
        print(f"{a} is present")
        i = i+1
        break
if(i == 0):
    print(f"{a} is not present")

