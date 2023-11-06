class Item():
    def __init__(self, id, name, stock, price):
        self.id = id
        self.name = name
        self.stock_num = stock
        self.price = price

    def update_price(self,new_price):
        self.price = new_price

    def update_stock(self,new_stock):
        self.stock = new_stock