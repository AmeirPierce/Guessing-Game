import random

# Setup
secret_num = random.randint(1, 10)
attempt = 0
max_tries = 5
guessed = False

# Game loop
while attempt < max_tries:
    choice = int(input("I'm thinking of a number between 1 and 10. Can you guess it? 😜 "))

    attempt += 1

    if choice == secret_num:
        print("NICE TRY 🤪 You got it!")
        guessed = True
        break
    elif choice < secret_num:
        print("Too low! You are SOOOO close 😂")
    else:
        print("Too high! You are SOOOO close 😂")

# Final message
if not guessed:
    print(f"BETTER LUCK NEXT TIME LITTLE BRO 😝 The number was {secret_num}")
else:
    print(f"You won in {attempt} tries! 🥳")


