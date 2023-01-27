#! python3
# multiplicationQuiz.py - A Multiplication Quiz

import random

# TODO Ask user 10 mutiplication problems.
numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    print('#%s: %s x %s = ' %(questionNumber+1, num1, num2))
    response = int(input())
    if response == num1*num2:
        print ('True!')
        continue
    else:
        print("wrong answer!")
        break
input()

# Check the response if it is valid or not

