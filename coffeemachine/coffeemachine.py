water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups_needed = int(input("Write how many cups of coffee you will need:\n"))

# Считаем, на сколько чашек хватит каждого ингредиента по отдельности
possible_by_water = water // 200
possible_by_milk = milk // 50
possible_by_beans = beans // 15

# Максимальное число чашек ограничено самым дефицитным ингредиентом
max_cups = min(possible_by_water, possible_by_milk, possible_by_beans)

if max_cups == cups_needed:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups_needed:
    extra_cups = max_cups - cups_needed
    print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
else:
    print(f"No, I can make only {max_cups} cup(s) of coffee")
