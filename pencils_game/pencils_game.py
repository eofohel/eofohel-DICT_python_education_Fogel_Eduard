import random

# 1. Проверка ввода количества олівців
num_pencils_str = input("How many pencils would you like to use:\n")

while True:
    if not num_pencils_str.isdigit():
        print("The number of pencils should be numeric")
        num_pencils_str = input()
        continue

    num_pencils = int(num_pencils_str)

    if num_pencils <= 0:
        print("The number of pencils should be positive")
        num_pencils_str = input()
        continue

    break

# 2. Выбор первого игрока (John — человек, Jack — бот)
players = ["John", "Jack"]
first_player = input(f"Who will be the first ({players[0]}, {players[1]}):\n")

while first_player not in players:
    print(f"Choose between '{players[0]}' and '{players[1]}'")
    first_player = input()

current_player_index = 0 if first_player == players[0] else 1

# 3. Игровой цикл с ботом
while num_pencils > 0:
    print("|" * num_pencils)
    current_player = players[current_player_index]

    if current_player == "John":
        # Ход человека
        taken_str = input(f"{current_player}'s turn:\n")

        if taken_str not in ["1", "2", "3"]:
            print("Possible values: '1', '2' or '3'")
            continue

        taken = int(taken_str)

        if taken > num_pencils:
            print("Too many pencils were taken")
            continue
    else:
        # Ход бота (Jack)
        print(f"{current_player}'s turn:")

        if num_pencils == 1:
            taken = 1
        elif num_pencils % 4 == 1:
            # Проигрышная позиция для бота — берет случайное число от 1 до 3
            taken = random.randint(1, min(3, num_pencils))
        else:
            # Выигрышная позиция — берем так, чтобы оставить сопернику остаток 1
            taken = (num_pencils - 1) % 4
            if taken == 0:
                taken = 1

        print(taken)

    # Уменьшаем количество олівців
    num_pencils -= taken

    # Проверка на конец игры (кто взял последний — проиграл)
    if num_pencils == 0:
        winner = players[1 - current_player_index]
        print(f"{winner} won!")
        break

    # Смена хода
    current_player_index = 1 - current_player_index
