import time
import sys
import datetime

# List of appetizers
appetizers = [
    {'name': 'Vegetable salad', 'price': 99, 'stock': 50},
    {'name': 'French Fries', 'price': 89, 'stock': 50},
    {'name': 'Garlic Bread', 'price': 109, 'stock': 50},
    {'name': 'Nachos', 'price': 99, 'stock': 50},
    {'name': 'Soup', 'price': 69, 'stock': 50}

# List of main course
]
foods = [
    {'name': 'Chicken Wings', 'price': 169, 'stock': 50},
    {'name': 'Beef Steak', 'price': 189, 'stock': 50},
    {'name': 'Shrimp Stir-fry', 'price': 159, 'stock': 50},
    {'name': 'Eggplant Omelet', 'price': 149, 'stock': 50},
    {'name': 'Sweet & Sour Por', 'price': 159, 'stock': 50}
]

# List of drinks
drinks = [
    {'name': 'Ice Tea', 'small': 49, 'medium': 59, 'large': 69, 'stock': 50},
    {'name': 'Royal', 'small': 49,'medium': 59, 'large': 59, 'stock': 50},
    {'name': 'Sprite', 'small': 49,'medium': 59, 'large': 59, 'stock': 50},
    {'name': 'Coca-Cola', 'small': 49, 'medium': 59, 'large': 69, 'stock': 50},
    {'name': 'Pineapple', 'small': 49, 'medium': 59, 'large': 69,'stock': 50}

]

# list of desserts
desserts = [
    {'name': 'Leche Flan', 'price': 99, 'stock': 50},
    {'name': 'Dubai Chewy Cookies', 'price': 95, 'stock': 50},
    {'name': 'Ice Cream', 'price': 25, 'stock': 50},
    {'name': 'Chocolate', 'price':25, 'stock': 50},
    {'name': 'Cup cake', 'price': 40, 'stock': 50},

]

# store user accounts
users = []

#Global variables - bills
currentBill = 0
totalBill = 0

# login page
def login(users):
    print('\n---------- LOG IN/SIGN UP ----------')
    attempt = 3
    have_account = input("\nDo you want to log in or sign up? (l/s): ").strip()
    account_found = False

    if have_account.upper() == 'L':
        while attempt > 0: # run until the attempt is equal to 0
            print('\n---------- LOG IN ----------')
            name = input('Enter name: ')
            password = input('Enter password: ')

            for user in users:
                if name == user['fullName'] and password == user['password']:
                    account_found = True
                    print('Succesfully log in')
                    main()
                elif password != user['password'] and name == user['fullName']:
                    attempt -= 1
                    print(f'Attempt left {attempt}')
                    print('Invalid password')
                elif name != user['fullName'] and password == user['password']:
                    attempt -= 1
                    print(f'Attempt left {attempt}')
                    print('Invalid Username')       
            if not account_found:
                        print('Account not found! Please Sign Up first')
                        create_account()
        
    elif have_account.upper() == 'S':
        create_account()
    else:
        print('Invalid Input! Try again')
        login(users)

    
def create_account():
    special_characters = [
        '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '-', '_', '=', '+', '[', ']',
        '{', '}', '|', '\\', ':', ';', '"', "'",
        '<', '>', ',', '.', '?', '/', '`', '~'
    ]
    user_data = {}
    
    print('\n---------- CREATE ACCOUNT----------')
   
    user_data['fullName'] = input('Enter your name: ')
    while True:
        password = input('Enter your password: ')

        if len(password) < 6:
            print('Password is too short! Try again')
            continue

        has_special_char = any(ch in special_characters for ch in password)
        if not has_special_char:
            print('Password must contain special character! Try again')
            continue

        user_data['password'] = password
        break

    user_data['email'] = input('Enter your email: ')
    user_data['street'] = input('Enter your street: ')
    user_data['barangay'] = input('Enter your barangay: ')
    user_data['province'] = input('Enter your province: ')
    print('------------------------------------')

    print('\nAccount Successfully Created')
    users.append(user_data)
    login(users)
    return users


