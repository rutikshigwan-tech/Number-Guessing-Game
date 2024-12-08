from random import randint 

random_number = randint(1, 10) # Generate a random number between 1 and 10

chance = 1 # Start with the first chance

while chance <= 3:
    guess = int(input(f"Chance {chance} - Guess a number between 1 and 10: "))
    # Check if the guess is correct
    if guess == random_number:
        print("Congrats!! You guessed the correct number!")
        break  # Exit the loop since the user guessed correctly
    else:
        # If it's the last chance, inform the user
        if chance == 3:
            print("Sorry, that was your last chance. The correct number was:", random_number)
        else:
            print("Try again...")

    chance += 1  # Increment the chance after each guess

print("Thank you for playing!")
