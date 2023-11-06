class Transaction():
    def __init__(self,member):
        self.member = member
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, itemid):
        #find item id and remove it from list
        for i,item in enumerate(self.items):
            if item.id == itemid:
                self.items.pop(i)

    def calc_total(self):
        price = 0
        
        for item in self.items:
            price += item.price

        return price