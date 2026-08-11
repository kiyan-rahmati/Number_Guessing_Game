"""
This is a simple number guessing game where the user can choose a difficulty level and try to guess a randomly generated number.
The user has a limited number of attempts to guess the correct number, and the game provides feedback on whether the guess is too low or too high.
The user can choose to play again after each round, and their score is tracked throughout the game.
"""

import random

score = 0

def main():
    """
    Main function to run the guessing game.
    """
    # Ask the user to choose a level and generate a random number based on that level
    while True:
        rand_num = generate_level()

        res = game(rand_num)
        match res:
            case None:
                break
            case "continue":
                continue

       
def game(rand_num):
    """
    Run the guessing game.
    """
    # Start the game and ask the user to guess the number
    global score
    mistake = 0
    while mistake < 5:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        except KeyboardInterrupt:
            print("\nGoodbye!")
            return None 

        if is_answer(rand_num, guess):
            print("You guessed it right!")
            score += 1

            # Ask the user if they want to play again
            q = input("Do you want to play again? (y/n): ").strip().lower()
            if q == "y":
                return "continue"
            elif q == "n":
                print(f"Your score is: {score}")
                return None                
        else:
            mistake += 1
            if guess < rand_num:
                print("Your guess is too low.\n")
                continue 
            elif guess > rand_num:
                print("Your guess is too high.\n")
                continue

    # If the user has used all their attempts, print the correct number and break the loop
    if mistake == 5:
        print(f"You have used all your attempts. The correct number was {rand_num}.")
        return None
                    

def generate_level():
    """
    Generate a random number based on the level chosen by the user.
    """
    while True:
        try:
            level = int(input("\nChose level: " \
            "\n1.Easy " \
            "\n2.Medium " \
            "\n3.Hard " \
            "\n4.Iran " \
            "\nPlease enter just the number(1-4): "))
        except ValueError:
            print("\nPlease enter a valid integer.")
            continue
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


        # Generate the random number with level that givan from user
        match level:
            case 1:
                rand_num = generate_random_number("Easy")
            case 2:
                rand_num = generate_random_number("Medium")
            case 3:
                rand_num = generate_random_number("Hard")
            case 4:
                rand_num = generate_random_number("Iran")
            case _:
                print("\nTry again, Please")
                continue

        if rand_num is None:
            print("\nTry again, please")
            continue

    return rand_num


def generate_random_number(level):
    """
    Generate a random number based on the level chosen by the user.
    """
    # Make random number with the title form of level if the level is valid
    if level.title() in ["Easy", "Medium", "Hard", "Iran"]:
        match level:
            case "Easy":
                num = random.randint(0, 10)
            case "Medium":
                num = random.randint(0, 100)
            case "Hard":
                num = random.randint(0, 1000)
            case "Iran":
                num = random.randint(-1000, 1000)
    else:
        return None 

    # Return the level 
    return num


def is_answer(rand_num, guess):
    """
    Check if the user's guess is correct.
    """
    # Check if the user's guess is correct
    return rand_num == guess

    
if __name__ == "__main__":
    main()
