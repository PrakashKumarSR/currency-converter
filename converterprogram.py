# currency_converter.py

with open('currencydata.txt') as f:
    lines = f.readlines()

currencydict = {}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]] = parsed[1]

amount = int(input("Enter amount in INR:\n"))

print("Available currencies:")
[print(item) for item in currencydict.keys()]

currency = input("Please enter the name of the currency to convert to:\n")

converted_amount = amount * float(currencydict[currency])
print(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
