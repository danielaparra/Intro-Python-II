# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, room):
        self.roomCurrentlyIn = room
        self.items = []

    def move_n(self):
        if hasattr(self.roomCurrentlyIn, 'n_to'):
            newRoom = self.roomCurrentlyIn.n_to
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!\n")
    
    def move_s(self):
        if hasattr(self.roomCurrentlyIn, 's_to'):
            newRoom = self.roomCurrentlyIn.s_to
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!\n")

    def move_w(self):
        if hasattr(self.roomCurrentlyIn, 'w_to'):
            newRoom = self.roomCurrentlyIn.w_to
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!\n")
    
    def move_e(self):
        if hasattr(self.roomCurrentlyIn, 'e_to'):
            newRoom = self.roomCurrentlyIn.e_to
            self.roomCurrentlyIn = newRoom
        else:
            print("Can't go in that direction!\n")

    def get(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def inventory(self):
        if self.items == 0:
            return "No items in inventory."
        else: 
            return f"Items in inventory: {','.join(self.items)}"

    def i(self):
        if self.items == 0:
            return "No items in inventory."
        else: 
            return f"Items in inventory: {','.join(self.items)}"