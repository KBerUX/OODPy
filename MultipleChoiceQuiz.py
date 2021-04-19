from Questions import question

question_prompts = [
    "How many pets does Kist have?\n(a) 2\n(b) 3\n(c) 5\n(d) 0\n(e) too many to count!\n\n",
    "What month was Kist born?\n(a) Dec\n(b) Nov\n(c) Feb\n(d)Don't know don't care :)\n(e) April\n\n",
    "What's kist's favorite color?\n(a) Purble\n(b) Green\n(c) None :)\n(d) Yellow\n(e) Pink\n\n"
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "b"),
    question(question_prompts[2], "e"),
]


# function to run test - inside is a list of questions
def run_test(Questions):
    score = 0
    for question in Questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
