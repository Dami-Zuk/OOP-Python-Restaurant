# Authors: Damian Zukowski, Ho Kim, Quang Anh Nguyen, Quan Nguyen

""" This file contains all the Staff - Waiters & Cooks """

Stations = ["garnish", "fry", "grill", "cold", "dessert"]
class Staff:
    def __init__(self, fname:str, lname:str, gender:str, age:int, salary:int, email: str = "QuangRestaurant@quang.fi", phone: str = "040 666 1337"):
        self._fname = fname
        self._lname = lname
        self.gender = gender
        self.age = age
        self.salary = salary
        self.contact = {
            "email": email,
            "phone-number": phone
        }

class Server(Staff):
    def serve_food(self):
        print(f'{self._fname} is serving you food')
    def clean_up(self):
        print(f'{self._fname} is cleaning your table')
    def taking_order(self):
        print(f'{self._fname} is noting down your order')

class Bartender(Staff):
    def making_drink(self):
        print(f'{self._fname} is preparing your drink...')

class Cook(Staff):
    def __init__(self, fname, lname, gender, age, salary, station):
        assert station in Stations, f"{station} station does not exist in {Stations}" #Checking if the station name is valid
        super().__init__(fname, lname, gender, age, salary)
        self.station = station
    def preparing_order(self):
         print(f'{self._fname} is making the order')
    def handling_order(self):
         print('The dish has been passed to the Headchef to check')

class HeadChef(Cook):
    def __init__(self, fname, lname, gender, age, salary):
        super().__init__(fname, lname, gender, age, salary, 'garnish')
    def receive_order(self):
        print(f'{self._fname} has received the order and assigning the cook')
    def checking_dish(self):
         print(f'{self._fname} has received the dish and checking it...')
    def serve(self):
         print('Ring!! The food is ready')

    def dropped_a_plate(self):
        print(f"{self._fname} {self._lname} dropped a plated, deducted into salary")
        self.salary -=20
        print(f"Salary has becomed {self.salary}")


class SousChef(Cook):
    def __init__(self, fname, lname, gender, age, salary):
        super().__init__(fname, lname, gender, age, salary, 'garnish')
    def garnish(self):
        print(f'{self._fname} is garnishing the dish')
    def taste_test(self):
        print(f'{self.fname} is taste-testing the dish...')

#testing:

def fronthouse_test(): #test the fronthouse staff (server and bartender)
    server1 = Server("Damian", "Zuski", "Female", 25, 1200, "zuski666@gmail.com", "046 123 4567")
    bartender_staff = Bartender("Quang", "Nguyen", "Male", 20, 1000, "vietkingkong@xoxo.com", "040 987 6543")
    Server.serve_food(server1)
    Server.taking_order(server1)
    Bartender.making_drink(bartender_staff)
 

def kitchen_test(): #every staff in the kitchen
    cook1 = Cook("Kim", "Ho", "Male", 33, 1300, "grill")
    headchef_staff = HeadChef("Peyman", "Mann", "Male", 40, 1250)
    souschef_staff = SousChef("Casper", "Michaelli", "Female", 39, 1100)
    HeadChef.receive_order(headchef_staff)
    Cook.preparing_order(cook1)
    SousChef.garnish(souschef_staff)

    headchef_staff.preparing_order()
    headchef_staff.dropped_a_plate()

'''print("Front house staff testings:")
fronthouse_test()
print("")
print("Front house test has completed!")
print("")

print("kitchen staff testings:")
kitchen_test()
print("")
print("kitchen staff test has completed!")'''
    
