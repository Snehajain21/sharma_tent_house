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

    print("1. Add Chairs Quantity")
    print("2. View Item Details")
    print("3. Remove Chairs Quantity")
    print("4. Update Item Name")
    print("5. Update Rental Price")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # ADD CHAIRS
    if choice == "1":

        while True:

            quantity = input("Enter number of chairs to add: ")

            # Empty input validation
            if quantity == "":

                print("Quantity cannot be empty.")
                continue

            # Numeric validation
            if not quantity.isdigit():

                print("Please enter a valid positive number.")
                continue

            quantity = int(quantity)

            # Negative validation
            if quantity <= 0:

                print("Quantity must be greater than zero.")
                continue

            break

        # Update quantity
        item["total_quantity"] = (
            item["total_quantity"] + quantity
        )

        # Save updated data
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

            quantity = input(
                "Enter number of chairs to remove: "
            )

            # Empty input validation
            if quantity == "":

                print("Quantity cannot be empty.")
                continue

            # Numeric validation
            if not quantity.isdigit():

                print("Please enter a valid positive number.")
                continue

            quantity = int(quantity)

            # Negative validation
            if quantity <= 0:

                print("Quantity must be greater than zero.")
                continue

            break

        # Prevent over-removal
        if quantity > item["total_quantity"]:

            print("Not enough chairs available.")

        else:

            item["total_quantity"] = (
                item["total_quantity"] - quantity
            )

            # Save updated data
            with open(FILE_NAME, "w") as file:

                json.dump(item, file, indent=4)

            print("Chairs removed successfully.")

            print(
                "Remaining Quantity:",
                item["total_quantity"]
            )


    # UPDATE ITEM NAME
    elif choice == "4":

        new_name = input("Enter new item name: ")

        # Empty name validation
        if new_name == "":

            print("Item name cannot be empty.")

        else:

            item["item_name"] = new_name

            # Save updated data
            with open(FILE_NAME, "w") as file:

                json.dump(item, file, indent=4)

            print("Item name updated successfully.")


    # UPDATE RENTAL PRICE
    elif choice == "5":

        while True:

            new_price = input(
                "Enter new rental price: "
            )

            # Empty input validation
            if new_price == "":

                print("Rental price cannot be empty.")
                continue

            # Numeric validation
            if not new_price.isdigit():

                print("Please enter a valid positive number.")
                continue

            new_price = int(new_price)

            # Negative validation
            if new_price <= 0:

                print(
                    "Rental price must be greater than zero."
                )

                continue

            break

        item["rental_price"] = new_price

        # Save updated data
        with open(FILE_NAME, "w") as file:

            json.dump(item, file, indent=4)

        print("Rental price updated successfully.")


    # EXIT PROGRAM
    elif choice == "6":

        print("Exiting program...")
        break


    # INVALID MENU OPTION
    else:

        print(
            "Invalid choice. Please select a valid menu option."
        )