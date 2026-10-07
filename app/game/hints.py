def proximity_hint(secret: int, guess: int) -> str:
    distance = abs(secret - guess)

    if distance == 0:
        return "🎯 Exact!"

    if distance <= 5:
        return "🔥 Extremely close!"

    if distance <= 20:
        return "🔥 Very close!"

    if distance <= 100:
        return "🙂 Getting closer."

    return "🥶 Far away."


def parity_hint(secret: int) -> str:
    if secret % 2 == 0:
        return "💡 The number is even."

    return "💡 The number is odd."


def range_hint(secret: int, minimum: int, maximum: int) -> str:
    middle = (minimum + maximum) // 2

    if secret <= middle:
        return f"💡 The number is between {minimum} and {middle}."

    return f"💡 The number is between {middle + 1} and {maximum}."