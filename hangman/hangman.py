
import random

words = ["python", "java", "javascript", "php"]
score = 0

while True:
    print("\nHANGMAN")
    print("1. Play")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "2":
        print("Thanks for playing!")
        print(f"Your score: {score}")
        break

    elif choice == "1":
        word = random.choice(words)
        guessed = ["-"] * len(word)
        used_letters = []
        attempts = 8

        while attempts > 0:
            print("\n" + "".join(guessed))
            letter = input("Input a letter: ")

            if len(letter) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a single lowercase letter")
                continue

            if letter in used_letters:
                print("No improvements")
                attempts -= 1
            else:
                used_letters.append(letter)

                if letter in word:
                    for i in range(len(word)):
                        if word[i] == letter:
                            guessed[i] = letter
                else:
                    print("That letter doesn't appear in the word")
                    attempts -= 1

            if "-" not in guessed:
                print("You guessed the word!")
                print("You survived!")
                score += 1
                break

        if attempts == 0 and "-" in guessed:
            print("You lost!")
            print(f"The word was: {word}")

    else:
        print("Invalid option. Choose 1 or 2.")
