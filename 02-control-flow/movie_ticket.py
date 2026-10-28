age = int(input("Hey welcome to the movies! To start off, enter your age:"))
student = input("And are you a student? (y/n): ").strip().lower()

is_student = student == 'y'

if age < 12:
    print("Your ticket costs $8!")
elif age >= 65:
    print("Your ticket costs $9!")
elif is_student:
    print("Your ticket costs $11!") 
else:
    print("Your ticket costs $15!")