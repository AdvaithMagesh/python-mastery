bill = float(input("How much was the bill?"))
tip_percent = float(input("How much would you like to tip?"))

tip = bill * (tip_percent / 100)
total = bill + tip
print(f"Your tip will be ${tip:.2f} and your total is ${total:.2f}")