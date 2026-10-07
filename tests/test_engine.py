import random

from app.game.difficulty import Difficulty
from app.game.engine import GameEngine
from app.models.game_result import GameStatus


def test_engine_generates_number_in_range():
    engine = GameEngine(
        Difficulty.EASY,
        rng=random.Random(1),
    )

    assert 1 <= engine.secret_number <= 10


def test_correct_guess_wins():
    engine = GameEngine(
        Difficulty.EASY,
        rng=random.Random(1),
    )

    result = engine.guess(
        engine.secret_number
    )

    assert result.status == GameStatus.WON
    assert result.score > 0


def test_wrong_guesses_can_end_game():
    engine = GameEngine(
        Difficulty.EASY,
        rng=random.Random(1),
    )

    for _ in range(engine.config.attempts):
        result = engine.guess(
            engine.config.minimum
        )

    assert result.status in {
        GameStatus.WON,
        GameStatus.LOST,
    }


def test_out_of_range_does_not_use_attempt():
    engine = GameEngine(Difficulty.EASY)

    before = engine.attempts_left

    message = engine.guess(999)

    assert "between" in message
    assert engine.attempts_left == before