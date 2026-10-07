import json
from dataclasses import asdict
from pathlib import Path

from app.models.player import Player


class Leaderboard:
    """JSON-backed leaderboard."""

    def __init__(
        self,
        path: str | Path = "data/leaderboard.json",
    ) -> None:
        self.path = Path(path)

    def load(self) -> list[dict]:
        if not self.path.exists():
            return []

        try:
            data = json.loads(
                self.path.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, OSError):
            return []

        return data if isinstance(data, list) else []

    def save_score(
        self,
        player: Player,
        limit: int = 10,
    ) -> list[dict]:

        entries = self.load()

        entries.append(asdict(player))

        entries.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        entries = entries[:limit]

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.path.write_text(
            json.dumps(
                entries,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        return entries