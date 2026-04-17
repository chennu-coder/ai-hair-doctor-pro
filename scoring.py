def calculate_score(data):
    score = 100

    if data["years"] > 5:
        score -= 25
    if data["smoking"] == "Yes":
        score -= 15
    if data["drinking"] == "Yes":
        score -= 10
    if "dandruff" in data["problem"].lower():
        score -= 10

    return max(score, 10)