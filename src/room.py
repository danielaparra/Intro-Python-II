# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def itemsInventory(self):
        return f"Items in room: {' ,'.join(self.items)}"

    def remove(self, item):
        self.items.remove(item)