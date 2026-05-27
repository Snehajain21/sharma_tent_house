from storage import (
    load_items
)

from helpers import (
    find_item_by_name,
    show_available_items
)

from item import (
    view_item_details,
    add_new_item,
    delete_item,
    add_item_quantity,
    remove_item_quantity,
    update_item_name,
    update_rental_price
)


# MAIN PROGRAM
def main():

    items = load_items()

    while True:

        print(
            "\n========== Sharma Tent House Inventory =========="
        )

        print("1. View Item Details")

        print("2. Add New Item")

        print("3. Delete Item")

        print("4. Add Item Quantity")

        print("5. Remove Item Quantity")

        print("6. Update Item Name")

        print("7. Update Rental Price")

        print("8. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        # ADD NEW ITEM
        if choice == "2":

            add_new_item(items)

            continue

        # OPERATIONS REQUIRING ITEM SEARCH
        if choice in ["1", "3", "4", "5", "6", "7"]:

            # SHOW AVAILABLE ITEMS
            show_available_items(items)

            item_name = input(
                "\nEnter item name: "
            ).strip()

            item = find_item_by_name(
                items,
                item_name
            )

            if item is None:

                print("Item not found.")
                continue

        # VIEW ITEM
        if choice == "1":

            view_item_details(item)

        # DELETE ITEM
        elif choice == "3":

            delete_item(
                item,
                items
            )

        # ADD QUANTITY
        elif choice == "4":

            add_item_quantity(
                item,
                items
            )

        # REMOVE QUANTITY
        elif choice == "5":

            remove_item_quantity(
                item,
                items
            )

        # UPDATE NAME
        elif choice == "6":

            update_item_name(
                item,
                items
            )

        # UPDATE PRICE
        elif choice == "7":

            update_rental_price(
                item,
                items
            )

        # EXIT
        elif choice == "8":

            print("Exiting program...")
            break

        else:

            print(
                "Invalid choice. Please select a valid menu option."
            )


# START PROGRAM
if __name__ == "__main__":

    main()