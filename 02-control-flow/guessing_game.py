import random
secret = random.randint(1, 100)
attempts = 0

print("I am thinking of a number between 1 and 100. Guess the secret number!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Congrats! You guessed the right number after {attempts} tries!")
        break



