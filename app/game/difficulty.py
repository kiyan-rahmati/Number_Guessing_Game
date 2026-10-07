from dataclasses import dataclass
from enum import Enum


class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    EXTREME = "Extreme"
    LEGENDARY = "Legendary"


@dataclass(frozen=True)
class DifficultyConfig:
    minimum: int
    maximum: int
    attempts: int
    multiplier: float


CONFIGS = {
    Difficulty.EASY: DifficultyConfig(1, 10, 10, 1.0),
    Difficulty.MEDIUM: DifficultyConfig(1, 50, 8, 1.5),
    Difficulty.HARD: DifficultyConfig(1, 100, 7, 2.0),
    Difficulty.EXTREME: DifficultyConfig(1, 1000, 6, 4.0),
    Difficulty.LEGENDARY: DifficultyConfig(1, 10000, 5, 10.0),
}


def get_config(level: Difficulty | str) -> DifficultyConfig | None:
    if isinstance(level, str):
        try:
            level = Difficulty(level)
        except ValueError:
            return None

    return CONFIGS.get(level)