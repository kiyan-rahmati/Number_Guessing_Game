def calculate_score(
    multiplier: float,
    attempts_left: int,
    hints_used: int,
    streak: int,
) -> int:
    score = 100 * multiplier
    score += attempts_left * 25 * multiplier
    score -= hints_used * 30
    score += streak * 50

    return max(10, int(score))