# Authors: Damian Zukowski, Ho Kim, Quang Anh Nguyen, Quan Nguyen

""" This file containt Menu with all the Food items """


class Menu:
    def __init__(self):
        self.food_items = []
        self.drinks = []

    # Adds a food item to the menu
    def add_food(self, food_item):
        if food_item not in self.food_items:
            self.food_items.append(food_item)
        else:
            print(f"The {food_item} is already on the menu!")

    # Adds a drink to the menu
    def add_drink(self, drink):
        if drink not in self.drinks:
            self.drinks.append(drink)
        else:
            print(f"{drink} is already on the menu!")

    # Removes a food item from the menu
    def remove_food(self, food_item):
        if food_item in self.food_items:
            self.food_items.remove(food_item)
        else:
            print(f"The {food_item} is not on the menu!")

    # Removes a drink from the menu
    def remove_drink(self, drink):
        if drink in self.drinks:
            self.drinks.remove(drink)
        else:
            print(f"{drink} is not on the menu!")

    # Prints all contents of the menu -> to be upgraded, possibly a dict or unpacking the list into a nice string
    def show_menu(self):
        print(f"All available food: {self.food_items} \n All available drinks: {self.drinks}")


# Parent FoodItem and Drink classes
class FoodItem:
    def __init__(self, name: str, price: float, category: str, calories: int, spicyness: str, allergens: str, is_vege: bool):
        self._name = name
        self._price = price
        self._category = category
        self._calories = calories
        self._spicyness = spicyness
        self._allergens = allergens
        self._is_vege = is_vege

    def __str__(self):
        return f"{self._name} {self._price} USD, {self._category}, {self._calories} kcal, Spicy: {self._spicyness}, Allergens: {self._allergens}, Vegetarian: {self._is_vege}"


class Drink:
    def __init__(self, name: str, price: float, size: float, temp: str):
        self._name = name
        self._price = price
        self._size = size
        self._temp = temp


# Food items 
class Burger(FoodItem):
    # Args handles positional arguments (values, "Cheeseburger"), kwargs handles keyword arguments (attributes, name=Cheeseburger)
    def __init__(self, size: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._size = size

    def __str__(self):
        return f"{super().__str__()}, Size: {self._size}"



# Test object and print
nowy_borgir = Burger("XXL", "cheesebrgr", 29.99, "burger", 700, "medium", "G, E", False)  
print(nowy_borgir)
        
    

