class Menu:
    # Constructor
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
  
    # String representation
    def __repr__(self):
        return '{} menu available from {} to {}'.format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price
  
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Representation string
    def __repr__(self):
        return "Address: {}".format(self.address)

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Create instance Class menu
brunch = Menu("Brunch", {
    'pancakes': 7.50, 
    'waffles': 9.00, 
    'burger': 11.00, 
    'home fries': 4.50, 
    'coffee': 1.50, 
    'espresso': 3.00, 
    'tea': 1.00, 
    'mimosa': 10.50, 
    'orange juice': 3.50
}, "11am", "4pm")

# Create instance Class menu
early_bird = Menu("Early Bird", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50, 'espresso': 3.00
}, "3pm", "6pm")

# Create instance Class menu
dinner = Menu("Dinner", {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,'coffee': 2.00, 'espresso': 3.00
}, "5pm", "11pm")

# Create instance Class menu
kid = Menu("Kid", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}, "11am", "9pm")

# Create instance Class menu for Take a' Arepa
arepas_menu = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}

# Create instance Class menu for Take a' Arepa
arepas_place = Franchise("189 Fitzgerald Avenue", [Menu("Take a' Arepa", arepas_menu, "10am", "8pm")])

# Define instances for class Franchise
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kid])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kid])

# Create instance for class Business
take_arepa = Business("Take a' Arepa", [flagship_store, new_installment, arepas_place])

# Time for testing available_menus
# time = "12pm" 
available_menus = take_arepa.franchises[0].available_menus("12pm")
for menu in available_menus:
    print(menu)
