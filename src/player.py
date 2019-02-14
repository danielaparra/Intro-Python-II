# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, room):
        self.roomCurrentlyIn = room
        self.items = []

    def move_n(self):
        newRoom = self.roomCurrentlyIn.n_to
        if newRoom != None:
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!")
    
    def move_s(self):
        newRoom = self.roomCurrentlyIn.s_to
        if newRoom != None:
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!")

    def move_w(self):
        newRoom = self.roomCurrentlyIn.w_to
        if newRoom != None:
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!")
    
    def move_e(self):
        newRoom = self.roomCurrentlyIn.e_to
        if newRoom != None:
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!")

    def get(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def inventory(self):
        pass