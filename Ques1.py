bill = float(input("Enter total restaurant bill: "))
tip_percentage = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = bill * tip_percentage / 100
total_bill = bill + tip
each_person = total_bill / people

print("Total Tip:", tip)
print("Total Bill including Tip:", total_bill)
print("Each Person Pays:", each_person)