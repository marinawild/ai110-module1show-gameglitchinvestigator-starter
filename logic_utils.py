def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "" or raw == " ":
        return False, None, "Enter a guess."

    if(raw < low):
        return False, None, "Below Guessing Range."
    if(raw > high):
        return False, None, "Above Guessing Range."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

def check_guess(guess, secret):
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"



def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
