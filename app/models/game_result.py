from dataclasses import dataclass
from enum import Enum


class GameStatus(str, Enum):
    WON = "won"
    LOST = "lost"
    QUIT = "quit"


@dataclass(frozen=True)
class GameResult:
    status: GameStatus
    secret_number: int
    guesses: int
    score: int = 0
    hints_used: int = 0