from storage import (
    load_items
)

from helpers import (
    search_item
)

from item import (
    view_item_details,
    add_new_item,
    delete_item,
    add_item_quantity,
    remove_item_quantity,
    update_item_name,
    update_rental_price,
    export_items_to_excel
)


# UPDATE EXISTING ITEM MENU
def update_existing_item(item, items):

    while True:

        print(
            f"\n========== Update {item['item_name']} =========="
        )

        print("1. View Item Details")

        print("2. Add Item Quantity")

        print("3. Remove Item Quantity")

        print("4. Update Item Name")

        print("5. Update Rental Price")

        print("6. Back to main Menu")

        choice = input(
            "\nEnter your choice: "
        )

        # VIEW DETAILS
        if choice == "1":

            view_item_details(item)

        # ADD QUANTITY
        elif choice == "2":

            add_item_quantity(
                item,
                items
            )

        # REMOVE QUANTITY
        elif choice == "3":

            remove_item_quantity(
                item,
                items
            )

        # UPDATE NAME
        elif choice == "4":

            update_item_name(
                item,
                items
            )

        # UPDATE RENTAL PRICE
        elif choice == "5":

            update_rental_price(
                item,
                items
            )

        # BACK
        elif choice == "6":

            break

        else:

            print("Invalid choice.")


# MAIN PROGRAM
def main():

    items = load_items()

    while True:

        print(
            "\n========== Sharma Tent House Inventory =========="
        )

        print("1. Add New Item")

        print("2. Update Existing Item")

        print("3. Delete Item")

        print("4. View All Items")

        print("5. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        # ADD NEW ITEM
        if choice == "1":

            add_new_item(items)

        # UPDATE EXISTING ITEM
        elif choice == "2":

            item = search_item(items)

            if item is not None:

                update_existing_item(
                    item,
                    items
                )

        # DELETE ITEM
        elif choice == "3":

            item = search_item(items)

            if item is not None:

                delete_item(
                    item,
                    items
                )

        # VIEW ALL ITEMS
        elif choice == "4":

            export_items_to_excel(items)

        # EXIT
        elif choice == "5":

            print("Exiting program...")
            break

        else:

            print(
                "Invalid choice. Please select a valid menu option."
            )


# START PROGRAM
if __name__ == "__main__":

    main()