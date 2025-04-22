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
        print(f"All available food:")
        for item in self.food_items:
            print(f'{item._name}, {item._price} EUR, {item._category}, {item._calories} kcal, Spicyness: {item._spicyness}, Allergens: {item._allergens}, Vegetarian: {item._is_vege}')
        print(f"All available drinks:")
        for drink in self.drinks:
            print(f'{drink._name}, {drink._price} EUR, Size: {drink._size} ml, Temperature: {drink._temp}')

# Parent FoodItem 
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
        return f"{self._name}, {self._price} EUR, {self._category}, {self._calories} kcal, Spicyness: {self._spicyness}, Allergens: {self._allergens}, Vegetarian: {self._is_vege}"


# Pizza
class Pizza(FoodItem):
    def __init__(self, size: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._size = size

    def __str__(self):
        return f"{super().__str__()}, Size: {self._size}"

 
# Burger
class Burger(FoodItem):
    # Args handles positional arguments (values, "Cheeseburger"), kwargs handles keyword arguments (attributes, name=Cheeseburger)
    def __init__(self, size: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._size = size

    def __str__(self):
        return f"{super().__str__()}, Size: {self._size}"


# Parent Drink
class Drink:
    def __init__(self, name: str, price: float, size: float, temp: str):
        self._name = name
        self._price = price
        self._size = size
        self._temp = temp

    def __str__(self):
        return f"{self._name}, {self._price} EUR, Size: {self._size} ml, Temperature: {self._temp}"
    

# Alcoholic drinks
class AlcoDrink(Drink):
    def __init__(self, alc_content: float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._alc = alc_content

    def __str__(self):
        return f"{super().__str__()}, Alc: {self._alc}%"


# FOOD ITEMS

# Sandwiches and burgers
ChickenBurger = Burger("XL", "Chicken Burger", 15.99, "Burgers", 600, "Low", "G", False)
ClubSandwich = Burger("Normal", "Club Sandwich", 13.99, "Burgers", 300, "Low", "G, L", False)
FalafelPita = Burger("L", "Falafel Pita", 12.99, "Burgers", 280, "Low", "G", True)
BahnMi = Burger("XXL", "Bahn Mi :3", 9.99, "Burgers", 470, "Medium", "G", False)

# Pasta dishes
SpaghettiBolognese = FoodItem("Spaghetti Bolognese", 17.99, "Pasta dish", 700, "Low", "G", False)
SpaghettiCarbonara = FoodItem("Spaghetti Carbonara", 17.99, "Pasta dish", 650, "Low", "G, L", True)
Lasagne = FoodItem("Lasagne", 16.99, "Pasta dish", 800, "Low", "G, L", False)
MacAndCheese = FoodItem("Mac and Cheese", 12.99, "Pasta dish", 540, "Low", "G, L", True)
PenneArrabiata = FoodItem("Penne Arrabiata", 14.99, "Pasta dish", 530, "Hot", "G", True)

# Seafood dishes
FishAndChips = FoodItem("Fish and Chips", 13.99, "Seafood", 560, "Low", "None", False)
ShrimpTacos = FoodItem("Shrimp Tacos", 17.99, "Seafood", 320, "Medium", "G", False)
GrilledSalmon = FoodItem("Grilled Salmon", 19.99, "Seafood", 480, "Low", "None", False)

# Pizza
Margherita = Pizza("L", "Margherita", 12.99, "Pizza", 510, "Low", "G, L", True)
Napoletana = Pizza("N", "napoletana", 14.99, "Pizza", 570, "Low", "G, L", False)
Pepperoni = Pizza("XL", "Pepperoni", 15.99, "Pizza", 620, "Medium", "G, L", False)
QuattroFormaggi = Pizza("N", "Quattro Formaggi", 14.99, 640, "Pizza", "Low", "G, L", True)

# Meat dishes
SteakFries = FoodItem("Steak Fries", 24.99, "Meat dish", 800, "Medium", "None", False)
BBQRibs = FoodItem("BBQ Ribs", 22.99, "Meat dish", 770, "Low", "None", False)
CajunChicken = FoodItem("Cajun Chicken", 18.99, "Meat dish", 690, "Hot", "G, L", False)

# Vegetarian dishes
FrenchFries = FoodItem("French Fries", 7.99, "Vege Dish", 350, "Low", "G", True)
GreekSalad = FoodItem("Greek Salad", 9.99, "Vege Dish", 250, "Low", "None", True)
CeasarSalad = FoodItem("Ceasar Salad", 9.99, "Vege Dish", 250, "Low", "None", True)
StuffedPeppers = FoodItem("Stuffed Peppers", 11.99, "Vege Dish", 300, "Hot", "L", True)

# Non-alcoholic drinks
CocaCola = Drink("Cola Cola", 4.99, 500, "Cold")
Fanta = Drink("Fanta", 4.99, 500, "Cold")
Sprite = Drink("Sprite", 4.99, 500, "Cold")
Lemonade = Drink("Lemonade", 5.99, 500, "Cold")
StillWater = Drink("Still water", 2.50, 500, "Cold")
SparklingWater = Drink("Sparkling water", 2.50, 500, "Cold")
Tea = Drink("Tea", 3.80, 330, "Hot")
Coffee = Drink("Coffee", 3.80, 330, "Hot")

# Alcoholic drinks
IPA = AlcoDrink(5.2, "IPA", 7.99, 500, "Cold")
Weizenbier = AlcoDrink(5.5, "Weizenbier", 7.80, 500, "Cold")
Pils = AlcoDrink(5.0, "Pils", 7.50, 500, "Cold")
Lager = AlcoDrink(4.9, "Lager", 6.90, 500, "Cold")
Cider = AlcoDrink(4.7, "Cider", 7.50, 500, "Cold")
LongDrink = AlcoDrink(5.1, "Long Drink", 8.80, 500, "Cold")
Wine = AlcoDrink(8.2, "Wine", 7.50, 300, "Normal")


# Test object and print
def food_test():
    all_items = [ChickenBurger, ClubSandwich, FalafelPita, BahnMi, SpaghettiBolognese, SpaghettiCarbonara, Lasagne, MacAndCheese, PenneArrabiata,
            FishAndChips, ShrimpTacos, GrilledSalmon, Margherita, Napoletana, Pepperoni, QuattroFormaggi, SteakFries, BBQRibs, CajunChicken, 
            FrenchFries, GreekSalad, CeasarSalad, StuffedPeppers]
    for item in all_items:
        print(item)

def drinks_test():
    all_drinks = [CocaCola, Fanta, Sprite, Lemonade, StillWater, SparklingWater, 
            Tea, Coffee, IPA, Weizenbier, Pils, Lager, LongDrink, Wine]
    for drink in all_drinks:
        print(drink)

# food_test()
# drinks_test()

m1 = Menu()
m1.food_items = [ChickenBurger, ClubSandwich, FalafelPita, BahnMi, SpaghettiBolognese, SpaghettiCarbonara, Lasagne, MacAndCheese, PenneArrabiata,
            FishAndChips, ShrimpTacos, GrilledSalmon, Margherita, Napoletana, Pepperoni, QuattroFormaggi, SteakFries, BBQRibs, CajunChicken, 
            FrenchFries, GreekSalad, CeasarSalad, StuffedPeppers]
m1.drinks = [CocaCola, Fanta, Sprite, Lemonade, StillWater, SparklingWater,Tea, Coffee, IPA, Weizenbier, Pils, Lager, LongDrink, Wine]
