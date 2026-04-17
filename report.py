def generate_report(user, ai_text, score, analytics):

    return f"""
🧑‍⚕️ AI Hair Specialist Report

👤 Patient Details:
Age: {user['age']}
Gender: {user['gender']}
Smoking: {user['smoking']}
Drinking: {user['drinking']}

📉 Hair Condition Score: {score}/100
⚠️ Risk Level: {analytics['risk']}
📊 Recovery Time: {analytics['recovery_time']}
🎯 Confidence: {analytics['confidence']}

🔍 Diagnosis:
{ai_text}

💊 Treatment Plan:
1. Improve protein & iron intake
2. Reduce stress
3. Use ketoconazole shampoo (if dandruff)
4. Oil massage twice a week

📌 Next Steps:
- Track hair weekly
- Maintain diet consistency
- Consult dermatologist if no improvement in 90 days

⚠️ Note:
This is AI-generated guidance, not a medical prescription.
"""