def menu():
    # Display the food menu
    print("\n========== B'TOYS FOOD MENU ==========")
    print('\n---------- APPETIZER ----------')
    for appetizer in appetizers:
        for key, value in appetizer.items():
            print(f'{key}: {value}')
        print()
    print('--------------------')

    print('\n---------- MAIN COURSE ----------')
    for food in foods:
        for key, value in food.items():
            print(f"{key}: {value}")
        print()
    print('--------------------')

    # Display the drink men
    print('\n---------- DRINKS ----------')
    for drink in drinks:
        for key, value in drink.items():
            print(f"{key}: {value}")
        print()
    print('--------------------')

    # Display the dessert section
    print('\n---------- DESSERT ----------')
    for dessert in desserts:
        for key, value in dessert.items():
            print(f"{key}: {value}")
        print()
    print('--------------------')
    
def main():
    print("\n---------- Welcome to B'toys Food Fair -----------")
    print('\nB’TOYS  Food  Fair is  a lively and')
    print('flavorful event where delicious food')
    print('refreshing drinks, and sweet desserts')
    print('come together.')
    while True:
        print('\n---------- CHOICES ----------')
        print('1. Show food menu')
        print('2. Order Appetizer')
        print('3. Order Food')
        print('4. Order Drinks')
        print('5. Order Dessert')
        print('6. Proceed to payment')
        print('7. log out')

        try:
            choice = int(input('Enter choice: '))

            match choice:
                case 1:
                    menu()
                case 2:
                    appetizer_order(appetizers)
                case 3:
                    food_order(foods)
                case 4:
                    drink_order(drinks)
                case 5:
                    dessert_order(desserts)
                case 6:
                    mode_of_payment()
                case 7:
                    print('\nLog out!')
                    login(users)
                case _:
                    print('Invalid Input! Input only 1-7')
        except ValueError:
            print('Invalid value')


def pay():
    try:
        pay = input('Do you want to pay? Y/N: ')

        if pay.upper() == 'Y':
            try:
                print('\n---------- PAYMENT ----------')
                print(f'total is {totalBill}')
                money = float(input('Enter your money: '))
                if money < totalBill:
                    print('Insuficient Amount')
                elif money > totalBill:
                    change = money - totalBill

                    for user in users:
                        print('\n----------- RECIEPT ----------')
                        print(f'total is {totalBill}')
                        print(f'Your change is {change}')
                        print('------------')
                        print('------------')
                        print('You succesfully paid your order')
                        orderTime = datetime.datetime.now()
                        print(f'Thankyou for ordering {user['fullName']}')
                        print(f'Order time {orderTime}')
                        sys.exit()

            except ValueError:
                print('Invalid value')
    except ValueError:
        print('Invalid')

def mode_of_payment():
    global totalBill
    print('\n---------- CHOOSE MOP ----------')
    print('1. Online payment')
    print('2. Cash on deliver')
    try:
       payment_method = int(input('Enter payment method: '))

       match payment_method:
            case 1:
                online_payment()
            case 2:
                print('Preparing your order')
                print('Order preparing wait for 5 minutes')
                time.sleep(3)

                print('Your order is prepared')
                print('Order will delivered in 5 minutes')
                sys.exit()
    except ValueError:
        print('Invalid value')

def online_payment():
    print('\n---------- ONLINE PAYMENT ----------')
    print('1. Gcash')
    print('2. Maya')
    print('3. BDO')
    print('4. PNB Digital')
    choice = int(input('\nEnter your choice: '))

    match choice:
        case 1:
            print('\n---------- GCASH PAYMENT ----------')
            gcashNumber = input('Your Gcash Number: ')
            gcashName = input('Your Gcash Name: ')
            pay()
            return gcashName, gcashNumber
        case 2: 
            print('\n---------- MAYA PAYMENT ----------')
            mayaNumber = input('Your Maya Number: ')
            mayaName = input('Your Maya Name: ')
            pay()
            return mayaName, mayaNumber
        case 3:
            print('\n---------- BDO PAYMENT ----------')
            accountNumber = input('Account number: ')
            accountName = input('Account name: ')
            pay()
            return accountName, accountNumber
        case 4:
            print('\n---------- PNB PAYMENT ----------')
            accountNumber = input('Account number: ')
            accountName = input('Account name: ')
            pay()
            return accountName, accountNumber

