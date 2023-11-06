import Member, Transaction, Item

members_list = []
next_transaction_id = 0
pending_transactions_list = []
temp_member = Member.Member("Malcolm","Fonseca",0,543543)
temp = Transaction.Transaction(0,temp_member)
temp.add_item(Item.Item(0,'tempitem',1,50))
temp2 = Transaction.Transaction(1,temp_member)
temp2.add_item(Item.Item(0,'tempitem2',1,50))
temp2.add_item(Item.Item(0,'tempitem3',1,50))
processed_transactions_list = [temp, temp2]

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
            main_menu()

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
    pass

def inventory_viewing():
    pass

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

            new_transaction = Transaction.Transaction(next_transaction_id, add_member)
            next_transaction_id += 1

            #add items to transaction
            print("Number of Items to be Added: ")
            num = int(input())
            new_items = []
            for i in range(0,num):
                print(f"Enter Item #{i} ID: ")
                

            pending_transactions_list.append()
            print("Transaction Added")

            transaction_processing()
        #remove transaction
        elif choice == 2:
            transaction_processing()
        #view pending transactions
        elif choice == 3:
            transaction_processing()
        #process transaction
        elif choice == 4:
            transaction_processing()
        elif choice == 5:
            main_menu()
    else:
        print("Invalid Choice!")
        transaction_processing()


#display inital menu
main_menu()