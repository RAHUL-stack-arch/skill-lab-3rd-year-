days = int(input("Enter the number of days = "))
print(f"{float(days/365): .0f} year {float((days%365)/30): .0f} month {((days%365)%30)} days")