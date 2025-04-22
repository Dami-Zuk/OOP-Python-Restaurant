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

        choice = int(input('type an option: '))
        if choice == 1:
            print('Add food')
            food_type = input('Enter food type (Pizza, Burger, Salad, Dessert): ')
            if food_type == 'Pizza':
                pizza = Pizza('Pineapple Paradise', 15.99, 'Large', 'Tomato sauce, pineapple, ham')
                my_restaurant.menu.add_food(pizza)
            elif food_type == 'Burger':
                burger = Burger('Bacon tornado', 19.99, 'Beef', 'Lettuce, tomato, cheese, bacon')
                my_restaurant.menu.add_food(burger)
            else:
                print('Invalid food type!')
            my_restaurant.menu.add_food()
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
            m1 = Menu()
            food_name = input('Enter food name to remove: ')
            for food in my_restaurant.menu.food_items:
                if food._name == food_name:
                    my_restaurant.menu.remove_food(food)
                    break
            else:
                print('Food not found!')
        elif choice == 4:
            m1 = Menu()
            drink_name = input('Enter drink name to remove: ')
            for drink in my_restaurant.menu.drinks:
                if drink._name == drink_name:
                    my_restaurant.menu.remove_drink(drink)
                    break
            else:
                print('Drink not found!')
        elif choice == 5:       
            m1 = Menu()
            print('Menu:')
            print('Food items:')
            for food in my_restaurant.menu.food_items:
                print(f'Name: {food._name}, Price: {food._price}, Category: {food._category}')

            print('Drinks:')
            for drink in my_restaurant.menu.drinks:
                if isinstance(drink, AlcoDrink):
                    print(f'Name: {drink._name}, Price: {drink._price}, Alcohol content: {drink._alc}%')
                else:
                    print(f'Name: {drink._name}, Price: {drink._price}, Size: {drink._size}ml, Temperature: {drink._temp}')


        elif choice == 6:  
            my_restaurant.show_staff()

        elif choice == 7: 
            new_staff = Staff(input('First name: '), input('Last name: '), input('Gender: '), input('Salary:'))      
            my_restaurant.add_staff(new_staff)    
        
        elif choice == 8:
            f_name = input('First name: ')
            l_name = input('Last name: ')
            for member in my_restaurant.staff_members:
                if member._fname == f_name and member._lname == l_name:
                    my_restaurant.remove_staff(member)
                    break
        elif choice == 9:
            pass
        elif choice == 0:
            break

        else:
            print('Invalid option!')
            
ui()
