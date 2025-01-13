import sys

#prompt user
user_choice = input("What would you like? \nespresso\nlatte\ncappuccino\n\n\n)"  )

water = 1000
Milk = 1000
Coffee = 1000
Money = 1000

#proceed as per user's choice #check if resources are available

if user_choice == "espresso":
    if not water >= 100:
        print("Sorry, There's not enough Water")
    elif not Milk >= 100:
        print("Sorry, There's not enough Milk")
    elif not water >= 100:
        print("Sorry, There's not enough Water")
    else:
        print("Please insert coins")
        input("quarters
        input("dimesnickles = $0.05, pennies = $0.01)

elif user_choice == "latte":
    if not water >= 50:
        print("Sorry, There's not enough Water")
    elif not Milk >= 50:
        print("Sorry, There's not enough Milk")
    elif not water >= 50:
        print("Sorry, There's not enough Water")

elif user_choice == "cappuccino":
    if not water >= 150:
        print("Sorry, There's not enough Water")
    elif not Milk >= 150:
        print("Sorry, There's not enough Milk")
    elif not water >= 150:
        print("Sorry, There's not enough Water")

elif user_choice == "off":
  #turn off the machine
    print("Machine has stopped.")
    sys.exit(0)

elif user_choice == "report":
    print(f"{Water : } ml")
    print(f"{Milk: } ml")
    print(f"{Coffee: } g")
    print(f"{Money: $}")

else:
  print("Please opt for a valid option.")

