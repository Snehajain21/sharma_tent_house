# COMMON VALIDATION FUNCTION
def read_positive_int(prompt):

    while True:

        value = input(prompt).strip()

        if value == "":

            print("Input cannot be empty.")
            continue

        if not value.isdigit():

            print("Please enter a valid positive number.")
            continue

        value = int(value)

        if value <= 0:

            print("Value must be greater than zero.")
            continue

        return value


# SHOW AVAILABLE ITEMS
def show_available_items(items):

    print("\nAvailable Items:")

    for item in items:

        print("-", item["item_name"])


# FIND ITEM BY NAME
def find_item_by_name(items, item_name):

    item_name = item_name.lower()

    for item in items:

        # PARTIAL MATCH SEARCH
        if (
            item_name
            in item["item_name"].lower()
        ):

            return item

    return None