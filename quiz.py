questions = [
    {
        "question": "What is the capital of India?",
        "options": ["a) Delhi", "b) Mumbai", "c) Chennai", "d) Kolkata"],
        "answer": "a"
    },
    {
        "question": "Which language is used for Data Engineering?",
        "options": ["a) HTML", "b) Python", "c) CSS", "d) Photoshop"],
        "answer": "b"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    }
]

score = 0

print("\n--- Quiz App ---")

for i, q in enumerate(questions, start=1):
    print(f"\nQ{i}: {q['question']}")
    
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    if user_answer == q["answer"]:
        print("Correct ✅")
        score += 1
    else:
        print(f"Wrong ❌ (Correct: {q['answer']})")

print("\n--- Result ---")
print(f"Your Score: {score}/{len(questions)}")
