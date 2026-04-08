def grade(task, action):
    """
    Grades the agent's action based on the task requirements.
    Returns a score between 0.0 and 1.0
    """

    score = 0.0
    expected = task.get("expected", {})

    # ✅ 1. Bug Detection (0.4)
    if "bug" in expected:
        if action.bug_detected == expected["bug"]:
            score += 0.4
        else:
            score -= 0.2  # penalty for wrong detection

    # ✅ 2. Suggestion Quality (0.3)
    if "suggestion" in expected:
        expected_suggestion = expected["suggestion"].lower()
        user_suggestion = action.suggestion.lower()

        if expected_suggestion in user_suggestion:
            score += 0.3
        elif len(user_suggestion) > 5:
            score += 0.1  # partial credit

    # ✅ 3. Review Comment Quality (0.3)
    if action.review_comment:
        length = len(action.review_comment.strip())

        if length > 20:
            score += 0.3
        elif length > 10:
            score += 0.2
        elif length > 5:
            score += 0.1

    # ✅ Clamp score between 0 and 1
    score = max(0.0, min(score, 1.0))

    return score