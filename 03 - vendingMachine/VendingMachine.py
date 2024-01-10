# File        :   VendingMachine.py
# Version     :   1.0.0
# Description :   Vending Machine implementation
# Date:       :   Jan 09, 2023
# Author      :   Ricardo Acevedo-Avila (racevedoaa@gmail.com)
# License     :   Creative Commons CC0

import pprint


class VendingMachine:
    # Class variable, shared by all instances:
    machineType = "Vending Machine"
    machineVersion = "1.0"

    # Initialization:
    def __init__(self, name: str = "Default", products: list = None) -> None:

        print("Initializing ", self.machineType)

        # Machine name:
        self._name = name
        # List of available products:
        self._stock = {}
        # List of option -> product:
        self._productOptions = []
        # Current Selection:
        self._currentProduct = -1
        # Total items (units/products):
        self._totalItems = 0
        # Empty flag:
        self._empty = False

        # Verbosity output:
        self._verbose = False

        # Fill with default products:
        if not products:
            self.display("No products given, using default.")

            # Create default products:
            initProducts = [{"Product ID": "Soda-1", "Price": 2.5, "Units": 1},
                            {"Product ID": "Soda-2", "Price": 1.5, "Units": 1},
                            {"Product ID": "Soda-1", "Price": 2.5, "Units": 1}]

            # Fill machine with default products:
            self.fillMachine(initProducts)

    # Total products:
    def __len__(self):
        # Return the number of items currently in stock:
        totalItems = 0
        for k, v in self._stock.items():
            # Get current units:
            productUnits = v["Units"]
            totalItems += productUnits

        return totalItems

    # Set verbose:
    def setVerbose(self, verbose: bool) -> None:
        self._verbose = verbose
        print("Verbose set to: ", self._verbose)

    # Print to machine's display:
    def display(self, message: str) -> None:
        print(self._name + ": " + message)

    # Setup stock of products:
    def fillMachine(self, products: list) -> None:
        self.display("Filling machine stock with products...")

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
                self._stock.setdefault(productType, {"Price": productPrice, "Units": 0})
                # Add units to "entry":
                self._stock[productType]["Units"] += productUnits

                if self._verbose:
                    print("Product Added:", productType, "Price: ", productPrice, "Units:", productUnits)

            else:
                if self._verbose:
                    print("Product:", productType, " got no units, not added to stock.")

        self.display("Current Stock:")
        pp = pprint.PrettyPrinter(width=1)
        pp.pprint(self._stock)

        # Create options from stock:
        self.createOptions()

        # Get total products:
        self._totalItems = len(self)
        self.display("Total items available: " + str(self._totalItems))

    # Create options menu from stock:
    def createOptions(self) -> None:

        self.display("Creating options from stock products...")

        # Loop through the stock and assign each product an
        # option to be displayed in the menu:
        for i, k in enumerate(self._stock):
            self._productOptions.append(k)

    # Updates the stock:
    def updateStock(self, item: int) -> None:

        self.display("Updating stock...")

        # Get product name:
        productName = self._productOptions[item]
        # Get original quantity:
        pastUnits = self._stock[productName]["Units"]
        # Subtract item:
        self._stock[productName]["Units"] -= 1
        currentUnits = self._stock[productName]["Units"]

        self.display("Updated item: " + productName + " : " + str(pastUnits) + " -> " + str(currentUnits))

        # Get total products:
        self._totalItems = len(self)

        # Is the machine empty?
        if self._verbose:
            print("Total items: ", self._totalItems)
        if self._totalItems < 1:
            # Machine is empty:
            self._empty = True

    # Display menu:
    def displayMenu(self, extraOptions: list = None) -> None:

        print("* * ======{ Menu }====== * *")

        # Get total items:
        print(self.machineType, "currently has: ", self._totalItems, "item(s).")

        print("> Select an option from the available products: ")

        # Display options of available product:
        totalOptions = len(self._productOptions)
        for i in range(totalOptions):
            # Get product name:
            productName = self._productOptions[i]
            # Price:
            productPrice = self._stock[productName]["Price"]
            # Quantity:
            productQuantity = self._stock[productName]["Units"]

            # Build option string:
            optionString = " I: " + productName + "   P: " + str(productPrice) + " $   Q: " + str(productQuantity)
            # Show current option:
            print("[" + str(i) + "]", " ---> ", optionString)

        # Display extra options:
        if extraOptions:
            for currentTuple in extraOptions:
                # Get symbol
                extraOption = currentTuple[0]
                # Get description:
                optionInfo = currentTuple[1]

                # Show current option:
                print("[" + str(extraOption) + "]", " ---> ", optionInfo + "  ", end=" ")

        # Print new line:
        print("\n")

    # Processes item selection:
    def processSelection(self, item: int) -> bool:

        self._currentProduct = item
        self.display("Your selection: " + str(self._currentProduct))

        # Show product name, price and quantity:
        productName = self._productOptions[self._currentProduct]
        productPrice = self._stock[productName]["Price"]
        productQuantity = self._stock[productName]["Units"]

        self.display("Selected item: " + productName + " (x" + str(productQuantity) + ")")
        self.display("Price: " + str(productPrice))

        # Default flag value (no product is given):
        giveItem = False

        # Check at least one quantity of the item is available:
        if productQuantity >= 1:

            # Receive money from user:
            userMoney = float(input("Enter money: "))

            # Check if money is enough:
            moneyDifference = userMoney - productPrice

            # If difference >= epsilon, got enough money
            if moneyDifference >= 0:
                if self._verbose:
                    print("You entered: " + str(userMoney) + " $")
                # Compute change:
                moneyChange = moneyDifference
                giveItem = True

            # Else user is broke:
            else:
                self.display("You are broke. Come back when you have enough money.")
                moneyChange = userMoney

            # Give change:
            self.display("> Your change: " + str(moneyChange) + " $")

        # No quantities left from this item:
        else:
            self.display("No units left for this item. Please select another one.")

        return giveItem

    # Serves the item:
    def serveProduct(self, item: int):
        productName = self._productOptions[item]
        self.display("> Here's your product: " + productName)

    # Returns the list of options:
    @property
    def productOptions(self) -> list:
        # Read only attribute:
        return self._productOptions

    # Shuts down machine:
    def shutdownMachine(self) -> None:
        self.display("Bye!")

    # Displays machine info:
    def getMachineInfo(self) -> None:
        print("==== Machine Info: ==== ")
        print("Type: " + str(self.machineType))
        print("Name: " + str(self._name))
        print("Ver: " + str(self.machineVersion))
        print("Current Stock:")
        pp = pprint.PrettyPrinter(width=1)
        pp.pprint(self._stock)
