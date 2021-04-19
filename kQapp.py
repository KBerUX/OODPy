from kQuestions import questions


k_questions = [
    "What is my favorite color?\n(a) pink\n(b) red\n(c) grey\n(d) I don't have one :)\n\n",
    "Cats or Dogs?\n(a) both\n(b) ew, no!\n(c) Cats hands-down\n(d) dogs are man's best friend!\n\n",
    "How many pets do I have?\n(a) 2\n(b) 3\n(c) 5\n(d) 0\n(e) too many to count!\n\n",
    "Netlix or Hulu?\n(a) Hulu lol\n(b) Netflix is better D:\n\n",
    "Xbox, PS4, Or PC?\n(a) PC Master Race\n(b) nah, Xbox\n(c) Ps4 is just better!\n\n"
]

question_answer = [
    questions(k_questions[0], "a"),
    questions(k_questions[1], "c"),
    questions(k_questions[2], "e"),
    questions(k_questions[3], "a"),
    questions(k_questions[4], "c"),
]


def try_test(kQuestions):
    score = 0
    for questions in kQuestions:
        answer = input(questions.ask)
        if answer == questions.response:
            score += 1
    print("You got " + str(score) + "/" +
          str(len(k_questions)) + " correct.")


try_test(question_answer)
