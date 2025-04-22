from menu import Menu, FoodItem, Pizza, Drink, Burger, AlcoDrink
from restaurant import Restaurant, my_restaurant
from staff import Staff

def ui():
    while True:
        print('Choose an option:')
        print('1. Add food')
        print('2. Add drink')
        print('3. Remove food')
        print('4. Remove drink')
        print('5. Show menu')
        print('6. Show staff') 
        print('7. Add staff')
        print('8. Remove staff')
        print('0. To Quit')

        choice = input('type an option: ')
        if choice == 1:
            print('Add food')
            food_type = input('Enter food type (Pizza, Burger, Salad, Dessert): ')
            if food_type == 'Pizza':
                my_restaurant.menu.add_food(Pizza)
            elif food_type == 'Burger':
                my_restaurant.menu.add_food(Burger)
            else:
                print('Invalid food type!')
            my_restaurant.menu.add_food()
        elif choice == 2:
            pass
        elif choice == 3:
            m1 = Menu()
            
ui()