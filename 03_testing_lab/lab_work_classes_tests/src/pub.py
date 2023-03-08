class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def count_drinks(self):
        return len(self.drinks)
    
    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def add_to_till(self, drink):
        self.till += drink.price

    def sell_drink(self, customer, drink):
        self.remove_drink(drink)
        self.add_to_till(drink)
        customer.reduce_wallet(drink.price)
        customer.add_drink(drink)