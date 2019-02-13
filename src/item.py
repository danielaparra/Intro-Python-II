class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = name
    
    def on_take(self):
        print("{self.name} has been taken.")

    def on_drop(self):
        print("{self.name} has been dropped.")