def appetizer_order(appetizers):
    global currentBill
    global totalBill
    foundAppetizer = False

    print('\n---------- APPETIZER ORDER ----------')
   
    try:
        appetizer_order = input('Enter your Food Order: ')
        for appetizer in appetizers:
            if appetizer_order.lower() == appetizer['name'].lower():
                if appetizer['stock'] > 0:
                    foundAppetizer = True
                    quantity = int(input('Enter the quantity: '))
                    appetizer['stock'] - quantity

                    print(f'You succesfully order the food {appetizer['name']}')
                    print('\n---------- CURRENT BILL ----------')
                    currentBill = appetizer['price'] * quantity
                    print(f'Your current bill is {currentBill} pesos')
                    totalBill += currentBill
                   
                    try: 
                        while True:
                            print('\n1. Another order')
                            print('2. Proceed to payment')
                            another_order = int(input('\nDo you want Another order or Proceed to Payment?: '))

                            if another_order == 1:
                                main()
                            elif another_order == 2:
                                mode_of_payment()
                    except ValueError:
                        print('Invalid value')
        if not foundAppetizer:
            print('Dessert not found')
    except ValueError:
        print('Invalid Try again')

def food_order(foods):
    global currentBill
    global totalBill
    foundFood = False
    print('\n---------- FOOD ORDER ----------')
   
    try:
        food_order = input('Enter your Food Order: ')
        for food in foods:
            if food_order.lower() == food['name'].lower():
                if food['stock'] > 0:
                    foundFood = True
                    quantity = int(input('Enter the quantity: '))
                    food['stock'] - quantity

                    print(f'\nYou succesfully order the food {food['name']}')
                    print('\n---------- CURRENT BILL ----------')
                    currentBill = food['price'] * quantity
                    print(f'Your current bill is {currentBill} pesos')

                    totalBill += currentBill
                   
                    try: 
                        while True:
                            print('\n1. Another order')
                            print('2. Proceed to payment')
                            another_order = int(input('\nDo you want Another order or Proceed to Payment?: '))

                            if another_order == 1:
                                main()
                            elif another_order == 2:
                                mode_of_payment()
                    except ValueError:
                        print('Invalid value')
        if not foundFood:
            print('Food not found')
    except ValueError:
        print('Invalid Try again')

def drink_order(drinks):
    global currentBill
    global totalBill
    foundDrink = False
    print('\n---------- DRINK ORDER ----------')
   
    try:
        drink_order = input('Enter your Food Order: ')
        for drink in drinks:
            if drink_order.lower() == drink['name'].lower():
                if drink['stock'] > 0:
                    foundDrink = True
                    quantity = int(input('Enter the quantity: '))
                    drink['stock'] - quantity

                    size = input('Enter drink size: Small /Medium /Large: ')
                    if size.lower() == 'SMALL'.lower():
                        currentBill = drink['small'] * quantity
                    elif size.upper() == 'MEDIUM'.upper():
                        currentBill = drink['medium'] * quantity
                    else:
                        currentBill = drink['large'] * quantity

                    print(f'You succesfully order the food {drink['name']}')
                    print('\n---------- CURRENT BILL ----------')
                    print(f'Your current bill is {currentBill} pesos')

                    totalBill += currentBill
                    try: 
                        while True:
                            print('\n1. Another order')
                            print('2. Proceed to payment')
                            another_order = int(input('\nDo you want Another order or Proceed to Payment?: '))

                            if another_order == 1:
                                main()
                            elif another_order == 2:
                                mode_of_payment()
                    except ValueError:
                        print('Invalid value')

        if not foundDrink:
            print('Drink not found')
    except ValueError:
        print('Invalid Try again')

def dessert_order(desserts):
    global currentBill
    global totalBill
    foundDessert = False
    print('\n---------- DESSERT ORDER ----------')
    try:
        dessert_order = input('Enter your Food Order: ')
        for dessert in desserts:
            if dessert_order.lower() == dessert['name'].lower():
                if dessert['stock'] > 0:
                    foundDessert = True
                    quantity = int(input('Enter the quantity: '))
                    dessert['stock'] - quantity

                    print(f'You succesfully order the food {dessert['name']}')
                    print('\n---------- CURRENT BILL ----------')
                    currentBill = dessert['price'] * quantity
                    print(f'Your current bill is {currentBill} pesos')

                    totalBill += currentBill
                
                    try: 
                        while True:
                            print('\n1. Another order')
                            print('2. Proceed to payment')
                            another_order = int(input('\nDo you want Another order or Proceed to Payment?: '))

                            if another_order == 1:
                                main()
                            elif another_order == 2:
                                mode_of_payment()
                    except ValueError:
                        print('Invalid value')

        if not foundDessert:
            print('Dessert not found')
    except ValueError:
        print('Invalid Try again')
    
if __name__ == '__main__':
    login(users)