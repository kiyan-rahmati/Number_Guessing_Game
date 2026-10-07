import random

from app.game.difficulty import Difficulty, DifficultyConfig, get_config
from app.game.hints import parity_hint, proximity_hint, range_hint
from app.game.scoring import calculate_score
from app.models.game_result import GameResult, GameStatus


class GameEngine:
    """Core game rules without terminal input/output."""

    def __init__(
        self,
        difficulty: Difficulty | str,
        streak: int = 0,
        rng: random.Random | None = None,
    ) -> None:
        config = get_config(difficulty)

        if config is None:
            raise ValueError("Invalid difficulty level.")

        self.difficulty = Difficulty(difficulty)
        self.config: DifficultyConfig = config

        self._rng = rng or random.Random()

        self.secret_number = self._rng.randint(
            config.minimum,
            config.maximum,
        )

        self.attempts_left = config.attempts
        self.guesses = 0
        self.hints_used = 0
        self.streak = streak
        self.finished = False

    def guess(self, value: int) -> GameResult | str:
        if self.finished:
            raise RuntimeError("This game has already finished.")

        if not self.config.minimum <= value <= self.config.maximum:
            return (
                f"Enter a number between "
                f"{self.config.minimum} and "
                f"{self.config.maximum}."
            )

        self.guesses += 1
        self.attempts_left -= 1

        if value == self.secret_number:
            self.finished = True

            score = calculate_score(
                self.config.multiplier,
                self.attempts_left,
                self.hints_used,
                self.streak,
            )

            return GameResult(
                status=GameStatus.WON,
                secret_number=self.secret_number,
                guesses=self.guesses,
                score=score,
                hints_used=self.hints_used,
            )

        if self.attempts_left == 0:
            self.finished = True

            return GameResult(
                status=GameStatus.LOST,
                secret_number=self.secret_number,
                guesses=self.guesses,
                hints_used=self.hints_used,
            )

        direction = "low" if value < self.secret_number else "high"

        return (
            f"📈 Too {direction}! "
            f"{proximity_hint(self.secret_number, value)}"
        )

    def hint(self, kind: str) -> str:
        if self.finished:
            return "The game is already finished."

        kind = kind.lower()

        if kind == "parity":
            message = parity_hint(self.secret_number)

        elif kind == "range":
            message = range_hint(
                self.secret_number,
                self.config.minimum,
                self.config.maximum,
            )

        elif kind == "distance":
            message = (
                f"💡 Distance from zero: "
                f"{abs(self.secret_number)}"
            )

        else:
            return (
                "Unknown hint. "
                "Use: parity, range, or distance."
            )

        self.hints_used += 1

        return message