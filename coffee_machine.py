class CoffeeMachine:
    water_needed, milk_needed, beans_needed, cost = 0, 0, 0, 0

    def __init__(self, water, milk, coffeebeans, disposablecups, money):
        self.water = water
        self.milk = milk
        self.coffeebeans = coffeebeans
        self.disposablecups = disposablecups
        self.money = money
        self.active = True

    def espresso(self):
        self.water_needed = 250
        self.beans_needed = 16
        self.cost = 4

    def latte(self):
        self.water_needed = 350
        self.milk_needed = 75
        self.beans_needed = 20
        self.cost = 7

    def cappuccino(self):
        self.water_needed = 200
        self.milk_needed = 100
        self.beans_needed = 12
        self.cost = 6

    def machine_state(self):
        print("the coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.coffeebeans, " of coffee beans")
        print(self.disposablecups, " of disposable cups")
        print(self.money, " of money")

    def update(self):
        self.water -= self.water_needed
        self.milk -= self.milk_needed
        self.coffeebeans -= self.beans_needed
        self.money += self.cost
        self.disposablecups -= 1

    def update_state(self, a, b, c, d):
        self.water += a
        self.coffeebeans += c
        self.milk += b
        self.disposablecups += d

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def check_resources(self):
        if self.water < 200 and self.milk < 75 and self.coffeebeans < 12:
            print("Sorry, not enough water, milk and coffee beans")
            return False
        elif self.water < 200:
            print("Sorry, not enough water!")
            return False
        elif self.milk < 75:
            print("Sorry, not enough milk!")
            return False
        elif self.coffeebeans < 12:
            print("Sorry, not enough coffee beans!")
            return False
        else:
            return True

    def buy_coffee(self):
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,  4 - back: ")
        if self.check_resources():
            if user_input == "1":
                self.espresso()
                print('I have enough resources, making you a coffee!')
                self.update()
            elif user_input == "2":
                self.latte()
                print('I have enough resources, making you a coffee!')
                self.update()
            elif user_input == "3":
                self.cappuccino()
                print('I have enough resources, making you a coffee!')
                self.update()
            elif user_input == "4":
                self.choosing_action()

    def choosing_action(self):
        while self.active:
            user_input = input("Write action(buy, fill, take, remaining, exit): ")
            if user_input == "buy":
                self.buy_coffee()
            elif user_input == "fill":
                a = int(input("Write how many ml of water do you want to add: "))
                b = int(input("Write how many ml of milk do you want to add: "))
                c = int(input("Write how many grams of coffee beans do you want to add: "))
                d = int(input("Write how many disposable cups of coffee do you want to add: "))
                machine.update_state(a, b, c, d)
            elif user_input == "take":
                machine.take()
            elif user_input == "remaining":
                machine.machine_state()
            elif user_input == "exit":
                self.active = False


# Code
machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.choosing_action()
