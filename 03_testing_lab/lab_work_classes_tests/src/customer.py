class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks = []

    def add_drink(self, drink_to_buy):
        self.drinks.append(drink_to_buy)

    def count_drinks(self):
        return len(self.drinks)
    
    def count_wallet(self):
        return self.wallet
    
    def reduce_wallet(self, amount):
        self.wallet -= amount