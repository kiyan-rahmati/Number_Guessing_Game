import random
import os


HIGH_SCORE_FILE = "highscore.txt"


def load_high_score():
    """Load high score from file."""

    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    """Save high score to file."""

    try:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))
    except OSError:
        print("Could not save high score.")


def clear_screen():
    """Clear terminal screen."""

    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    """Show game banner."""

    print("""
╔══════════════════════════════════════╗
║          🎯 NUMBER GUESSER           ║
║             PYTHON GAME              ║
╚══════════════════════════════════════╝
""")


def get_integer(prompt):
    """Get a valid integer from user."""

    while True:
        try:
            value = input(prompt).strip()

            if value.lower() == "q":
                return None

            return int(value)

        except ValueError:
            print("❌ Please enter a valid integer or q.")


def generate_random_number(level):
    """Generate number based on difficulty."""

    levels = {
        "Easy": {
            "min": 0,
            "max": 50,
            "attempts": 10
        },

        "Medium": {
            "min": 0,
            "max": 500,
            "attempts": 7
        },

        "Hard": {
            "min": 0,
            "max": 5000,
            "attempts": 5
        },

        "Iran": {
            "min": -10000,
            "max": 10000,
            "attempts": 5
        }
    }

    if level not in levels:
        return None

    minimum = levels[level]["min"]
    maximum = levels[level]["max"]

    return random.randint(minimum, maximum)


def get_level():
    """Let the player choose difficulty."""

    while True:

        print("""
╔════════════════════════════╗
║       SELECT LEVEL         ║
╠════════════════════════════╣
║ 1. Easy                    ║
║ 2. Medium                  ║
║ 3. Hard                    ║
║ 4. Iran                    ║
║ 5. Random                  ║
║ q. Back                    ║
╚════════════════════════════╝
""")

        choice = input("Choose level: ").strip().lower()

        levels = {
            "1": "Easy",
            "2": "Medium",
            "3": "Hard",
            "4": "Iran"
        }

        if choice in levels:
            return levels[choice]

        if choice == "5":
            return random.choice(
                ["Easy", "Medium", "Hard", "Iran"]
            )

        if choice == "q":
            return None

        print("❌ Invalid choice.")


def get_level_info(level):
    """Return difficulty information."""

    data = {
        "Easy": (0, 50, 10),
        "Medium": (0, 500, 7),
        "Hard": (0, 5000, 5),
        "Iran": (-10000, 10000, 5)
    }

    return data[level]


def give_hint(number, guess):
    """Give a hint based on player's guess."""

    difference = abs(number - guess)

    if difference == 0:
        return "🎯 EXACT!"

    if difference <= 5:
        return "🔥 Extremely close!"

    if difference <= 20:
        return "🔥 Very close!"

    if difference <= 100:
        return "🙂 You're getting close."

    return "🥶 You're far away."


def calculate_score(level, attempts_left, hints_used, streak):
    """Calculate score."""

    base_scores = {
        "Easy": 100,
        "Medium": 250,
        "Hard": 500,
        "Iran": 1000
    }

    score = base_scores[level]

    score += attempts_left * 25

    score -= hints_used * 30

    score += streak * 50

    if score < 10:
        score = 10

    return score


def use_hint(number, minimum, maximum):
    """Give the player different types of hints."""

    print("""
╔════════════════════════════╗
║         💡 HINTS           ║
╠════════════════════════════╣
║ 1. Even / Odd              ║
║ 2. Number Range             ║
║ 3. Distance                 ║
║ 4. Cancel                   ║
╚════════════════════════════╝
""")

    choice = input("Choose hint: ").strip()

    if choice == "1":

        if number % 2 == 0:
            print("💡 The number is EVEN.")
        else:
            print("💡 The number is ODD.")

        return True

    elif choice == "2":

        middle = (minimum + maximum) // 2

        if number <= middle:
            print(
                f"💡 The number is between "
                f"{minimum} and {middle}."
            )
        else:
            print(
                f"💡 The number is between "
                f"{middle + 1} and {maximum}."
            )

        return True

    elif choice == "3":

        print(
            f"💡 The number is approximately "
            f"{abs(number)} units from zero."
        )

        return True

    elif choice == "4":
        return False

    else:
        print("❌ Invalid hint.")
        return False


