#WAP to search for a substring within a main string

statement = "hello,how is python learning going on"
a = input("Enter the substring to search = ")
if(a in statement):
    print("It is present in main string")
else:
    print("it is not present in main string")
