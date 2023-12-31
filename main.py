import Member, Transaction, Item, Inventory
import random

temp_member = Member.Member("Malcolm","Fonseca",0,543543)
temp = Transaction.Transaction(0,temp_member)
temp.add_item(Item.Item(0,'tempitem',1,50))
temp2 = Transaction.Transaction(1,temp_member)
temp2.add_item(Item.Item(0,'tempitem2',1,50))
temp2.add_item(Item.Item(0,'tempitem3',1,50))

MainInventory = Inventory.Inventory()
items_list = []
members_list = [temp_member]
pending_transactions_list = [temp, temp2]
processed_transactions_list = []

def main_menu():
    print("""Welcome to the Retail Store Management Program!
          1. Member Management
          2. Item Management
          3. Inventory Viewing
          4. Transaction Processing
          5. Exit
          Enter choice: """)
    
    choice = int(input())
    if 0<choice<6:
        #member management
        if choice == 1:
            member_management()
        #item management
        elif choice == 2:
            item_management()
        #inventory viewing
        elif choice == 3:
            inventory_viewing()
        #transaction processing
        elif choice == 4:
            transaction_processing()
        #end
        elif choice == 5:
            print("Goodbye!")
            pass
    else:
        print("Invalid Choice!")
        main_menu()
        

def member_management():
    print("""Member Management
          1. Add Member
          2. Update Member
          3. View Purchase History
          4. View Current Members
          5. Return to Main Menu
          Enter choice: """)
    
    choice = int(input())
    if 0<choice<6:

        #add member
        if choice == 1:
            print("Add Member\nEnter First Name: ")
            first = input()
            print("Enter Last Name: ")
            last = input()
            print("Enter Phone Number: ")
            phone = input()
            new_member = Member.Member(first,last,len(members_list),phone)
            members_list.append(new_member)
            print("Member Added")
            
            member_management()
        #update member
        elif choice == 2:
            print("Update Member\nEnter Member Id: ")
            id = int(input())
            #check if member exists
            exists = False
            for member in members_list:
                if member.id == id:
                    exists = True

            if exists:
                print("Member Found")
            else:
                print("Member does not exist")
                member_management()
                return

            print("Enter First Name: ")
            first = input()
            print("Enter Last Name: ")
            last = input()
            print("Enter Phone Number: ")
            phone = input()

            member_management()
        #view purchase history
        elif choice == 3:
            print("Purchase History")
            for transaction in processed_transactions_list:
                print(transaction.str())
            member_management()

        #view members
        elif choice == 4:
            for member in members_list:
                print(member.str())
            member_management()

        elif choice == 5:
            main_menu()
    else:
        print("Invalid Choice!")
        member_management()

def item_management():
    print("""Item Management
          1. Add Item
          2. Update Price
          3. Update Stock
          4. Return to Main Menu4
          Enter choice: """)

    choice=input()
    if choice.isnumeric():
        choice = int(choice)
        if 0<choice<6:
            if choice ==1:

                name= input("Enter item name: ")
                stock=int(input("Enter Stock: "))
                price=float(input("Enter Price: "))
                item=Item.Item(len(items_list),name,stock,price)
                items_list.append(item)
                print(item.str())
                item_management()
            elif choice == 2:
                ID=int(input("Enter ID number: "))
                price=float(input("Enter new price: "))
                tempPrice=items_list[ID].price
                items_list[ID].update_price(price)
                print(f"Price was updated from ${tempPrice} to ${items_list[ID].price}\n")
                item_management()
            elif choice == 3:
                ID=int(input("Enter ID number: "))
                stock=int(input("Enter new Stock: "))
                tempStock=items_list[ID].stock_num
                items_list[ID].update_stock(stock)
                print(f"Stock was updated from {tempStock} to {items_list[ID].stock_num}\n")
                item_management()
            elif choice == 4:
                main_menu()
        else:
            item_management()
    else:
        item_management()

def inventory_viewing():
    print("""Inventory Management
          1. Add Item
          2. Remove Item
          3. Display Inventory
          4. Return to Main Menu
          Enter choice: """)

    choice=input()
    if choice.isnumeric():
        choice = int(choice)
        if 0<choice<5:
            if len(items_list)>0:

                if choice==1:
                    ID=int(input(f"Enter ID(0-{len(items_list)-1}): "))
                    MainInventory.add_item(items_list[ID])
                    print("Item Added\n")
                    inventory_viewing()
                elif choice ==2:
                    ID=int(input(f"Enter ID to remove(0-{len(items_list)-1}): "))
                    MainInventory.remove_item(items_list[ID].id)
                    print("Item removed")
                    inventory_viewing()
                elif choice == 3:
                    if len(MainInventory.items)==0:
                        print("Inventroy Empty")
                    else:
                        for i in MainInventory.items:
                            print(i)
                    inventory_viewing()
            else:
                print("Add Items before accessing inventory\n")
                main_menu()

        else:
            inventory_viewing()
    else:
        inventory_viewing()

def transaction_processing():
    print("""Transaction Processing
          1. Add Transaction
          2. Remove Transaction
          3. View Pending Transactions
          4. Process Transaction
          5. Return to Main Menu
          Enter choice: """)
    
    choice = int(input())
    if 0<choice<6:
        #add transaction
        if choice == 1:
            print("Add Transaction\nEnter Member ID: ")
            id = int(input())

            #find member for transaction
            add_member = None
            for member in members_list:
                if member.id == id:
                    add_member = member

            new_transaction = Transaction.Transaction(random.randint(0,1000), add_member)

            #add items to transaction
            print("Number of Items to be Added: ")
            num = int(input())
            for i in range(0,num):
                #check if item exists
                exists = False
                while(exists == False):
                    print(f"Enter Item #{i} ID: ")
                    id = int(input())
                    for item in items_list:
                        if item.id == id:
                            new_transaction.add_item(item)
                            exists = True

            pending_transactions_list.append(new_transaction)
            print("Transaction Added")

            transaction_processing()
        #remove transaction
        elif choice == 2:
            print("Remove Transaction\nEnter Transaction ID: ")
            id = int(input())
            for i,transaction in enumerate(pending_transactions_list):
                if transaction.id == id:
                    pending_transactions_list.pop(i)
            print("Transaction Removed")

            transaction_processing()
        #view pending transactions
        elif choice == 3:
            print("Pending Transactions:")

            for transaction in pending_transactions_list:
                print(transaction.str())

            transaction_processing()
        #process transaction
        elif choice == 4:
            print("Process Transaction\nEnter Transaction ID: ")
            id = int(input())
            for i,transaction in enumerate(pending_transactions_list):
                if transaction.id == id:
                    processed_transactions_list.append(transaction)
                    pending_transactions_list.pop(i)
            print("Transaction Processed")

            transaction_processing()
        elif choice == 5:
            main_menu()
    else:
        print("Invalid Choice!")
        transaction_processing()


#display inital menu
main_menu()