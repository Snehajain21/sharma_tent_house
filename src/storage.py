import json
import os

FILE_NAME = "items.json"
BOOKINGS_FILE = "bookings.json"


# LOAD ITEMS
def load_items():

    # CHECK IF FILE EXISTS
    if os.path.exists(FILE_NAME):

        # OPEN FILE IN READ MODE
        with open(FILE_NAME, "r") as file:

            # LOAD JSON DATA
            return json.load(file)

    # DEFAULT ITEMS
    return [

        {
            "item_id": "I101",

            "item_name": "Plastic Chair",

            "total_quantity": 100,

            "rental_price": 10,

            "last_updated": "Not updated yet"
        },

        {
            "item_id": "I102",

            "item_name": "Table",

            "total_quantity": 20,

            "rental_price": 50,

            "last_updated": "Not updated yet"
        },

        {
            "item_id": "I103",

            "item_name": "Gas Burner",

            "total_quantity": 5,

            "rental_price": 100,

            "last_updated": "Not updated yet"
        }
    ]


# SAVE ITEMS
def save_items(items):

    # OPEN FILE IN WRITE MODE
    with open(FILE_NAME, "w") as file:

        # SAVE ITEMS INTO JSON FILE
        json.dump(items, file, indent=4)


# LOAD BOOKINGS
def load_bookings():

    if os.path.exists(BOOKINGS_FILE):

        with open(
            BOOKINGS_FILE,
            "r"
        ) as file:

            return json.load(file)

    return []


# SAVE BOOKINGS
def save_bookings(bookings):

    with open(
        BOOKINGS_FILE,
        "w"
    ) as file:

        json.dump(
            bookings,
            file,
            indent=4
        )