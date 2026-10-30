def calculate_tip(bill, percent=15):
    tip_amount = bill * (percent / 100)
    return tip_amount

def calculate_total(bill, tip_amount):
    total = bill + tip_amount
    return total

bill = float(input("How much was the bill? "))

percent_text = input("Tip percentage (press Enter for 15%): ")

if percent_text == "":
    tip = calculate_tip(bill)
else:
    tip = calculate_tip(bill, float(percent_text))

total = calculate_total(bill, tip)

print(f"Your tip is ${tip:.2f} and your total is ${total:.2f}")
