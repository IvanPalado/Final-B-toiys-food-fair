import time
import sys
import datetime

# List of appetizers
appetizers = [
    {'number': 'A1', 'name': 'Vegetable salad', 'price': 99, 'stock': 50},
    {'number': 'A2', 'name': 'French Fries', 'price': 89, 'stock': 50},
    {'number': 'A3', 'name': 'Garlic Bread', 'price': 209, 'stock': 50},
    {'number': 'A4', 'name': 'Nachos', 'price': 99, 'stock': 50},
    {'number': 'A5', 'name': 'Soup', 'price': 69, 'stock': 50}
]
# List of main course
foods = [
    {'number': 'F1', 'name': 'Chicken Wings', 'price': 169, 'stock': 50},
    {'number': 'F2', 'name': 'Beef Steak', 'price': 189, 'stock': 50},
    {'number': 'F3', 'name': 'Shrimp Stir-fry', 'price': 159, 'stock': 50},
    {'number': 'F4', 'name': 'Eggplant Omelet', 'price': 149, 'stock': 50},
    {'number': 'F5', 'name': 'Sweet & Sour Por', 'price': 159, 'stock': 50}
]
# List of drinks
drinks = [
    {'number': 'D1', 'name': 'Ice Tea', 'small': 49, 'medium': 59, 'large': 69, 'stock': 50},
    {'number': 'D2', 'name': 'Royal', 'small': 49, 'medium': 59, 'large': 59, 'stock': 50},
    {'number': 'D3', 'name': 'Sprite', 'small': 49, 'medium': 59, 'large': 59, 'stock': 50},
    {'number': 'D4', 'name': 'Coca-Cola', 'small': 49, 'medium': 59, 'large': 69, 'stock': 50},
    {'number': 'D5', 'name': 'Pineapple', 'small': 49, 'medium': 59, 'large': 69,'stock': 50}
]
# list of desserts
desserts = [
    {'number': 'DE1', 'name': 'Leche Flan', 'price': 99, 'stock': 50},
    {'number': 'DE2', 'name': 'Dubai Chewy Cookies', 'price': 95, 'stock': 50},
    {'number': 'DE3', 'name': 'Ice Cream', 'price': 25, 'stock': 50},
    {'number': 'DE4', 'name': 'Chocolate', 'price':25, 'stock': 50},
    {'number': 'DE5', 'name': 'Cup cake', 'price': 40, 'stock': 50},

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
    have_account = input("Do you want to log in or sign up? (login/signup): ").lower()
    account_found = False

    if have_account == 'l' or have_account == 'login':
        while attempt > 0:
            print('\n---------- LOG IN ----------')
            name = input('Enter name: ')
            password = input('Enter password: ')

            for user in users:
                if name == user['fullName'] and password == user['password']:
                    account_found = True
                    print('Succesfully log in')
                    main()
                elif name != user['fullName'] and password == user['password']:
                    print('Invalid Username')  
                elif password != user['password'] and name == user['fullName']:
                    attempt -= 1
                    print(f'Attempt left {attempt}')
                    print('Invalid password')     
            if not account_found:
                        print('Account not found! Please Sign Up first')
                        create_account()
    elif have_account == 's' or have_account == 'signup':
        create_account()
    else:
        print('Invalid Input! Try again')
        login(users)

# Create account
def create_account():
    special_characters = [
        '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '-', '_', '=', '+', '[', ']',
        '{', '}', '|', '\\', ':', ';', '"', "'",
        '<', '>', ',', '.', '?', '/', '`', '~'
    ]
    user_data = {}

    print('\n---------- CREATE ACCOUNT----------')
    while True:
        name = input('Enter your full name: ')

        if name == "":
            print('Name cannot be empty')
            continue

        user_data['fullName'] = name
        break

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

    while True:
        email = input('Enter your email: ')

        if email == "":
            print('Email cannot be empty')
            continue

        user_data['email'] = email
        break

    while True:
        street = input('Enter your street: ')

        if street == "":
            print('street cannot be empty')
            continue

        user_data['street'] = street
        break

    while True:
        baranggay = input('Enter your baranggay: ')

        if baranggay == "":
            print('branggay cannot be empty')
            continue

        user_data['baranggay'] = baranggay
        break

    while True:
        municipality = input('Enter your municipality: ')

        if municipality == "":
            print('municipality cannot be empty')
            continue

        user_data['municipality'] = municipality
        break

    while True:
        province = input('Enter your province: ')

        if province == "":
            print('province cannot be empty')
            continue

        user_data['province'] = province
        break
        
    print('------------------------------------')

    print('\nAccount Successfully Created')
    users.append(user_data)
    main()
    return users

# Food menu
def menu():
    # Display the food menu
    print("\n========== B'TOYS FOOD MENU ==========")
    # Display the appetizer menu
    print('\n------------------------------ APPETIZER ------------------------------')
    print(f"{'APPETIZER NUMBER':<20} {'NAME':<20} {'PRICE':<20} {'STOCK':<20}")
    for appetizer in appetizers:
        print(f"{appetizer['number']:<20} {appetizer['name']:<20} {appetizer['price']:<20} {appetizer['stock']:<20}")

    # Display the food menu
    print('\n------------------------------ MAIN COURSE ------------------------------')
    print(f"{'FOOD NUMBER':<20} {'NAME':<20} {'PRICE':<20} {'STOCK':<20}")
    for food in foods:
        print(f"{food['number']:<20} {food['name']:<20} {food['price']:<20} {food['stock']:<20}")

    # Display the drink menu
    print('\n------------------------------ DRINKS ------------------------------')
    print(f"{'DRINK NUMBER':<20} {'NAME':<20} {'SMALL PRICE':<20} {'MEDIUM PRICE':<20} {'LARGE PRICE':<20} {'STOCK':<20}")
    for drink in drinks:
        print(f"{drink['number']:<20} {drink['name']:<20} {drink['small']:<20} {drink['medium']:<20} {drink['large']:<20} {drink['stock']:<0}")

    # Display the dessert sections
    print('\n------------------------------ DESSERT ------------------------------')
    print(f"{'DESSERT NUMBER':<20} {'NAME':<20} {'PRICE':<20} {'STOCK':<20}")
    for dessert in desserts:
        print(f"{dessert['number']:<20} {dessert['name']:<20} {dessert['price']:<20} {dessert['stock']:<20}")

# Main page  
def main():
    print("\n---------- Welcome to B'toys Food Fair -----------")
    print('B’TOYS  Food  Fair is  a lively and')
    print('flavorful event where delicious food')
    print('refreshing drinks, and sweet desserts')
    print('come together.')
    while True:
        print('\n---------- CHOICES ----------')
        print('1. FOOD MENU')
        print('2. APPETIZER')
        print('3. MAIN COURE')
        print('4. DRINK')
        print('5. DESSERT')
        print('6. PROCEED TO PAYMENT')
        print('7. LOG OUT')

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

# Pay section
def pay():
    try:
        pay = input('Would you like to proceed with payment? (yes/no)').lower()

        if pay == 'yes':
            try:
                print('\n---------- PAYMENT ----------')
                print(f'total is {totalBill}₱')
                money = float(input('Please enter the payment amount: '))
                if money < totalBill:
                    print('Insuficient Amount')
                    cancel = input('Do you want to cancel your payment? (yes/no): ').lower()

                    if cancel == 'yes':
                        sys.exit()
                    else:
                        print('Enter the valid amount')

                elif money > totalBill:
                    change = money - totalBill

                    for user in users:
                        print('\n----------- RECIEPT ----------')
                        print(f'total is {totalBill}₱')
                        print(f'Your change is {change}₱')
                        print('------------')
                        print('------------')
                        print('You succesfully paid your order')
                        orderTime = datetime.datetime.now()
                        print(f'Thankyou for ordering {user['fullName']}')
                        print(f'Order time {orderTime}')
                        sys.exit()
            except ValueError:
                print('Invalid value')
        if pay == 'no':
            print('You cancel your payment')
            sys.exit()
            
    except ValueError:
        print('Invalid')

# mode of payment
def mode_of_payment():
    global totalBill
    print('\n---------- CHOOSE MOP ----------')
    print('1. Online payment')
    print('2. Cash on delivery')
    try:
       payment_method = int(input('Enter payment method: '))

       match payment_method:
            case 1:
                online_payment()
            case 2:
                print('Preparing your order')
                print('Order preparing please wait for a minute!')
                time.sleep(3)

                print('Your order is prepared')
                print('Order will delivered in 5 minutes')
                menu()
            case _:
               print('Invalid input. Kindly enter either 1 or 2')
    except ValueError:
        print('Invalid value')

# Online Payment
def online_payment():
    print('\n---------- ONLINE PAYMENT ----------')
    print('1. Gcash')
    print('2. Maya')
    print('3. BDO')
    print('4. PNB Digital')
    choice = int(input('\nEnter your choice: '))

    match choice:
        case 1:
            print('\n========== GCASH PAYMENT ==========')
            print("Merchant : B'toys Food Fair")
            print("Method   : GCash")
            print("----------------------------------")
            print("Note     : Please enter your GCash details correctly.\n")

            account_number = input("GCash Number  : ")
            account_name = input("Account Name  : ")

        case 2:
            print('\n========== MAYA PAYMENT ==========')
            print("Merchant : B'toys Food Fair")
            print("Method   : Maya")
            print("----------------------------------")
            print("Note     : Please enter your Maya details correctly.\n")

            account_number = input("Maya Number   : ")
            account_name = input("Account Name  : ")

        case 3:
            print('\n========== BDO PAYMENT ==========')
            print("Merchant : B'toys Food Fair")
            print("Bank     : BDO")
            print("----------------------------------")
            print("Note     : Ensure your bank details are correct.\n")

            account_number = input("Account Number: ")
            account_name = input("Account Name  : ")

        case 4:
            print('\n========== PNB PAYMENT ==========')
            print("Merchant : B'toys Food Fair")
            print("Bank     : PNB")
            print("----------------------------------")
            print("Note     : Ensure your bank details are correct.\n")

            account_number = input("Account Number: ")
            account_name = input("Account Name  : ")

        case _:
            print("\nInvalid choice! Please select 1–4 only.")
            return None

    print("\n---------- PAYMENT DETAILS ----------")
    print(f"Name   : {account_name}")
    print(f"Number : {account_number}")

    confirm = input("\nConfirm payment? (yes/no): ").lower()

    if confirm == "yes":
        pay()
        print("Payment Successful! Thank you for ordering at B'toys Food Fair 🍔")
        return account_name, account_number
    else:
        print("Payment cancelled.")
        return None

# Appetizer order
def appetizer_order(appetizers):
    global currentBill
    global totalBill
    foundAppetizer = False

    print('\n------------------------------ APPETIZER ------------------------------')
    print(f"{'APPETIZER NUMBER':<20} {'NAME':<20} {'PRICE':<20} {'STOCK':<20}")
    for appetizer in appetizers:
        print(f"{appetizer['number']:<20} {appetizer['name']:<20} {appetizer['price']:<20} {appetizer['stock']:<20}")
    try:
        appetizer_order = input('Enter your Food Order: ')
        for appetizer in appetizers:
            if appetizer_order.lower() == appetizer['name'].lower() or appetizer_order.upper() == appetizer['number']:
                if appetizer['stock'] > 0:
                    foundAppetizer = True
                    quantity = int(input('Enter the quantity: '))
                    appetizer['stock'] - quantity

                    print('\n---------- ORDER DETAILS ---------- ')
                    print(f'You order: {appetizer['name']}')
                    currentBill = appetizer['price'] * quantity
                    print(f'Your current bill is {currentBill} ₱')
                    totalBill += currentBill
                    try: 
                        while True:
                            print('\n1. Add another order')
                            print('2. Proceed to payment')
                            another_order = int(input('\nDo you want to add another order or Proceed to Payment?: '))

                            if another_order == 1:
                                main()
                            elif another_order == 2:
                                mode_of_payment()
                    except ValueError:
                        print('Invalid value')
        if not foundAppetizer:
            print('Appetizer not found')
    except ValueError:
        print('Invalid Try again')

# Food order
def food_order(foods):
    global currentBill
    global totalBill
    foundFood = False
    print('\n------------------------------ MAIN COURSE ------------------------------')
    print(f"{'FOOD NUMBER':<20} {'NAME':<20} {'PRICE':<20} {'STOCK':<20}")
    for food in foods:
        print(f"{food['number']:<20} {food['name']:<20} {food['price']:<20} {food['stock']:<20}")

    try:
        food_order = input('Enter your Food Order: ')
        for food in foods:
            if food_order.lower() == food['name'].lower() or food_order.upper() == food['number']:
                if food['stock'] > 0:
                    foundFood = True
                    quantity = int(input('Enter the quantity: '))
                    food['stock'] - quantity

                    print('\n---------- ORDER DETAILS ---------- ')
                    print(f'You order: {food['name']}')
                    currentBill = food['price'] * quantity
                    print(f'Your current bill is {currentBill}₱')
                    totalBill += currentBill
                    try: 
                        while True:
                            print('\n1. Add another order')
                            print('2. Proceed to payment')
                            another_order = int(input('\nDo you want to add another order or Proceed to Payment?: '))

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

# Drink order
def drink_order(drinks):
    global currentBill
    global totalBill
    foundDrink = False
    print('\n------------------------------ DRINKS ------------------------------')
    print(f"{'DRINK NUMBER':<20} {'NAME':<20} {'SMALL PRICE':<20} {'MEDIUM PRICE':<20} {'LARGE PRICE':<20} {'STOCK':<20}")
    for drink in drinks:
        print(f"{drink['number']:<20} {drink['name']:<20} {drink['small']:<20} {drink['medium']:<20} {drink['large']:<20} {drink['stock']:<0}")

    try:
        drink_order = input('Enter your drink Order: ')
        for drink in drinks:
            if drink_order.lower() == drink['name'].lower() or drink_order.upper() == drink['number']:
                if drink['stock'] > 0:
                    foundDrink = True
                    quantity = int(input('Enter the quantity: '))
                    drink['stock'] - quantity

                    size = input('Enter drink size: Small/Medium/Large: ').lower()
                    if size == 'small':
                        currentBill = drink['small'] * quantity
                    elif size == 'medium':
                        currentBill = drink['medium'] * quantity
                    elif size == 'large':
                        currentBill = drink['large'] * quantity

                    print('\n---------- ORDER DETAILS ---------- ')
                    print(f'You order: {drink['name']}')
                    if size == 'small':
                        print('drink size: small')
                    elif size == 'medium':
                        print('drink size: medium')
                    elif size == 'large':
                        print('drink size: large')
                    print(f'Your current bill is {currentBill}₱')
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

# Dessert order
def dessert_order(desserts):
    global currentBill
    global totalBill
    foundDessert = False
    print('\n------------------------------ DESSERT ------------------------------')
    print(f"{'DESSERT NUMBER':<20} {'NAME':<20} {'PRICE':<20} {'STOCK':<20}")
    for dessert in desserts:
        print(f"{dessert['number']:<20} {dessert['name']:<20} {dessert['price']:<20} {dessert['stock']:<20}")
    try:
        dessert_order = input('Enter your dessert Order: ')
        for dessert in desserts:
            if dessert_order.lower() == dessert['name'].lower() or dessert_order.upper() == dessert['number']:
                if dessert['stock'] > 0:
                    foundDessert = True
                    quantity = int(input('Enter the quantity: '))
                    dessert['stock'] - quantity

                    print('\n---------- ORDER DETAILS ---------- ')
                    print(f'You order: {dessert['name']}')
                    currentBill = dessert['price'] * quantity
                    print(f'Your current bill is {currentBill}₱')
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
    
# Run if the file is run
if __name__ == '__main__':
    login(users)