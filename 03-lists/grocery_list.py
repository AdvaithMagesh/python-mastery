print("Let's make your list of groceries! Type 'done' when you're finished.")
groceries = []
while True:
    item = input("Add your item: ").strip().lower()
    if item == "done":
        break
    elif item in groceries:
        print("Already on your list!")
    else:
        groceries.append(item)

for i, item in enumerate(groceries, start=1):
    print(f"{i}. {item}")
