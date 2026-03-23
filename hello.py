import random

secret_pin = random.randint(1, 10)
attempt = 0

print("Let us play a game were you will try to guess a number i have in mind")
print("If you guess it right you win!")

while True:
    try:
        guess = int(input("Guess: "))
        attempt += 1
        if guess == secret_pin:
            print(f"You are correct!, You won after {attempt} attempt(s)")
            break

        elif guess < secret_pin:
            print("Number is too low")
        elif guess > secret_pin:
            print("Number is too high")
        else:
            print("Please enter a valid Number")

    except ValueError:
        print("Invalid input")
