from storage import (
    load_items,
    load_history
)

from item import (
    view_item_details,
    add_item_quantity,
    remove_item_quantity,
    update_item_name,
    update_rental_price,
    view_history
)


# MAIN PROGRAM
def main():

    items = load_items()

    item = items[0]

    history = load_history()

    while True:

        print(
            "\n========== Sharma Tent House Inventory =========="
        )

        print("1. View Item Details")

        print("2. Add Item Quantity")

        print("3. Remove Item Quantity")

        print("4. Update Item Name")

        print("5. Update Rental Price")

        print("6. View Inventory History")

        print("7. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            view_item_details(item)

        elif choice == "2":

            add_item_quantity(
                item,
                items,
                history
            )

        elif choice == "3":

            remove_item_quantity(
                item,
                items,
                history
            )

        elif choice == "4":

            update_item_name(
                item,
                items,
                history
            )

        elif choice == "5":

            update_rental_price(
                item,
                items,
                history
            )

        elif choice == "6":

            view_history(history)

        elif choice == "7":

            print("Exiting program...")
            break

        else:

            print(
                "Invalid choice. Please select a valid menu option."
            )


# START PROGRAM
main()