# Authors: Damian Zukowski, Ho Kim, Quang Anh Nguyen, Quan Nguyen

""" This is the main file """

import staff
import menu


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.staff_members = []
        self.menu = menu.Menu()
        self.orders = []  

    # Add a staff member
    def add_staff(self, staff_member):
        if staff_member not in self.staff_members:
            self.staff_members.append(staff_member)
        else:
            print(f"{staff_member._fname} join our team!")

    # Remove a staff member
    def remove_staff(self, fname, lname):
        for member in self.staff_members:
            if member._fname == fname and member._lname == lname:
                self.staff_members.remove(member)
                print(f"{fname} {lname} quit the job!")
                return False
        print(f"Staff member {fname} {lname} not found!")

    # Find a staff member
    def find_staff(self, fname, lname):
        for member in self.staff_members:
            if member._fname == fname and member._lname == lname:
                return f"{member._fname} {member._lname} - {type(member).__name__}"
        return f"Staff member {fname} {lname} not found!"

    # Show all staff
    def show_staff(self):
        print(f"Staff at {self.name}:")
        for member in self.staff_members:
            print(f"{member._fname} {member._lname} - {type(member).__name__}")

    # Show the menu
    def show_menu(self):
        self.menu.show_menu()

    # Take an order (customer orders food and drinks)
    def take_order(self, food_name, drink_name):
        food = next((f for f in self.menu.food_items if f._name == food_name), None)
        drink = next((d for d in self.menu.drinks if d._name == drink_name), None)

        if food and drink:
            self.orders.append((food, drink))
            print(f"Order placed: {food._name} and {drink._name}.")
        else:
            print("One or more items are not available on the menu!")

    # Process orders (simulate cooking and serving)
    def process_orders(self):
        if not self.orders:
            print("No orders to process!")
            return

        for order in self.orders:
            food, drink = order
            print(f"Preparing {food._name} and {drink._name}...")
        
        print("All orders have been completed!")
        self.orders.clear()

    # Close the restaurant (clear staff and menu)
    def close_restaurant(self):
        self.staff_members.clear()
        self.menu.food_items.clear()
        self.menu.drinks.clear()
        self.orders.clear()
        print(f"{self.name} is now closed for the day!")


# Testing the restaurant setup
if __name__ == "__main__":
    my_restaurant = Restaurant("My Quang so 1 Quang Nam")

    # Adding staff
    souschef = staff.SousChef("Quan", "Nguyen", "Male", 50)
    waiter = staff.Server("QuangAnh", "Nguyen", "Male", 24)
    bartender = staff.Bartender("Damian", "Zuski", "Female", 25)
    chef = staff.HeadChef("Kim", "Ho", "Male", 18)

    my_restaurant.add_staff(waiter)
    my_restaurant.add_staff(bartender)
    my_restaurant.add_staff(chef)
    my_restaurant.add_staff(souschef)

    # Adding menu items
    burger = menu.Burger("Large", "Cheeseburger", 10.99, "Main Course", 600, "Medium", "G, E", False)
    drink = menu.Drink("Cola", 2.99, 500, "Cold")

    my_restaurant.menu.add_food(burger)
    my_restaurant.menu.add_drink(drink)

    # Displaying information
    my_restaurant.show_staff()
    print("\nMenu:")
    my_restaurant.show_menu()

    # Taking and processing orders
    my_restaurant.take_order("Cheeseburger", "Cola")
    my_restaurant.process_orders()

    # Removing staff
    my_restaurant.remove_staff("QuangAnh", "Nguyen")

    # Closing restaurant
    my_restaurant.close_restaurant()
