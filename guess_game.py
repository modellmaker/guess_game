import random

lives = 0
interval = 0
high_score = {}


def read_file():  # high_score fájl beolvasása
    with open("high_score.txt", encoding="utf8") as hs_file:
        for line in hs_file:
            name, score = line.split()
            high_score[name] = score
    return high_score


def print_easy_score():
    del high_score["Easy"]
    for name in list(high_score)[3:]:
        del high_score[name]
    print("\nBest players:")
    for name, score in high_score.items():
        print(name + ": " + score)


def print_medium_score():
    for name in list(high_score)[0:5]:
        del high_score[name]
        for name_ in list(high_score)[7:]:
            del high_score[name_]
    print("\nBest players:")
    for name, score in high_score.items():
        print(name + ": " + score)


def print_hard_score():
    for name in list(high_score)[0:9]:
        del high_score[name]
    print("\nBest players:")
    for name, score in high_score.items():
        print(name + ": " + score)


def max_attempt():
    max_score = max(high_score.values())
    high_score.clear()
    return max_score


def write_file_easy():
    with open("high_score.txt", "r+", encoding="utf8") as hs_file:
        for line in hs_file:
            name, score = line.split()
            high_score[name] = score
        print(high_score)
        temp_score = high_score
        del temp_score["Easy"]
        for name in list(temp_score)[3:]:
            del temp_score[name]
        print(temp_score)
        print(max(temp_score.values()))
        temp_score.update(name)
        """for name, score in high_score.items():
            hs_file.write(str(name) + " " + str(score) + "\n")"""


def main():
    secret = random.randint(1, interval)
    attempt = 1

    for life in reversed(range(lives)):
        guess = int(input("\nYou have " + str(life + 1) + " guesses. Guess The number: "))
        if guess != secret:
            print("Sorry, try again!")
            attempt += 1
        else:
            print("You've guessed it! The secret number was " + str(secret) + "!")
            print("Attempts needed: " + str(attempt))
            if level == "easy" and int(max_attempt()) > attempt:
                write_file_easy()
            elif level == "medium" and int(max_attempt()) > attempt:
                print("medium write")
            elif level == "hard" and int(max_attempt()) > attempt:
                print("hard write")
            break


player_name = input("Please add your name: ")
print("Welcome, " + player_name.title() + "!")  # Játékos nevének bekérése

level = input("Choose level (Easy, Medium, Hard): ")  # Nehézségi szint választása
level = level.lower()

read_file()

if level == "easy":
    print_easy_score()
    lives = 20
    interval = 5

if level == "medium":
    print_medium_score()
    lives = 10
    interval = 15

if level == "hard":
    print_hard_score()
    lives = 5
    interval = 30

main()
