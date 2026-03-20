# B'toys Food Fair
import time
import sys

appetizers = [
    {'name': 'Vegetable salad', 'price': 99, 'stock': 50},
    {'name': 'French Fries', 'price': 89, 'stock': 50},
    {'name': 'Garlic Bread', 'price': 109, 'stock': 50},
    {'name': 'Nachos', 'price': 99, 'stock': 50},
    {'name': 'Soup', 'price': 69, 'stock': 50}


]
foods = [
    {'name': 'Chicken Wings', 'price': 169, 'stock': 50},
    {'name': 'Beef Steak', 'price': 189, 'stock': 50},
    {'name': 'Shrimp Stir-fry', 'price': 159, 'stock': 50},
    {'name': 'Eggplant Omelet', 'price': 149, 'stock': 50},
    {'name': 'Sweet & Sour Por', 'price': 159, 'stock': 50}
]

drinks = [
    {'name': 'Ice Tea', 'small': 49, 'medium': 59, 'large': 69, 'stock': 50},
    {'name': 'Royal', 'small': 49,'medium': 59, 'large': 59, 'stock': 50},
    {'name': 'Sprite', 'small': 49,'medium': 59, 'large': 59, 'stock': 50},
    {'name': 'Coca-Cola', 'small': 49, 'medium': 59, 'large': 69, 'stock': 50},
    {'name': 'Pineapple', 'small': 49, 'medium': 59, 'large': 69,'stock': 50}

]

desserts = [
    {'name': 'Leche Flan', 'price': 99, 'stock': 50},
    {'name': 'Dubai Chewy Cookies', 'price': 95, 'stock': 50},
    {'name': 'Ice Cream', 'price': 25, 'stock': 50},
    {'name': 'Chocolate', 'price':25, 'stock': 50},
    {'name': 'Cup cake', 'price': 40, 'stock': 50},

]

users = []


currentBill = 0
totalBill = 0

def login(users):
    attempt = 3
    print("\n---------- Welcome to B'toys Food Fair -----------")
    print('\nB’TOYS Food Fair is a lively and flavorful event where delicious food, refreshing drinks, and sweet desserts come together.')
    have_account = input('\nDo you have account? Y or N: ')
    if have_account.upper() == 'Y':
        while attempt > 0:
            print('\n---------- LOG IN ----------')
            name = input('Enter name: ')
            password = input('Enter password: ')
            for user in users:
                if name == user['fullName'] and password == user['password']:
                    print('Succesfully log in')
                    main()
                else:
                    attempt -= 1
                    print('Invalid password')
                    print(f'Attempt left {attempt}')
    else:
        create_account()

    
def create_account():
    user_data = {}
    print('\n---------- CREATE ACCOUNT----------')
    user_data['fullName'] = input('Enter your name: ')
    user_data['password'] = input('Enter your password: ')
    user_data['adsress'] = input('Enter your address: ')
    user_data['email'] = input('Enter your email: ')
    user_data['province'] = input('Enter your province: ')
    user_data['barangay'] = input('Enter your barangay: ')
    user_data['street'] = input('Enter your streetn: ')
    print("\nYou Succesfully Created Your Account in B'toys Food Fair")
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
    menu()
    while True:
        print('\n---------- FOOD CATEGORY ----------')
        print('1. Appetizer')
        print('2. Food')
        print('3. Drinks')
        print('4. Dessert')
        print('5. Show food menu')
        print('6. Proceed to payment')
        print('7. Exit')

        try:
            choice = int(input('Enter category: '))

            match choice:
                case 1:
                    appetizer_order(appetizers)
                case 2:
                    food_order(foods)
                case 3:
                    drink_order(drinks)
                case 4:
                    menu()
                case 5:
                    menu()
                case 6:
                    payment()
                case 7:
                    print('\nTerminating the program')
                    break
        except ValueError:
            print('Invalid value')


def pay():
    try:
        pay = input('Do you want to pay? Y/N: ')

        if pay.upper() == 'Y':
            try:
                print('\n---------- PAYMENT ----------')
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
                        print(f'Thankyou for ordering {user['fullName']}')
                        sys.exit()

            except ValueError:
                print('Invalid value')
    except ValueError:
        print('Invalid')

def payment():
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
               cod()
    except ValueError:
        print('Invalid value')

def cod():
    print('Preparing your order')
    print('Order preparing wait for 5 minutes')
    time.sleep(300)

    print('Your order is prepared')
    print('Order will delivered in 5 minutes')
    sys.exit()

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
                    foundAppetizerr = True
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
                                payment()
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
                                payment()
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
                                payment()
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
                                payment()
                    except ValueError:
                        print('Invalid value')
        if not foundDessert:
            print('Dessert not found')
    except ValueError:
        print('Invalid Try again')
    
if __name__ == '__main__':
    login(users)