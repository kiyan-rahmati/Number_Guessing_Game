from app.game.scoring import calculate_score


def test_score_never_drops_below_minimum():
    assert calculate_score(
        1,
        0,
        99,
        0,
    ) == 10


def test_more_attempts_left_means_more_score():
    low = calculate_score(
        1,
        1,
        0,
        0,
    )

    high = calculate_score(
        1,
        5,
        0,
        0,
    )

    assert high > low