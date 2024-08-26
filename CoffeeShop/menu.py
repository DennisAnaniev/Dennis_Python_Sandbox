drinks = ["Coke", "Pepsi", "Sprite", "Water", "Juice"]
flavors = ["Mint", "Strawberry", "Lemon", "Grapefruit"]
toppings = ["Cherry", "Blueberry", "Mango", "Pineapple"]

print("Select a drink:")
print("+++++ DRINKS +++++++++++")
i = 1
for drink in drinks:
    print(i, drink)
    i += 1

drink_choice = int(input("Enter the number of your choice: "))

print("\nSelect a flavor:")
print("+++++ FLAVORS +++++++++++")
i = 1
for flavor in flavors:
    print(i, flavor)
    i += 1

flavor_choice = int(input("Enter the number of your choice: "))

print("\nSelect a topping:")
print("+++++ TOPPINGS +++++++++++")
i = 1
for topping in toppings:
    print(i, topping)
    i += 1

topping_choice = int(input("Enter the number of your choice: "))

print("\nYour order:")
print("Drink:", drinks[drink_choice - 1])
print("Flavor:", flavors[flavor_choice - 1])
print("Topping:", toppings[topping_choice - 1])
