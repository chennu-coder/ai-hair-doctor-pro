def generate_analytics(score):
    if score > 80:
        risk = "Low"
    elif score > 50:
        risk = "Moderate"
    else:
        risk = "High"

    return {
        "risk": risk,
        "recovery_time": "3-6 months",
        "confidence": 0.85
    }