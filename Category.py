class Category:
    def __init__(self,name):
        self.name=name
        self.items={}
    def add(self,item):
        self.items[item.id]=item
    def remove(self,itemID):
        if itemID in self.items:
            del self.items[itemID]