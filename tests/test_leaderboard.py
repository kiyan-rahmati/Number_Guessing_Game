from app.models.player import Player
from app.storage.leaderboard import Leaderboard


def test_leaderboard_saves_and_sorts(tmp_path):
    board = Leaderboard(
        tmp_path / "leaderboard.json"
    )

    board.save_score(
        Player("A", score=100)
    )

    board.save_score(
        Player("B", score=300)
    )

    entries = board.load()

    assert entries[0]["name"] == "B"
    assert entries[1]["name"] == "A"