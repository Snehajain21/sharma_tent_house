from datetime import datetime

from helpers import (
    read_positive_int
)

from storage import (
    save_items,
    save_history
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

    print("Tracking Type:",
          item["tracking_type"])

    print("Last Updated:",
          item["last_updated"])

    # LOW STOCK WARNING
    if item["total_quantity"] < 5:

        print("Warning: Low stock.")


# ADD ITEM QUANTITY
def add_item_quantity(item, items, history):

    quantity = read_positive_int(
        "Enter quantity to add: "
    )

    item["total_quantity"] += quantity

    # UPDATE LAST UPDATED
    item["last_updated"] = get_current_time()

    save_items(items)

    history.append(
        f"[{get_current_time()}] Added {quantity} chairs"
    )

    save_history(history)

    print("Quantity added successfully.")


# REMOVE ITEM QUANTITY
def remove_item_quantity(item, items, history):

    quantity = read_positive_int(
        "Enter quantity to remove: "
    )

    if quantity > item["total_quantity"]:

        print("Not enough quantity available.")
        return

    item["total_quantity"] -= quantity

    # UPDATE LAST UPDATED
    item["last_updated"] = get_current_time()

    save_items(items)

    history.append(
        f"[{get_current_time()}] Removed {quantity} chairs"
    )

    save_history(history)

    print("Quantity removed successfully.")


# UPDATE ITEM NAME
def update_item_name(item, items, history):

    new_name = input(
        "Enter new item name: "
    ).strip()

    if new_name == "":

        print("Item name cannot be empty.")
        return

    old_name = item["item_name"]

    item["item_name"] = new_name

    # UPDATE LAST UPDATED
    item["last_updated"] = get_current_time()

    save_items(items)

    history.append(
        f"[{get_current_time()}] Updated item name from {old_name} to {new_name}"
    )

    save_history(history)

    print("Item name updated successfully.")


# UPDATE RENTAL PRICE
def update_rental_price(item, items, history):

    new_price = read_positive_int(
        "Enter new rental price: "
    )

    old_price = item["rental_price"]

    item["rental_price"] = new_price

    # UPDATE LAST UPDATED
    item["last_updated"] = get_current_time()

    save_items(items)

    history.append(
        f"[{get_current_time()}] Updated rental price from {old_price} to {new_price}"
    )

    save_history(history)

    print("Rental price updated successfully.")


# VIEW HISTORY
def view_history(history):

    if len(history) == 0:

        print("No history available.")
        return

    print("\n========== INVENTORY HISTORY ==========")

    for record in history:

        print(record)