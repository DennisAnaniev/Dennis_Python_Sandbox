def menu(choices, title='Menu', prompt="Enter your choice (1-{}): "):
    """
    This function presents a menu to the user with given choices and returns the selected choice.

    Parameters:
    choices (list): A list of options to be displayed in the menu.
    title (str, optional): The title of the menu. Default is 'Menu'.
    prompt (str, optional): The prompt message to ask the user for their choice. Default is "Enter your choice (1-{}): ".

    Returns:
    str: The selected choice from the list of options.
    """
    print(title)
    print(len(title) * "+")
    i = 1
    for choice in choices:
        print(i, choice)
        i += 1
    choice = int(input(prompt))
    answer = choices[choice - 1]
    return answer

drinks = ["Coke", "Pepsi", "Sprite", "Water", "Juice"]
flavors = ["Mint", "Strawberry", "Lemon", "Grapefruit"]
toppings = ["Cherry", "Blueberry", "Mango", "Pineapple"]

drink = menu(drinks)#, "Select a drink:", "Enter the number of your choice:")
print("You selected:", drink)

flavor = menu(flavors, "Select a flavor:", "Enter the number of your choice:")
print("You selected:", flavor)

topping = menu(toppings, "Select a topping:", "Enter the number of your choice:")
print("You selected:", topping)

print("\nYour order:")
print("Drink:", drink)
print("Flavor:", flavor)
print("Topping:", topping)
