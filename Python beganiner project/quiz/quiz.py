import requests
import random
from pathlib import Path

# High Score File
score_file = Path("scores.txt")
if not score_file.exists() or score_file.read_text().strip() == "":
    score_file.write_text("0")

# Fetch Questions
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=multiple")
data = response.json()
questions = data["results"]

# Quiz Logic
score = 0
for item in questions:
    question = item["question"]
    correct_answer = item["correct_answer"]
    options = item["incorrect_answers"] + [correct_answer]
    random.shuffle(options)

    print(f"\n❓ Question: {question}")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    user_input = input("Your choice (1-4 or 's' to skip): ").strip().lower()

    if user_input == 's':
        print("⏭️ Skipped.\n")
        continue

    try:
        selected_index = int(user_input) - 1
        selected_option = options[selected_index]
    except (ValueError, IndexError):
        print("⚠️ Invalid input. Skipping question.")
        continue

    if selected_option == correct_answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. The correct answer is {correct_answer}.\n")

# High Score Check
high_score = int(score_file.read_text())
print(f"🏅 Previous High Score: {high_score}")
print(f"🎯 Final Score: {score} / {len(questions)}")

if score > high_score:
    print("🎉 Congratulations! New High Score!")
    score_file.write_text(str(score))
