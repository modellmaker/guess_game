import random
secret = 0
lives = 0
interval = 0
attempt = 1
max_attempt = 0
high_score = {}
attempt_index = []

player_name = input("Please add your name: ")
print("Welcome, " + player_name.title() + "!")  # Játékos nevének bekérése

level = input("Choose level (Easy, Medium, Hard): ")  # Nehézségi szint választása
level = level.lower()


def read_file():  # high_score fájl beolvasása
    with open("high_score.txt", encoding="utf8") as hs_file:
        for line in hs_file:
            name, score = line.split()
            high_score[name] = score
    return high_score


def level_easy():
    del high_score["Easy"]
    for name in list(high_score)[3:]:
        del high_score[name]
    print("\nBest players:")
    for name, score in high_score.items():
        print(name + ": " + score)


def level_medium():
    for name in list(high_score)[0:5]:
        del high_score[name]
        for name_ in list(high_score)[7:]:
            del high_score[name_]
    print("\nBest players:")
    for name, score in high_score.items():
        print(name + ": " + score)


def level_hard():
    for name in list(high_score)[0:9]:
        del high_score[name]
    print("\nBest players:")
    for name, score in high_score.items():
        print(name + ": " + score)


def main():
    print()


read_file()

if level == "easy":
    level_easy()
    lives = 20
    interval = 5

if level == "medium":
    level_medium()
    lives = 10
    interval = 15

if level == "hard":
    level_hard()
    lives = 5
    interval = 30

secret = random.randint(1, interval)

for life in reversed(range(lives)):
    guess = int(input("\nYou have " + str(life+1) + " guesses. Guess The number: "))
    if guess != secret:
        print("Sorry, try again!")
        attempt += 1
    else:
        print("You've guessed it! The secret number was " + str(secret) + "!")
        print("Attempts needed: " + str(attempt))
        if level == "easy" and max_attempt > attempt:
            with open("high_score.txt", "r+", encoding="utf8") as hs_file:
                for item in range(len(high_score)):
                    attempt_index.append(high_score[item][1])
                attempt_index = attempt_index.index(max(attempt_index))
                high_score[attempt_index][0] = player_name
                high_score[attempt_index][1] = str(attempt)
                for item in high_score:
                    hs_file.write(str(item[0]) + "," + str(item[1]) + "\n")
        break
