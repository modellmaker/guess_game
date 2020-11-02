import random
secret = 0
lives = 0
interval = 0
attempt = 1
max_attempt = []
high_score = []
attempt_index = []

name = input("Please add your name: ")
print("Welcome, " + name.title() + "!")  # Játékos nevének bekérése

level = input("Choose level (Easy, Medium, Hard): ")  # Nehézségi szint választása
level = level.lower()

if level == "easy":
    lives = 20
    interval = 5
    with open("high_score_easy.txt", "r", encoding="utf8") as hs_file:  # high score fájl megnyitása
        contents = hs_file.read().splitlines()
        # print(contents)
        for line in contents:
            contents = line.split(",")
            high_score.append(contents)
        # print(high_score)
        for score in range(0, len(high_score)):
            max_attempt.append(high_score[score][1])
        max_attempt = max(max_attempt)
        # print(max_attempt)
        print("\nBest players on Easy level:")
        for item in range(0, len(high_score)):
            print(high_score[item][0] + ": " + high_score[item][1])

elif level == "medium":
    lives = 10
    interval = 15
    contents = open("high_score_medium.txt", "r", encoding="utf8")  # high score fájl megnyitása
    for line in contents:
        contents = line.strip().split(",")
        high_score.append(contents)
    for i in range(0, len(high_score[1])):
        high_score[1][i] = int(high_score[1][i])

    print("\nLevel: Medium\n\nBest players:")
    for i in range(0, len(high_score[0])):
        print(high_score[0][i] + ": " + str(high_score[1][i]))

elif level == "hard":
    lives = 5
    interval = 30
    contents = open("high_score_hard.txt", "r", encoding="utf8")  # high score fájl megnyitása
    for line in contents:
        contents = line.strip().split(",")
        high_score.append(contents)
    for i in range(0, len(high_score[1])):
        high_score[1][i] = int(high_score[1][i])

    print("\nLevel: Hard\n\nBest players:")
    for i in range(0, len(high_score[0])):
        print(high_score[0][i] + ": " + str(high_score[1][i]))
else:
    print("You didn't provide a suitable level.")

secret = random.randint(1, interval)

for life in reversed(range(lives)):
    guess = int(input("\nYou have " + str(life+1) + " guesses. Guess The number: "))
    if guess != secret:
        print("Sorry, try again!")
        attempt += 1
    else:
        print("You've guessed it! The secret number was " + str(secret) + "!")
        print("Attempts needed: " + str(attempt))
        if level == "easy" and max_attempt > str(attempt):
            with open("high_score_easy.txt", "r+", encoding="utf8") as hs_file:
                # print(high_score)
                # print(max_attempt)
                for item in range(0, len(high_score)):
                    attempt_index.append(high_score[item][1])
                attempt_index = attempt_index.index(max(attempt_index))
                # print(attempt_index)
                high_score[attempt_index][0] = name
                high_score[attempt_index][1] = str(attempt)
                # print(high_score)
                for item in high_score:
                    hs_file.write("'{0}'".format(high_score[0]))
                # hs_file.write("\n")
                """for item in high_score[1]:
                    hs_file.write("%s" % item)"""
        break
