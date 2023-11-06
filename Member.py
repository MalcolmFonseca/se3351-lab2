class Member:
    def __init__(self,firstName,lastName,id,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.id=id
        self.phone=phone 
    
    def update(self, firstName=None, lastName=None,ID=None, phone=None):
        if firstName != None:
            self.firstName = firstName
        if lastName != None:
            self.lastName = lastName
        if self.phone != None:
            self.phone = phone