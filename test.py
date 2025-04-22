from menu import Menu, FoodItem, Pizza, Drink, Burger, AlcoDrink
from restaurant import Restaurant, my_restaurant
from staff import Staff

def ui():
    """
    Command-line interface for interacting with the restaurant system.
    """
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

        try:
            choice = int(input('Type an option: '))
        except ValueError:
            print('Invalid input! Please enter a number.')
            continue

        if choice == 1:
            print('Add food')
            food_name = input('Enter food name: ')
            food_price = float(input('Enter food price: '))
            food_type = input('Enter food type (Pizza, Burger, Salad, Dessert): ')
            if food_type == 'Pizza':
                pizza = Pizza(food_name, food_price, 'Large', 'Custom ingredients')
                my_restaurant.menu.add_food(pizza)
            elif food_type == 'Burger':
                burger = Burger(food_name, food_price, 'Beef', 'Custom ingredients')
                my_restaurant.menu.add_food(burger)
            else:
                print('Invalid food type!')

        elif choice == 2:
            print('Add drink')
            drink_type = input('Enter drink type (AlcoDrink, Drink): ')
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            size = float(input("Enter size in ml: "))
            temp = input("Enter temperature (Hot, Cold, Normal): ")

            if drink_type == 'AlcoDrink':
                alcohol_content = float(input("Enter alcohol content (%): "))
                alco_drink = AlcoDrink(alcohol_content, name, price, size, temp)
                my_restaurant.menu.add_drink(alco_drink)
            elif drink_type == 'Drink':
                drink = Drink(name, price, size, temp)
                my_restaurant.menu.add_drink(drink)
            else:
                print('Invalid drink type!')

        elif choice == 3:
            food_name = input('Enter food name to remove: ')
            for food in my_restaurant.menu.food_items:
                if food.name == food_name:
                    my_restaurant.menu.remove_food(food)
                    break
            else:
                print('Food not found!')

        elif choice == 4:
            drink_name = input('Enter drink name to remove: ')
            for drink in my_restaurant.menu.drinks:
                if drink.name == drink_name:
                    my_restaurant.menu.remove_drink(drink)
                    break
            else:
                print('Drink not found!')
        elif choice == 5:       
            print('Menu:')
            my_restaurant.menu.show_menu()  

        elif choice == 6:
            my_restaurant.show_staff()

        elif choice == 7:
            first_name = input('First name: ')
            last_name = input('Last name: ')
            gender = input('Gender: ')
            salary = float(input('Salary: '))
            new_staff = Staff(first_name, last_name, gender, salary)
            my_restaurant.add_staff(new_staff)

        elif choice == 8:
            first_name = input('First name: ')
            last_name = input('Last name: ')
            my_restaurant.remove_staff(first_name, last_name)

        elif choice == 0:
            print('Exiting...')
            break

        else:
            print('Invalid option!')

#test the UI    
ui()
