# Guess the Number

## Description

Guess the Number is a simple command-line game written in Python. The player selects a difficulty level, and the program generates a random number within a specific range. The goal is to guess the correct number before running out of attempts.

The game includes four difficulty levels:

* **Easy:** Random number between **0 and 10**
* **Medium:** Random number between **0 and 100**
* **Hard:** Random number between **0 and 1000**
* **Iran:** Random number between **-1000 and 1000**

The player has **five attempts** to guess the correct number. After each incorrect guess, the program tells the player whether the guess is too high or too low. If the player guesses correctly, their score increases and they can choose to play another round. If all five attempts are used, the correct number is revealed and the game ends.

The project is divided into two files:

* **Main.py** contains the game logic, including user interaction, random number generation, and answer checking.
* **Test_Main.py** contains automated tests written with **pytest** to verify that the functions behave correctly.

## Functions

### `generate(level)`

Generates a random integer according to the selected difficulty level.

Supported levels:

* Easy
* Medium
* Hard
* Iran

If an invalid level is provided, the function returns `None`.

### `is_answer(rand_num, guess)`

Compares the generated number with the player's guess and returns:

* `True` if the guess is correct.
* `False` otherwise.

### `main()`

Runs the complete game by:

1. Asking the player to choose a difficulty.
2. Generating a random number.
3. Allowing up to five guesses.
4. Giving feedback after each incorrect guess.
5. Tracking the player's score.
6. Asking whether the player wants to play another round.

## Testing

The project uses **pytest** for testing.

The tests verify:

* Valid difficulty levels generate numbers within the correct ranges.
* Invalid difficulty levels return `None`.
* The `is_answer()` function correctly identifies correct and incorrect guesses.

Run the tests with:

```bash
pytest Test_Main.py
```

## Requirements

* Python 3.11
* pytest (for running the tests)

Install pytest if needed:

```bash
pip install pytest
```

## Project Structure

```text
. 
├── Main.py 
├── Test_Main.py 
├── requirements.txt 
└── README.md
```

## Notes

This project was created as a simple practice exercise to improve Python programming skills. It demonstrates the use of functions, loops, conditionals, exception handling, random number generation, and basic unit testing with pytest.
