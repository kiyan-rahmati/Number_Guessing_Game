from app.game.difficulty import Difficulty, get_config


def test_all_difficulties_have_config():
    for level in Difficulty:
        assert get_config(level) is not None


def test_invalid_difficulty_returns_none():
    assert get_config("Unknown") is None


def test_legendary_is_harder():
    config = get_config(Difficulty.LEGENDARY)

    assert config.maximum == 10000
    assert config.attempts == 5