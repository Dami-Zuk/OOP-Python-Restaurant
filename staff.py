# Authors: Damian Zukowski, Ho Kim, Quang Anh Nguyen, Quan Nguyen

""" This file contains all the Staff - Waiters & Cooks """

Stations = ["garnish", "fry", "grill", "cold", "dessert"]
class Staff:
    def __init__(self, fname:str, lname:str, gender:str, age:int):
        self._fname = fname
        self._lname = lname
        self.gender = gender
        self.age = age


class Server(Staff):
    def __init__(self, fname, lname, gender, age):
        super().__init__(fname, lname, gender, age)
    def serve_food(self):
        print(f'{self._fname} is serving you food')
    def clean_up(self):
        print(f'{self._fname} is cleaning your table')
    def taking_order(self):
        print(f'{self._fname} is noting down your order')

class Bartender(Staff):
    def __init__(self, fname, lname, gender, age):
        super().__init__(fname, lname, gender, age)
    def making_drink(self):
        print(f'{self._fname} is preparing your drink...')

class Cook(Staff):
    def __init__(self, fname, lname, gender, age, station):
        assert station in Stations, f"{station} station does not exist in {Stations}"
        super().__init__(fname, lname, gender, age)
        self.station = station
    def preparing_order(self):
         print(f'{self._fname} is making the order')
    def handling_order(self):
         print('The dish has been passed to the Headchef to check')

class HeadChef(Cook):
    def __init__(self, fname, lname, gender, age):
        super().__init__(fname, lname, gender, age, 'garnish')
    def receive_order(self):
        print(f'{self._fname} has received the order and assigning the cook')
    def checking_dish(self):
         print(f'{self._fname} has received the dish and checking it...')
    def serve(self):
         print('Ring!! The food is ready')


class SousChef(Cook):
    def __init__(self, fname, lname, gender, age):
        super().__init__(fname, lname, gender, age, 'garnish')
    def garnish(self):
        print(f'{self._fname} is garnishing the dish')
    def taste_test(self):
        print(f'{self.fname} is taste-testing the dish...')

#testing:

def fronthouse_test(): #test the fronthouse staff (server and bartender)
    server1 = Server("Damian", "Zuski", "Female", 25)
    bartender_staff = Bartender("Quang", "Nguyen", "Male", 20 )
    Server.serve_food(server1)
    Server.taking_order(server1)
    Bartender.making_drink(bartender_staff)
 

def kitchen_test(): #every staff in the kitchen
    cook1 = Cook("Kim", "Ho", "Male", 33, "grill")
    headchef_staff = HeadChef("Peyman", "Mann", "Male", 40)
    souschef_staff = SousChef("Casper", "Michaelli", "Female", 39)
    HeadChef.receive_order(headchef_staff)
    Cook.preparing_order(cook1)
    SousChef.garnish(souschef_staff)

print("Front house staff testings:")
fronthouse_test()
print("")
print("Front house test has completed!")
print("")

print("kitchen staff testings:")
kitchen_test()
print("")
print("kitchen staff test has completed!")
    
