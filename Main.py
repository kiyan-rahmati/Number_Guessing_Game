import random

score = 0

def main():
    """
    Main function to run the guessing game.
    """
    # Ask the user to choose a level and generate a random number based on that level
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
        if level == 1:
            rand_num = generate("Easy")
        elif level == 2:
            rand_num = generate("Medium")
        elif level == 3:
            rand_num = generate("Hard")
        elif level == 4:
            rand_num = generate("Iran")
        else:
            print("\nTry again, please")
            continue
        if rand_num is None:
            print("\nTry again, please")
            continue

        value = game(rand_num)
        if value is None:
            break
        elif value == "continue":
            continue
       
def game(rand_num):
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
                    

def generate(level):
    """
    Generate a random number based on the level chosen by the user.
    """
    # Make random number with the title form of level if the level is valid
    if level.title() in ["Easy", "Medium", "Hard", "Iran"]:
        if level == "Easy":
            num = random.randint(0, 10)
        elif level == "Medium":
            num = random.randint(0, 100)
        elif level == "Hard":
            num = random.randint(0, 1000)
        elif level == "Iran":
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
