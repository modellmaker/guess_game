import random
secret = 0
lives = 0
interval = 0
attempt = 1
max_attempt = 0

name = input("Please add your name: ")
print("Welcome, " + name.title() + "!")  # Játékos nevének bekérése

level = input("Choose level (Easy, Medium, Hard): ")  # Nehézségi szint választása
level = level.lower()

if level == "easy":
    lives = 20
    interval = 5
    with open("high_score_easy.txt", "r", encoding="utf8") as hs_file:  # high score fájl megnyitása
        high_score = []
        contents = hs_file
        for line in contents:
            contents = line.strip().split(",")[:-1]
            high_score.append(contents)
        for i in range(0, len(high_score[1])):
            high_score[1][i] = int(high_score[1][i])
        max_attempt = max(high_score[1])
        print("\nLevel: Easy\n\nBest players:")
        for i in range(0, len(high_score[0])):
            print(high_score[0][i] + ": " + str(high_score[1][i]))

elif level == "medium":
    lives = 10
    interval = 15
    contents = open("high_score_medium.txt", "r", encoding="utf8")  # high score fájl megnyitása
    high_score = []
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
    high_score = []
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

for i in reversed(range(lives)):
    guess = int(input("\nYou have " + str(i+1) + " guesses. Guess The number: "))
    if guess != secret:
        print("Sorry, try again!")
        attempt += 1
    else:
        print("You've guessed it! The secret number was " + str(secret) + "!")
        print("Attempts needed: " + str(attempt))
        if level == "easy" and max_attempt >= attempt:
            with open("high_score_easy.txt", "r+", encoding="utf8") as hs_file:
                high_score = []
                contents = hs_file
                for line in contents:
                    contents = line.strip().split(",")[:-1]
                    high_score.append(contents)
                attempt_index = high_score[1].index(str(max_attempt))
                high_score[0][attempt_index] = name
                high_score[1][attempt_index] = attempt
                hs_file.seek(0)
                hs_file.truncate()
                for item in high_score[0]:
                    hs_file.write("%s," % item)
                hs_file.write("\n")
                for item in high_score[1]:
                    hs_file.write("%s," % item)
                hs_file.close()
        break
