from app.game.difficulty import CONFIGS, Difficulty
from app.game.engine import GameEngine
from app.models.game_result import GameStatus
from app.models.player import Player
from app.storage.leaderboard import Leaderboard


def print_banner() -> None:
    print("\n" + "=" * 52)
    print("🎯 NUMBER GUESSING GAME")
    print("   Python • Modular Architecture • CLI")
    print("=" * 52)


def choose_difficulty() -> Difficulty | None:
    levels = list(Difficulty)

    print("\nSelect difficulty:")

    for index, level in enumerate(levels, 1):
        config = CONFIGS[level]

        print(
            f"{index}. {level.value:<10} "
            f"{config.minimum}-{config.maximum} | "
            f"{config.attempts} attempts"
        )

    print("q. Back")

    choice = input("Choose: ").strip().lower()

    if choice == "q":
        return None

    try:
        return levels[int(choice) - 1]

    except (ValueError, IndexError):
        print("❌ Invalid choice.")
        return None


def play_round(player: Player) -> bool:
    difficulty = choose_difficulty()

    if difficulty is None:
        return False

    engine = GameEngine(
        difficulty,
        streak=player.streak,
    )

    print(
        f"\n🎮 {difficulty.value}: "
        f"{engine.config.minimum}–"
        f"{engine.config.maximum}"
    )

    while not engine.finished:

        raw = input(
            f"\n❤️ Attempts left: "
            f"{engine.attempts_left} | "
            f"🏆 Score: {player.score}\n"
            "Guess (h = hint, q = quit): "
        ).strip().lower()

        if raw == "q":
            print("👋 Round cancelled.")
            return False

        if raw == "h":

            if player.hints <= 0:
                print("❌ No hints left.")
                continue

            print(engine.hint("parity"))
            player.hints -= 1
            continue

        try:
            value = int(raw)

        except ValueError:
            print("❌ Enter a valid integer.")
            continue

        result = engine.guess(value)

        if isinstance(result, str):
            print(result)
            continue

        if result.status == GameStatus.WON:

            player.score += result.score
            player.wins += 1
            player.streak += 1

            player.best_streak = max(
                player.best_streak,
                player.streak,
            )

            player.hints += 1

            print(
                f"\n🎉 YOU WIN! "
                f"Number: {result.secret_number}\n"
                f"💰 +{result.score} points | "
                f"🔥 Streak: {player.streak}"
            )

        else:

            player.losses += 1
            player.streak = 0

            print(
                f"\n💀 GAME OVER! "
                f"Number: {result.secret_number}"
            )

    return True


def show_stats(player: Player) -> None:
    print("\n📊 STATISTICS")
    print("-" * 30)

    print(f"Player       : {player.name}")
    print(f"Games        : {player.games_played}")
    print(f"Wins         : {player.wins}")
    print(f"Losses       : {player.losses}")
    print(f"Win rate     : {player.win_rate:.1f}%")
    print(f"Score        : {player.score}")
    print(f"Best streak  : {player.best_streak}")
    print(f"Hints        : {player.hints}")


def show_leaderboard(board: Leaderboard) -> None:
    print("\n🏆 LEADERBOARD")

    entries = board.load()

    if not entries:
        print("No scores yet.")
        return

    for index, entry in enumerate(entries, 1):
        print(
            f"{index:>2}. "
            f"{entry['name']:<16} "
            f"{entry['score']:>6} pts"
        )


def run() -> None:
    print_banner()

    name = input(
        "Player name: "
    ).strip() or "Player"

    player = Player(name)
    board = Leaderboard()

    while True:

        print(
            "\n1. 🎮 New game"
            "\n2. 📊 Statistics"
            "\n3. 🏆 Leaderboard"
            "\n4. 🚪 Exit"
        )

        choice = input("Choose: ").strip()

        if choice == "1":

            if play_round(player):
                board.save_score(player)

        elif choice == "2":
            show_stats(player)

        elif choice == "3":
            show_leaderboard(board)

        elif choice == "4":
            print(
                f"\n👋 Thanks for playing, "
                f"{player.name}!"
            )
            break

        else:
            print("❌ Invalid option.")