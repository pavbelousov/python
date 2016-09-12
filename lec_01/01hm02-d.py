import json
from datetime import datetime


def check_user(login):
    """Проверяет пользователя на уникальность.
    Если пользователь существует, возвращает 1, иначе 0"""
    with open("users.txt", "r") as f:
        f = f.readlines()
        for line in f:
            line = line.split(":")
            if login == line[0]:
                return 1
        return 0


def main():
    while True:
        username = input("Please, write your username or type exit for exit -  ")
        if check_user(username) == 1:
            print("This username already exists in a users.txt file. Please, try again.")
            continue
        elif username.lower() == "exit":
            break
        else:
            with open("ques_ans.json") as str_data:
                str_data = str_data.read()
                jsdata = json.loads(str_data)
                passed_test = 0
                print("Let's start testing...")
                for i in jsdata["questions"]:
                    asked_user = input("{} - ".format(i["question"]))
                    if asked_user.lower() in i["answers"] and len(asked_user) != 0:
                        print("Correct!")
                        passed_test += 1
                    else:
                        print("Wrong!")

            print("Your result: {0} of {1} done".format(passed_test, len(jsdata["questions"])))

            with open("users.txt", "a") as opened_file:
                opened_file.write("{login}:{date}:{correct}\n".format(login=username,
                                    date=datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S"), correct=passed_test))
            break

if __name__ == '__main__':
    main()
