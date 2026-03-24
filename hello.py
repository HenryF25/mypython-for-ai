import random

print("Maths Quiz")
score = 0
total_question = 5

for i in range(total_question):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    elif operator == "*":
        answer = a * b
    else:
        answer = a / b

    print(f"question {i + 1}: What is {a} {operator} {b}? ")

    try:
        user_input = float(input("Enter Answer: "))
        if user_input == answer:
            print("you are correct!")
            score += 1
        else:
            print(f"You are wrong! The correct answer is {answer}")
    except ValueError:
        print(f"Invalid Input! correct answer is {answer}")

print(f"Game Over! Total score is {score}/{total_question}")
