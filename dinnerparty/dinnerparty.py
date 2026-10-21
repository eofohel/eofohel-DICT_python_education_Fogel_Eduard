
import random

number = int(input("Enter the number of friends joining (including you):\n"))

if number <= 0:
    print("No one is joining for the party")
else:
    friends = {}

    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(number):
        name = input()
        friends[name] = 0

    print(friends)

    print("Enter the total amount:")
    total = float(input())

    share = round(total / number, 2)

    for name in friends:
        friends[name] = share

    print(friends)

    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if answer == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")

        if number > 1:
            share = round(total / (number - 1), 2)
            for name in friends:
                friends[name] = 0 if name == lucky else share

        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)