def play_game(level, stats):
    """Run one complete game."""

    minimum, maximum, attempts = get_level_info(level)

    number = random.randint(minimum, maximum)

    hints_used = 0
    attempts_left = attempts

    print("\n" + "=" * 45)

    print(f"🎮 Level: {level}")
    print(f"🔢 Range: {minimum} → {maximum}")
    print(f"❤️ Attempts: {attempts}")
    print(f"🔥 Current streak: {stats['streak']}")

    print("=" * 45)

    while attempts_left > 0:

        print(
            f"\n❤️ Attempts left: {attempts_left}"
            f" | 🪙 Coins: {stats['coins']}"
            f" | 🏆 Score: {stats['score']}"
        )

        print(
            "\nEnter your guess "
            "(h = hint, q = quit): ",
            end=""
        )

        user_input = input().strip().lower()

        if user_input == "q":
            print("\n👋 Leaving game...")
            return False

        if user_input == "h":

            if stats["coins"] <= 0:
                print("❌ You don't have enough coins.")

            else:
                used = use_hint(
                    number,
                    minimum,
                    maximum
                )

                if used:
                    stats["coins"] -= 1
                    hints_used += 1

            continue

        try:
            guess = int(user_input)

        except ValueError:
            print("❌ Enter a valid number.")
            continue

        attempts_left -= 1

        if guess == number:

            points = calculate_score(
                level,
                attempts_left,
                hints_used,
                stats["streak"]
            )

            stats["score"] += points
            stats["streak"] += 1
            stats["wins"] += 1

            stats["coins"] += 2

            print("""
╔════════════════════════════════╗
║          🎉 YOU WIN!           ║
╚════════════════════════════════╝
""")

            print(f"🎯 Correct number: {number}")
            print(f"💰 Points earned: {points}")
            print(f"🏆 Total score: {stats['score']}")
            print(f"🔥 Streak: {stats['streak']}")
            print("🪙 +2 coins")

            return True

        hint_message = give_hint(number, guess)

        if guess < number:
            print("📈 Too LOW!")
        else:
            print("📉 Too HIGH!")

        print(hint_message)

    stats["losses"] += 1
    stats["streak"] = 0

    print("""
╔════════════════════════════════╗
║          💀 GAME OVER          ║
╚════════════════════════════════╝
""")

    print(f"😈 The correct number was: {number}")
    print("🔥 Your streak has been reset.")

    return True


def show_statistics(stats, high_score):
    """Show player statistics."""

    print("""
╔══════════════════════════════╗
║        📊 STATISTICS         ║
╠══════════════════════════════╣
""")

    print(f"🏆 Current Score : {stats['score']}")
    print(f"🥇 High Score    : {high_score}")
    print(f"🎯 Wins          : {stats['wins']}")
    print(f"💀 Losses        : {stats['losses']}")
    print(f"🔥 Current Streak: {stats['streak']}")
    print(f"🪙 Coins         : {stats['coins']}")

    total_games = stats["wins"] + stats["losses"]

    if total_games > 0:

        win_rate = (
            stats["wins"] / total_games
        ) * 100

        print(f"📈 Win Rate      : {win_rate:.1f}%")

    else:
        print("📈 Win Rate      : 0%")

    print("╚══════════════════════════════╝")


def main():
    """Main game loop."""

    high_score = load_high_score()

    stats = {
        "score": 0,
        "wins": 0,
        "losses": 0,
        "streak": 0,
        "coins": 3
    }

    while True:

        clear_screen()
        show_banner()

        print(f"🏆 High Score: {high_score}")

        print("""
╔══════════════════════════════╗
║          MAIN MENU           ║
╠══════════════════════════════╣
║ 1. 🎮 New Game               ║
║ 2. 📊 Statistics             ║
║ 3. 🏆 High Score             ║
║ 4. 🪙 Buy Coins              ║
║ 5. 🚪 Exit                   ║
╚══════════════════════════════╝
""")

        choice = input("Choose: ").strip().lower()

        if choice == "1":

            level = get_level()

            if level is None:
                continue

            result = play_game(level, stats)

            if stats["score"] > high_score:

                high_score = stats["score"]

                save_high_score(high_score)

                print("\n🏆 NEW HIGH SCORE!")

            if result:

                again = input(
                    "\nPlay again? (y/n): "
                ).strip().lower()

                if again != "y":
                    continue

        elif choice == "2":

            clear_screen()

            show_statistics(
                stats,
                high_score
            )

            input("\nPress Enter to continue...")

        elif choice == "3":

            clear_screen()

            print("""
╔══════════════════════════════╗
║          🏆 HIGH SCORE       ║
╠══════════════════════════════╣
""")

            print(f"       {high_score}")

            print("""
╚══════════════════════════════╝
""")

            input("Press Enter to continue...")

        elif choice == "4":

            print("""
╔══════════════════════════════╗
║          🪙 COIN SHOP        ║
╠══════════════════════════════╣
║ 1. Buy 5 coins → +5 coins    ║
║ 2. Buy 10 coins → +10 coins  ║
║ 3. Back                       ║
╚══════════════════════════════╝
""")

            shop_choice = input("Choose: ").strip()

            if shop_choice == "1":

                stats["coins"] += 5
                print("🪙 +5 coins!")

            elif shop_choice == "2":

                stats["coins"] += 10
                print("🪙 +10 coins!")

            elif shop_choice == "3":
                continue

            else:
                print("❌ Invalid choice.")

            input("\nPress Enter to continue...")

        elif choice == "5":

            print("\n👋 Thanks for playing!")
            print(f"🏆 Final Score: {stats['score']}")

            break

        else:
            print("❌ Invalid option.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")
