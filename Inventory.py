class Inventory():
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,itemid):
        #find item id and remove it from list
        for i,item in enumerate(self.items):
            if item.id == itemid:
                self.items.pop(i)

    def search_item(self,search_params):
        #make empty array to add matches
        match_list = []

        #find items with input in their name
        for item in self.items:
            if search_params.lower() in item.name.lower():
                match_list.append(item)

        return match_list

    def list_category(self,category):
        pass