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

