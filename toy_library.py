"""This script represents a toy library"""

# Define the toy library collection globally
toy_library = [
    {
        "toy": "Barbie Extra Fashion Doll with Afro-Puffs",
        "type": "Doll",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 24.75
    },
    {
        "toy": "Forbidden Island",
        "type": "Board Game",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 19.99
    },
    {
        "toy": "LEGO Minecraft The Axolotl House",
        "type": "Building Set",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 29.99
    }
]


# TODO: Define the checkout function
def checkout(toy_index, checkout_date, due_date):

    # Get the toy from the toy library
    toy = toy_library[toy_index]

    # Check if the toy is already checked out
    if toy["status"] == "Checked Out":
        # If not, print a message and return False
        print(f"Sorry, {toy['toy']} is already checked out.")
        return False
    # If it is, update status, checkout_date, due_date, and checkout_count
    else:
        toy["status"] = "Checked Out"
        toy["checkout_date"] = checkout_date
        toy["due_date"] = due_date
        toy["checkout_count"] += 1

    # Print a message 
    print(f"Checking out {toy['toy']}.")

    # Update the toy library (optional: already handled)
    toy_library[toy_index] = toy
    
    # Return true
    return True

# TODO: Define the return_toy function
def return_toy(toy_index):

    # Get the toy from the toy library
    toy = toy_library[toy_index]

    # Check if the toy is already available
    if toy["status"] == "Available":
        # If not, print a message and return False
        print(f"Sorry, {toy['toy']} is already available.")
        return False
    # If it is, update status, checkout_date, due_date
    else:
        toy["status"] = "Available"
        toy["checkout_date"] = ""
        toy["due_date"] = ""

    # Print a message 
    print(f"Returning {toy['toy']}.")

    # Update the toy library (optional: already handled)
    toy_library[toy_index] = toy
    
    # Return true
    return True

# TODO: Define the add_toy function
def add_toy(toy, toy_type="", status="Available", replacement_cost=0.0):

    toy_library.append({
        "toy": toy,
        "type": toy_type,
        "status": status,
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": replacement_cost
    })

# TODO: Define the remove_toy function
def remove_toy(toy_index):

    # Remove the toy from the toy library
    toy = toy_library.pop(toy_index)

    # Return the removed toy
    return toy


# TODO: Define the print library function
def print_library(status=None, view_details=False):

    if status is not None:
        toy_library_filtered = [(index, toy) for index, toy
                                in enumerate(toy_library)
                                if toy["status"] == status]
    else:
         toy_library_filtered = [(index, toy) for index, toy
                                in enumerate(toy_library)]

    # Print the toy library
    for item in toy_library_filtered:
        # Unpack the tuple
        index, toy = item
        # Print the toy index, name and status
        print(f"{index}: {toy['toy']}")
        print(f"Status: {toy['status']}")

        # Print the detailed information if view_details is True
        if view_details:
            print(f"Type: {toy['type']}")
            print(f"Checkout Count: {toy['checkout_count']}")
            print(f"Replacement Cost: {toy['replacement_cost']:.2f}")
            if toy['status'] == "Checked Out":
                print(f"Checkout Date: {toy['checkout_date']}")
                print(f"Due Date: {toy['due_date']}")
            print("-" * 40)

# TODO: Define a function to check if the user input is in the toy library
def check_if_index_in_library(index):

    if index.isdigit():
        index = int(index)
        if index < len(toy_library):
            return index
    print("Invalid index. Please try again.")
    return None

# Define the main function
if __name__ == "__main__":

    library_menu = {
        "1": "Checkout a Toy",
        "2": "Return a Toy",
        "3": "View Toy Library",
        "4": "View Detailed Toy Library",
        "5": "Add a Toy",
        "6": "Remove a Toy",
        "7": "Exit"
    }

    # Print the library menu
    print("Welcome to the Toy Library!")

    # TODO: Implement the main menu loop
