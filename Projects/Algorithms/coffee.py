menu = {
    1: {'option': 'Black'},
    2: {'option': 'Cream'},
    3: {'option': 'Sugar'},
    4: {'option': 'Cream & Sugar'}
}

# Displays each item inside of the menu dictionary
def display_menu():
    print('-----MENU-----')
    for selection in menu:
        print(f"{selection}. {menu[selection]['option']}")
    print()

# Stores user input inside of order variable, converts string into array and returns it. If invalid input it calls on the display_menu method
def take_order():
    try:
        display_menu()
        
        order = input('How would you like your coffee? ')
        arr = list(order)
        arr.append(menu[int(order)])
        return arr
    except:
        display_menu()

# prints the oder the user chose. Error handling if invalid input it displays a message
def print_order(arr):
    try:
        coffee_order = arr[1]['option']
        if coffee_order == 'Black':
            print('You ordered your coffee ' + coffee_order)
        else:
            print('You ordered your coffee with ' + coffee_order)
    except:
        print('Choose an item from the menu!')

# Steps of program
def main():
        arr = take_order()
        print_order(arr)

# Starts the program
main()