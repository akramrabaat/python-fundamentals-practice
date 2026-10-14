secret_number = 42
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Invalid number! Try again.")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print("Game Over! You lost.")