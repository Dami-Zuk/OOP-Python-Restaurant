# Authors: Damian Zukowski, Ho Kim, Quang Anh Nguyen, Quan Nguyen

""" This file contains all the Staff - Waiters & Cooks """


class Staff:
    def __init__(self, fname, lname):
        self._fname = fname
        self._lname = lname


class Waiter(Staff):
    def __init__(self):
        super().__init__()


class Cook(Staff):
    def __init__(self):
        super().__init__()


class HeadChef(Cook):
    def __init__(self):
        super().__init__()


class SousChef(Cook):
    def __init__(self):
        super().__init__()


