#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random

# The quiz data. Keys are states and values are their capitals.
    # TODO: Take quiz data from text file.
capitals = eval(open('data/capitals.txt').read())
countries = list(capitals.keys())
random.shuffle(countries)
countriesAsked = countries[0:50]

# Generate 35 quiz files.
for quizNum in range (35):
    # TODO: Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    # TODO: Shuffle the order of the states.
    random.shuffle(countriesAsked)

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[countriesAsked[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
    # TODO: Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {countriesAsked[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. { answerOptions[i]}\n")
            quizFile.write('\n')
            answerKeyFile.write(f"{questionNum + 1}.  {'ABCD'[answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKeyFile.close()
    # TODO: Write the answer key to a file.