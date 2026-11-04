class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def process_input(self, user_input):
        if user_input == "buy":
            self.buy_coffee()
        elif user_input == "fill":
            self.fill_machine()
        elif user_input == "take":
            self.take_money()
        elif user_input == "remaining":
            self.print_state()

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} g of coffee beans")
        print(f"{self.cups} disposable cups")
        print(f"${self.money} of money\n")

    def buy_coffee(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "back":
            return

        choice = int(choice)
        recipes = {
            1: [250, 0, 16, 4],  # Espresso
            2: [350, 75, 20, 7],  # Latte
            3: [200, 100, 12, 6]  # Cappuccino
        }

        if choice in recipes:
            req_water, req_milk, req_beans, cost = recipes[choice]

            if self.water < req_water:
                print("Sorry, not enough water!")
            elif self.milk < req_milk:
                print("Sorry, not enough milk!")
            elif self.beans < req_beans:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= req_water
                self.milk -= req_milk
                self.beans -= req_beans
                self.cups -= 1
                self.money += cost

    def fill_machine(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.cups += int(input("Write how many disposable cups you want to add:\n"))

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0


# Запуск программы
machine = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "exit":
        break
    machine.process_input(action)
