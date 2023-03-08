class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.drinks = []
        self.age = age

    def add_drink(self, drink_to_buy):
        self.drinks.append(drink_to_buy)

    def count_drinks(self):
        return len(self.drinks)
    
    def count_wallet(self):
        return self.wallet
    
    def reduce_wallet(self, amount):
        self.wallet -= amount

    def check_customer_age(self):
        return self.age