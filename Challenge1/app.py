import random

def guess_game():
    min_val = 1
    max_val = 25
    random_number = random.randint(min_val, max_val)
    attempts = 0
    guess = None
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"Guess the number between {min_val} and {max_val}!")

    while guess != random_number:
        try:
            guess_input = input("Please enter your number: ")
            guess = int(guess_input)
            attempts += 1

            if guess < random_number:
                print("The number you entered is below the random number.")
            elif guess > random_number:
                print("The number you entered is above the random number.")
        except ValueError:
            print("Please enter a number!")
        
    print(f"Congratulations! You have guessed the correct number.")


if __name__ == "__main__":
    guess_game()
