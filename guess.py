import random
secret = 0
lives = 0
interval = 0
attempts = 1

name = input("Please add your name: ")
print("Welcome, " + name.title() + "!")

level = input("Choose level (Easy, Medium, Hard): ")
level = level.lower()

if level == "easy":
    lives = 20
    interval = 5
elif level == "medium":
    lives = 10
    interval = 15
elif level == "hard":
    lives = 5
    interval = 30
else:
    print("You didn't provide a suitable level.")

with open("high_score.txt", "r", encoding="utf8") as hs_file:
    contents = hs_file.read().splitlines()
    print(contents)
    if level == "easy":
        print("\nLevel: " + contents[0] + "\nBest player: " + contents[1] + ", Attempts: " + contents[2])

secret = random.randint(1, interval)

for i in reversed(range(lives)):
    guess = int(input("You have " + str(i+1) + " guesses. Guess The number: "))
    if guess != secret:
        print("Sorry, try again!")
        attempts += 1
    else:
        print("You've guessed it! The secret number was " + str(secret) + "!")
        print("Attempts needed: " + str(attempts))
        with open("high_score.txt", "w", encoding="utf8") as hs_file:
            hs_file.write(level.title() + "\n" + name.title() + "\n" + str(attempts))
        break
