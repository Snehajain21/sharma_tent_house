chair_quantity = 0

while True:

    print("\n--- Sharma Tent House Chair Inventory ---")
    print("1. Add Chairs")
    print("2. View Chair Quantity")
    print("3. Remove Chairs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        quantity = int(input("Enter number of chairs to add: "))

        chair_quantity = chair_quantity + quantity

        print("Chairs added successfully.")
        print("Total Chairs:", chair_quantity)

    elif choice == "2":

        print("Current Chair Quantity:", chair_quantity)

    elif choice == "3":

        quantity = int(input("Enter number of chairs to remove: "))

        if quantity > chair_quantity:

            print("Not enough chairs available.")

        else:

            chair_quantity = chair_quantity - quantity

            print("Chairs removed successfully.")
            print("Remaining Chairs:", chair_quantity)

    elif choice == "4":

        print("Exiting program...")
        break

    else:

        print("Invalid choice.")