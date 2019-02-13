# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.roomCurrentlyIn = room
        self.items = []

    def get(self, item):
        self.items.append(item)