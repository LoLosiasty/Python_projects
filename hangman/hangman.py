import random


def password_randomizer():
    return random.choice(["python", "java", "swift", "javascript"])


def password_hiding(password_):
    hidden_password_ = list(password_)
    i = 0
    while i < len(password):
        hidden_password_[i] = "-"
        i += 1
    return hidden_password_


def input_checker(answer_):
    if len(answer_) != 1:
        print("Please, input a single letter.")
        return True
    if ("z" >= answer_ >= "a") is False:
        print("Please, enter a lowercase letter from the English alphabet.")
        return True
    return False


print("H A N G M A N  # 8 attempts")
won_games = 0
lost_games = 0
while True:
    print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
    option = input()
    if option == "play":
        attempts = 8
        used_chars = ""
        password = password_randomizer()
        hidden_password = password_hiding(password)
        while attempts > 0:
            if password == "".join(hidden_password):
                print(password, "\nYou guessed the word " + password + "!\nYou survived!")
                won_games += 1
                break
            print("\n" + "".join(hidden_password))
            answer = input("Input a letter:")
            if input_checker(answer):
                continue
            if answer in password and answer not in used_chars:
                for index, elem in enumerate(password):
                    if elem == answer:
                        hidden_password[index] = answer
                        used_chars += answer
            elif answer in used_chars:
                print("You've already guessed this letter.")
            else:
                used_chars += answer
                attempts -= 1
                print("That letter doesn't appear in the word. #", attempts, "attempts")
        else:
            lost_games += 1
            print("You lost!")
    elif option == "results":
        print("You won:", won_games, "times\nYou lost:", lost_games, "times")
    elif option == "exit":
        break
