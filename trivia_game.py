import random
questions = {
    "What color is the sky on a clear day?": "blue",
    "How many legs does a spider have?": "8",
    "What do bees make?": "honey",
    "What planet do we live on?": "earth",
    "What do you call a baby cat?": "kitten",
    "How many days are there in a week?": "7",
    "What is the opposite of hot?": "cold",
    "What is 2 + 2?": "4",
    "What do you use to write on a blackboard?": "chalk",
    "How many wheels does a bicycle have?": "2",
    "Which animal barks?": "dog",
    "What is the first letter of the alphabet?": "a"
}


def trivia_game():
    # we use .keys fuction to take the info of the keys (answer) that we stored
    question_list = list(questions.keys())
    total_questions = 5
    count = 0

    selected_questions = random.sample(question_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input(f"Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct answer! \n")
            count += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}. \n")
    print(
        f"You have completed the game. Your socre is: {count}/{total_questions}")


def want_to_continue():
    continue_answer = input(
        "Do you want to continue playing this game (yes/no): ").lower()
    return continue_answer == "yes"


while True:
    trivia_game()
    if not want_to_continue():
        print("Thanks for playing this game.")
        break
