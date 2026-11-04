# Начальные ресурсы кофемашины
water = 400
milk = 540
beans = 120
cups = 9
money = 550

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "exit":
        break

    elif action == "remaining":
        print("\nThe coffee machine has:")
        print(f"{water} ml of water")
        print(f"{milk} ml of milk")
        print(f"{beans} g of coffee beans")
        print(f"{cups} disposable cups")
        print(f"${money} of money\n")

    elif action == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if coffee_type == "back":
            continue

        coffee_type = int(coffee_type)

        # Рецепты напитков: [вода, молоко, зрна, стоимость]
        recipes = {
            1: [250, 0, 16, 4],  # Espresso
            2: [350, 75, 20, 7],  # Latte
            3: [200, 100, 12, 6]  # Cappuccino
        }

        if coffee_type in recipes:
            req_water, req_milk, req_beans, cost = recipes[coffee_type]

            # Проверка ресурсов
            if water < req_water:
                print("Sorry, not enough water!")
            elif milk < req_milk:
                print("Sorry, not enough milk!")
            elif beans < req_beans:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= req_water
                milk -= req_milk
                beans -= req_beans
                cups -= 1
                money += cost

    elif action == "fill":
        water += int(input("Write how many ml of water you want to add:\n"))
        milk += int(input("Write how many ml of milk you want to add:\n"))
        beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        cups += int(input("Write how many disposable cups you want to add:\n"))

    elif action == "take":
        print(f"I gave you ${money}")
        money = 0
