a = input("Enter a string = ")

b = '''!()-[]{};:'"\,<>./?@#$%^&*_+~'''

for x in b:
    if x in a:
        print("not valid")