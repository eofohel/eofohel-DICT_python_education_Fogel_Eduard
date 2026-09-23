print("Hello! My name is DICT_Bot.")
print("I was created in 2026.")
print("Please, remind me your name.")
your_name = input("> ")
print(f"What a great name you have, {your_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

rem3 = int(input("> "))
rem5 = int(input("> "))
rem7 = int(input("> "))

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print(f"Your age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
num = int(input("> "))

for i in range(num + 1):
    print(f"{i} !")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat something many times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

while True:
    answer = int(input("> "))
    if answer == 2:
        break
    print("Please, try again.")

print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
