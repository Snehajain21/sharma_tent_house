import json
import os

FILE_NAME = "items.json"
HISTORY_FILE = "history.json"


# LOAD ITEMS
def load_items():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            return json.load(file)

    return [
        {
          "item_id": "I101",
          "item_name": "Plastic Chair",
          "total_quantity": 0,
          "rental_price": 10,
          "tracking_type": "bulk_quantity",
          "low_stock_limit": 5,
          "last_updated": "Not updated yet"
    }
    ]


# SAVE ITEMS
def save_items(items):

    with open(FILE_NAME, "w") as file:

        json.dump(items, file, indent=4)


# LOAD HISTORY
def load_history():

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as file:

            return json.load(file)

    return []


# SAVE HISTORY
def save_history(history):

    with open(HISTORY_FILE, "w") as file:

        json.dump(history, file, indent=4)