class Drink:
    def __init__(self, name = '', price = 0.0, contents = []):
        self.name = name
        self.price = price
        self.contents = contents

    def __str__(self):
        return f"name = {self.name}, price = {self.price}, contents = {self.contents}"

espresso = Drink('espresso',2,['milk', 'sugar', 'water', 'coffee_beans'])

print(espresso)

def Prompt():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "espresso":
        pass
