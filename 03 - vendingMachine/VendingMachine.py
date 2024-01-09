# File        :   VendingMachine.py
# Version     :   0.5.0
# Description :   Vending Machine implementation
# Date:       :   Jan 08, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

import pprint


class VendingMachine:
    # Class variable, shared by all instances:
    machineType = "Vending Machine"

    # Initialization:
    def __init__(self, name="Default", products=None) -> None:

        print("Initializing ", self.machineType)

        # Machine name:
        self.name = name
        # List of available products:
        self.stock = {}
        # List of option -> product:
        self.productOptions = []
        # Money entered:
        self.inputMoney = 0
        # Current Selection:
        self.currentProduct = -1
        # Change:
        self.currentChange = 0
        # Total items (units/products):
        self.totalItems = 0

        # Empty flag:
        self.empty = False

        # Fill with default products:
        if not products:
            print("Init>> No products given, using default.")

            # Create default products:
            initProducts = [{"Product ID": "Soda-1", "Price": 2.5, "Units": 1},
                            {"Product ID": "Soda-2", "Price": 1.5, "Units": 1},
                            {"Product ID": "Soda-1", "Price": 2.5, "Units": 1}]

            # Fill machine with default products:
            self.fillMachine(initProducts)

        # Execute vending machine FSM:
        self.machineFSM()

    # Total products:
    def __len__(self):
        # Return the number of items currently in stock:
        totalItems = 0
        for k, v in self.stock.items():
            # get current units:
            productUnits = v["Units"]
            totalItems += productUnits

        return totalItems

    # Setup stock of products:
    def fillMachine(self, products) -> None:
        print("Filling machine stock with products...")

        # products is the list of products, which are dictionaries entries
        # containing the key -> Product ID, the price, and the product quantities
        # let's add the products given to the machine's stock:
        for currentProduct in products:
            # Get product type:
            productType = currentProduct["Product ID"]
            # Check quantity before adding to stock:
            productUnits = currentProduct["Units"]

            if productUnits > 0:

                # Add to stock "entry: (key - default initialization)
                productPrice = currentProduct["Price"]
                self.stock.setdefault(productType, {"Price": productPrice, "Units": 0})
                # Add units to "entry":
                self.stock[productType]["Units"] += productUnits

                print("Product Added:", productType, "Price: ", productPrice, "Units:", productUnits)

            else:
                print("Product:", productType, " got no units, not added to stock.")

        print("Current Stock:")
        pp = pprint.PrettyPrinter(width=1)
        pp.pprint(self.stock)

        # Create options from stock:
        self.createOptions()

        # Get total products:
        self.totalItems = len(self)
        print("Total items available: ", self.totalItems)

        # Is the machine empty?
        if self.totalItems < 1:
            self.empty = True

    # Create options menu from stock:
    def createOptions(self) -> None:

        print("Creating options from stock products...")

        # Loop through the stock and assign each product an
        # option to be displayed in the menu:
        for i, k in enumerate(self.stock):
            self.productOptions.append(k)

    # Updates the stock:
    def updateStock(self, item) -> None:

        print("Updating stock...")

        # Get product name:
        productName = self.productOptions[item]
        # Get original quantity:
        pastUnits = self.stock[productName]["Units"]
        # Subtract item:
        self.stock[productName]["Units"] -= 1
        currentUnits = self.stock[productName]["Units"]

        print("Updated item: " + productName + " : " + str(pastUnits) + " -> " + str(currentUnits))

    # Display menu:
    def displayMenu(self) -> None:
        print("* * ======{ Menu }====== * *")

        # Get total items:
        print(self.machineType, "currently has: ", self.totalItems, "item(s).")

        print("> Select an option from the available products: ")

        # Display options of available product:
        totalOptions = len(self.productOptions)
        for i in range(totalOptions):
            # Get product name:
            productName = self.productOptions[i]
            # Price:
            productPrice = self.stock[productName]["Price"]
            # Quantity:
            productQuantity = self.stock[productName]["Units"]

            # Build option string:
            optionString = " I: " + productName + "   P: " + str(productPrice) + " $   Q: " + str(productQuantity)
            # Show current option
            print("[" + str(i) + "]", " ---> ", optionString)

    # Processes item selection:
    def processSelection(self, currentSelection) -> bool:

        self.currentProduct = currentSelection
        print("Your selection:", self.currentProduct)

        # Show product name, price and quantity:
        productName = self.productOptions[self.currentProduct]
        productPrice = self.stock[productName]["Price"]
        productQuantity = self.stock[productName]["Units"]

        print("Selected item: " + productName + " (x" + str(productQuantity) + ")")
        print("Price: " + str(productPrice))

        # Default flag value (no product is given):
        giveItem = False

        # Check at least one quantity of the item is available:
        if productQuantity > 1:

            # Receive money from user:
            userMoney = float(input("Enter money: "))

            # Check if money is enough:
            moneyDifference = userMoney - productPrice

            # If difference >= epsilon, got enough money
            if moneyDifference >= 0:
                print("You entered: " + str(userMoney) + " $")
                # Compute change:
                moneyChange = moneyDifference
                giveItem = True

            # Else user is broke:
            else:
                print("You are broke. Come back when you have enough money.")
                moneyChange = userMoney

            # Give change:
            print("> Your change: " + str(moneyChange) + " $")

        # No quantities left from this item:
        else:
            print("No units left for this item. Please select another one.")

        return giveItem

    # Serves the item:
    def serveProduct(self, item):
        productName = self.productOptions[item]
        print("> Here's your product: ", productName)

    # Default greeting:
    def displayGreeting(self) -> None:
        print("Hello from: ", self.name, "!")
        print("Type: ", self.machineType)

    # Executes the vending machine FSM:
    def machineFSM(self) -> None:

        # Greet:
        self.displayGreeting()

        # Display menu:
        self.displayMenu()

        # Check if the machine is empty
        if not self.empty:

            # Receive input from user:
            currentSelection = input("Enter item: ")
            currentSelection = int(currentSelection)

            giveItem = self.processSelection(currentSelection)

            # Has the product been dispatched?
            if giveItem:
                # Serve product:
                self.serveProduct(currentSelection)

                # Update stock:
                self.updateStock(currentSelection)

            # Ready for next costumer:
            print("Come back anytime!")

        else:
            print("Out of product. Come back later!")
