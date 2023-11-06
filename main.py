import Member

members_list = []
transactions_list = []

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
            pass
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
    pass

main_menu()