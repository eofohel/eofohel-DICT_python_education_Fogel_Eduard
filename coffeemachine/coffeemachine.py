# Начальные ресурсы кофемашины
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def print_state():
    print("\nThe coffee machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{beans} g of coffee beans")
    print(f"{cups} disposable cups")
    print(f"${money} of money\n")


# Показываем состояние в начале
print_state()

action = input("Write action (buy, fill, take):\n")

if action == "buy":
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    if coffee_type == "1":  # Espresso
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    elif coffee_type == "2":  # Latte
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    elif coffee_type == "3":  # Cappuccino
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6

elif action == "fill":
    add_water = int(input("Write how many ml of water you want to add:\n"))
    add_milk = int(input("Write how many ml of milk you want to add:\n"))
    add_beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    add_cups = int(input("Write how many disposable cups you want to add:\n"))

    water += add_water
    milk += add_milk
    beans += add_beans
    cups += add_cups

elif action == "take":
    print(f"I gave you ${money}")
    money = 0

# Показываем состояние после выполненного действия
print_state()
