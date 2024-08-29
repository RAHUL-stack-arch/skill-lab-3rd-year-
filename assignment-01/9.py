#Calculate the Gross salary of an employee (Input Basic salary, TA, DA and HRA from the
#keyboard)

basic_sal = float(input("Enter the salary = "))
ta = float(input("Enter the ta = "))
da = float(input("Enter the da = "))
hra = float(input("Enter the hra = "))
print(f"The gross salary = {basic_sal + ta + da + hra}")

