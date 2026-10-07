from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int = 0
    wins: int = 0
    losses: int = 0
    streak: int = 0
    best_streak: int = 0
    hints: int = 3

    @property
    def games_played(self) -> int:
        return self.wins + self.losses

    @property
    def win_rate(self) -> float:
        if not self.games_played:
            return 0.0

        return self.wins / self.games_played * 100