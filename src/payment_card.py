class PaymentCard:
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def eat_affordably(self):
        if (self.balance >= 2.6):
            self.balance -= 2.6
    
    def eat_heartily(self):
        if (self.balance >= 4.6):
            self.balance -= 4.6

    def add_money(self, amount):
        if (amount > 0):
            if (self.balance + amount > 150):
                self.balance = 150
            else:
                self.balance += amount

    def __str__(self):
        return "The card has a balance of " + str(self.balance) + " pounds"
