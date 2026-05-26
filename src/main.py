import json
import os

FILE_NAME = "item.json"



# LOAD ITEM DATA
if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "r") as file:

        item = json.load(file)

else:

    # Default single item structure
    item = {
        "item_id": "I101",
        "item_name": "Plastic Chair",
        "total_quantity": 0,
        "rental_price": 10,
        "tracking_type": "bulk_quantity"
    }


# MAIN PROGRAM LOOP
while True:

    print("\n--- Sharma Tent House Inventory ---")

    print("1. Add Chairs")
    print("2. View Item Details")
    print("3. Remove Chairs")
    print("4. Exit")

    choice = input("Enter your choice: ")


    # ADD CHAIRS
    if choice == "1":

        while True:

            quantity = input("Enter number of chairs to add: ")

            # if iput is empty
            if quantity == "":

                print("Quantity cannot be empty.")
                continue

            # if input is other then number
            if not quantity.isdigit():

                print("Please enter a valid positive number.")
                continue

            quantity = int(quantity)

            # if input is negative
            if quantity <= 0:

                print("Quantity must be greater than zero.")
                continue

            break

        # Update quantity
        item["total_quantity"] = item["total_quantity"] + quantity

        # Save updated data into JSON file
        with open(FILE_NAME, "w") as file:

            json.dump(item, file, indent=4)

        print("Chairs added successfully.")
        print("Updated Quantity:", item["total_quantity"])

    # VIEW ITEM DETAILS
    elif choice == "2":

        print("\n--- Item Details ---")

        print("Item ID:", item["item_id"])
        print("Item Name:", item["item_name"])
        print("Total Quantity:", item["total_quantity"])
        print("Rental Price:", item["rental_price"])
        print("Tracking Type:", item["tracking_type"])

    # REMOVE CHAIRS
    elif choice == "3":

        while True:

            quantity = input("Enter number of chairs to remove: ")

            # if input is empty 
            if quantity == "":

                print("Quantity cannot be empty.")
                continue

            # if input is not number
            if not quantity.isdigit():

                print("Please enter a valid positive number.")
                continue

            quantity = int(quantity)

            # if input is negative
            if quantity <= 0:

                print("Quantity must be greater than zero.")
                continue

            break

        # removing more quantites then currently available
        if quantity > item["total_quantity"]:

            print("Not enough chairs available.")

        else:

            item["total_quantity"] = item["total_quantity"] - quantity

            # Save updated quantity into JSON file
            with open(FILE_NAME, "w") as file:

                json.dump(item, file, indent=4)

            print("Chairs removed successfully.")
            print("Remaining Quantity:", item["total_quantity"])

    # EXIT PROGRAM
    elif choice == "4":

        print("Exiting program...")
        break

    # INVALID MENU INPUT
    else:

        print("Invalid choice. Please select a valid menu option.")