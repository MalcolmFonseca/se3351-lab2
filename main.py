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
    pass

def item_management():
    pass

def inventory_viewing():
    pass

def transaction_processing():
    pass

main_menu()