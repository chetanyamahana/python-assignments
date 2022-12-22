gross_inc = float(input("Enter the gross income: "))
dependents = int(input("Number of dependents: "))
std_deduction = 10000
depn_deduction = 3000
taxable_inc = gross_inc - std_deduction - (depn_deduction*dependents)
tax = taxable_inc*0.2
print("Tax: ", tax)
print("Taxable income: ",taxable_inc)
