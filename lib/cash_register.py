#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0
        self.last_quantity = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.last_quantity = quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100.0)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction
            for _ in range(self.last_quantity):
                if self.items:
                    self.items.pop()
            self.last_transaction = 0.0
        else:
            self.total = 0.0
