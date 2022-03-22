class Book:
    listOrders = []

    def __init__(self, name):
        self.name = name

    def insert_buy(self, qty, price):
        Book.listOrders.append(Order(self.name, "BUY", qty, price))
        Book.listOrders.sort(key=lambda x: x.price, reverse=True)
        printLog(self.name)

    def insert_sell(self, qty, price):
        Book.listOrders.append(Order(self.name, "SELL", qty, price))
        Book.listOrders.sort(key=lambda x: x.price, reverse=True)
        printLog(self.name)

class Order:
    id = 0

    def __init__(self, bookName, type, qty, price):
        Order.id += 1
        self.id = Order.id
        self.bookName = bookName
        self.type = type
        self.qty = qty
        self.price = price
        print("------------------------")
        print(f"-- Insert {self.type} {self.qty}@{self.price} id={self.id} on {self.bookName} Book")
    
    def get_price(self):
        return self.price

    def __str__(self):
        return f"        {self.type} {self.qty}@{self.price} id={self.id}"

def printLog(bookName):
    for order in Book.listOrders:
        if order.bookName == bookName:
            print(order)
