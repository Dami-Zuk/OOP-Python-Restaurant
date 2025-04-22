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
                pizza = Pizza('Pineapple Paradise', 15.99, 'Large', 'Tomato sauce, pineapple, ham')
                my_restaurant.menu.add_food(pizza)
            elif food_type == 'Burger':
                burger = Burger('Bacon tornado', 19.99, 'Beef', 'Lettuce, tomato, cheese, bacon')
                my_restaurant.menu.add_food(burger)
            else:
                print('Invalid food type!')
            my_restaurant.menu.add_food()
        elif choice == 2:
            pass
        elif choice == 3:
            m1 = Menu()
        elif choice == 4:
            m1 = Menu()
        elif choice == 5:       
            m1 = Menu()
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

        else:
            print('Invalid option!')
            
ui()