from datetime import datetime

from helpers import (
    read_positive_int
)

from storage import (
    save_items
)


# GET CURRENT TIME
def get_current_time():

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )


# VIEW ITEM DETAILS
def view_item_details(item):

    print("\n========== ITEM DETAILS ==========")

    print("Item ID:",
          item["item_id"])

    print("Item Name:",
          item["item_name"])

    print("Total Quantity:",
          item["total_quantity"])

    print("Rental Price:",
          item["rental_price"])

    print("Last Updated:",
          item["last_updated"])


# ADD NEW ITEM
def add_new_item(items):

    item_name = input(
        "Enter new item name: "
    ).strip()

    total_quantity = read_positive_int(
        "Enter item quantity: "
    )

    rental_price = read_positive_int(
        "Enter rental price: "
    )

    # FIND NEXT UNIQUE ITEM ID
    max_id = 100

    for item in items:

        current_id = int(
            item["item_id"][1:]
        )

        if current_id > max_id:

            max_id = current_id

    item_id = "I" + str(max_id + 1)

    new_item = {

        "item_id": item_id,

        "item_name": item_name,

        "total_quantity": total_quantity,

        "rental_price": rental_price,

        "last_updated": "Not updated yet"
    }

    items.append(new_item)

    save_items(items)

    print("New item added successfully.")


# DELETE ITEM
def delete_item(item, items):

    confirmation = input(
        f"Are you sure you want to delete '{item['item_name']}'? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":

        print("Delete operation cancelled.")
        return

    items.remove(item)

    save_items(items)

    print("Item deleted successfully.")


# ADD ITEM QUANTITY
def add_item_quantity(item, items):

    quantity = read_positive_int(
        "Enter quantity to add: "
    )

    item["total_quantity"] += quantity

    item["last_updated"] = get_current_time()

    save_items(items)

    print("Quantity added successfully.")


# REMOVE ITEM QUANTITY
def remove_item_quantity(item, items):

    quantity = read_positive_int(
        "Enter quantity to remove: "
    )

    if quantity > item["total_quantity"]:

        print("Not enough quantity available.")
        return

    item["total_quantity"] -= quantity

    item["last_updated"] = get_current_time()

    save_items(items)

    print("Quantity removed successfully.")


# UPDATE ITEM NAME
def update_item_name(item, items):

    new_name = input(
        "Enter new item name: "
    ).strip()

    if new_name == "":

        print("Item name cannot be empty.")
        return

    item["item_name"] = new_name

    item["last_updated"] = get_current_time()

    save_items(items)

    print("Item name updated successfully.")


# UPDATE RENTAL PRICE
def update_rental_price(item, items):

    new_price = read_positive_int(
        "Enter new rental price: "
    )

    item["rental_price"] = new_price

    item["last_updated"] = get_current_time()

    save_items(items)

    print("Rental price updated successfully.")