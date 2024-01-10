# File        :   main.py
# Version     :   1.0.0
# Description :   Vending Machine instantiation
# Date:       :   Jan 09, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

from VendingMachine import VendingMachine


def getMenuOptions(machine: VendingMachine, extraOptions: list) -> dict:
    """
    Receives a VendingMachine instance and a list of extra
    options and returns a dict of 2 lists: one list with numerical
    products indices and another list with character options.
    Both lists store strings
    """
    # Create list of extra options:
    menuList = [options[0] for options in extraOptions]

    # Create list of options:
    productList = list(range(0, len(machine.productOptions)))
    # Int to string
    productList = [str(number) for number in productList]

    return {"Products": productList, "Menu": menuList}


# Create a new vending machine:
newMachine = VendingMachine(name="Dracula")

# Set verbosity:
newMachine.setVerbose(False)

# Set Additional options to be displayed in menu:
extraOptions = [("E", "Exit"), ("I", "Info")]

# Get lists of available menu options:
optionsDict = getMenuOptions(newMachine, extraOptions)
productOptions = optionsDict["Products"]
menuOptions = optionsDict["Menu"]

# Loop control:
runMachine = True

# Greet:
greetMessage = "Hello from " + newMachine.machineType + ". My name is: " + newMachine._name
newMachine.display(greetMessage)

while runMachine:

    # Display menu:
    newMachine.displayMenu(extraOptions)

    # Check if the machine is empty
    machineEmpty = newMachine._empty

    # If no empty, run the loop:
    if not machineEmpty:

        # Receive input from user:
        currentOption = input("Enter selection: ")

        # Check if numerical option:
        if currentOption in productOptions:

            # Convert to int:
            currentOption = int(currentOption)

            # Process product selection:
            giveItem = newMachine.processSelection(currentOption)

            # Has the product been dispatched?
            if giveItem:
                # Serve product:
                newMachine.serveProduct(currentOption)

                # Update stock:
                newMachine.updateStock(currentOption)

            # Ready for next costumer:
            newMachine.display("Have a nice day!")

        else:

            # To uppercase:
            currentOption = currentOption.upper()

            # Check if extra option:
            if currentOption in menuOptions:

                # Exit?
                if currentOption.upper() == "E":
                    # Say goodbye and exit:
                    newMachine.shutdownMachine()
                    runMachine = False

                else:

                    # Display info?
                    if currentOption.upper() == "I":
                        newMachine.getMachineInfo()
                    else:
                        newMachine.display("Invalid option, try again.")

            else:
                newMachine.display("Invalid option, try again.")

    else:
        # There are no items left:
        newMachine.display("Out of product. Come back later!")
        runMachine = False
