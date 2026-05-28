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


# FIND MATCHING ITEMS
def find_matching_items(items, item_name):

    matching_items = []

    item_name = item_name.lower()

    for item in items:

        if (
            item_name
            in item["item_name"].lower()
        ):

            matching_items.append(item)

    return matching_items


# SEARCH AND SELECT ITEM
def search_item(items):

    item_name = input(
        "\nSearch item: "
    ).strip()

    matching_items = find_matching_items(
        items,
        item_name
    )

    # NO MATCH
    if len(matching_items) == 0:

        print("Item not found.")
        return None

    # SINGLE MATCH
    elif len(matching_items) == 1:

        return matching_items[0]

    # MULTIPLE MATCHES
    else:

        print("\nMultiple matching items found:")

        for index, item in enumerate(
            matching_items,
            start=1
        ):

            print(
                f"{index}. {item['item_name']}"
            )

        selected_number = read_positive_int(
            "Select item number: "
        )

        if (
            selected_number
            > len(matching_items)
        ):

            print("Invalid selection.")
            return None

        return matching_items[
            selected_number - 1
        ]