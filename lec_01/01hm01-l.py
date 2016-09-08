import sys

__author__ = 'pavbelousov'

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

questions = ['What is a major version of Python you should choose?',
             'How to output to console your program?',
             'Who is the author of the Python programming language?',
             'What is a function to convert a integer to string?',
             'How to call a Zen of Python?'
             ]

answer = {0: ["3", "3.0", "3.5"],
          1: ["print", "print()"],
          2: ["guido van rossum", "guido", "rossum"],
          3: ["str", "str()"],
          4: "import this"
          }

passed_test = 0
for i in range(len(questions)):
    asked_user = input_function("{} - ".format(questions[i]))
    if asked_user.lower() in answer[i]:
        print("Correct! ({0} of {1})".format(i+1, len(questions)))
        passed_test += 1
    else:
        print("Wrong! ({0} of {1})".format(i+1, len(questions)))

print("\nFinish! Your answers is correct: -= {0} =- ".format(passed_test))
