import uuid

class Cart:
    __CART_FILE = "cart.csv"
    __TRANSACTION_FILE = "transaction.csv"
    def __init__(self, userID, taxRate):
        self.__id = uuid.uuid4()
        self.__basket = {}
        self.__subtotal = 0.0
        self.__total = 0.0
        self.__taxRate = taxRate
        self.__taxAmount = 0.0
        self.__itemsInBasket = 0
        self.__userID = userID

    def __str__(self):
        return "This cart with ID " + str(self.__id) + " has " + str(self.__itemsInBasket) \
               + " items in its basket for a subtotal of $" + str(self.__subtotal) + " and total of $" \
               + str(self.__total) + "(" + str(format(self.__taxRate, '.2%')) + " tax rate)"

    def getID(self):
        """Returns the id of self"""
        return self.__id

    def getBasket(self):
        """Returns the basket list of self"""
        return self.__basket

    def getSubtotal(self):
        """Returns the subtotal amount of self"""
        return self.__subtotal

    def getTotal(self):
        """Returns the total amount of self"""
        return self.__total

    def getTaxAmount(self):
        """Returns the tax amount of self"""
        return self.__taxAmount

    def getTaxRate(self):
        """Returns the tax rate of self"""
        return self.__taxRate

    def showBasketList(self):
        """Prints the basket list of self in a human readable format"""

        print("----------------------------------------")
        print("-------------Current Basket-------------")
        # Print Headers
        print("ID - NAME - QTY")

        for key in self.__basket:
            print(str(key + 1) + " - " + str(self.__basket[key]['name']) + " - " + str(self.__basket[key]['qty']))

        print("--------------- " + str(self.__itemsInBasket) + " Items ---------------")
        print("----------------------------------------")
        print()

    def setTaxRate(self, taxRate):
        """Sets the tax rate of self"""
        # Check that submitted param is a float
        try:
            # Check that Tax rate is a positive number
            if taxRate > 0.0:
                self.__taxRate = float(taxRate)
            else:
                print("Tax rate must be greater than or equal to 0.00. Defaulting to 0.00")
        except ValueError:
            print("Tax rate must be in a float. Defaulting to 0.00")
        except Exception as err:
            print(err)

    def addItem(self, productID, qty, productDetails, inventory):
        """Adds an item to self's basket list"""

        # Check that productID is an integer, if not return False
        try:
            productID = int(productID)
        except ValueError:
            print("Item not found. Product ID is not a valid product id.")
            return False

        except Exception as err:
            print(err)
            return False

        # Check that the productID is not larger than the length of the inventory, if it is return False
        if(productID > len(inventory)):
            print("Item not found. Product ID is beyond the inventory list.")
            return False

        # Check if product with key `productID` is in the dictionary
        if productID not in self.__basket:
            # Convert productDetails list to a dictionary with mapped keys
            productDictionary = self.__mapProductListToDictionary(productDetails)

            # append the quantity to add
            productDictionary["qty"] = qty

            # Append to __basket dictionary
            self.__basket[productID] = productDictionary
        else:
            # Update the qty
            self.__basket[productID]['qty'] = self.__basket[productID]['qty'] + qty

        # Calculate and Update the Subtotal
        self.__calculateSubtotal()

        # Calculate and Update the Total
        self.__calculateTotal()

        # Calculate and Update the Tax Amount
        self.__calculateTaxAmount()

        # Calculate the amount of Items in the Basket
        self.__calculateItemsInBasket()

    def removeItem(self, productID, qty):
        """Remove an item from the basket list of self"""
        # Check if product with key `productID` is in the dictionary
        if productID in self.__basket:
            if(qty > self.__basket[productID]['qty']):
                print()
                print("*************** WARNING ****************")
                print("\n", end="")
                print("Quantity for removal exceeds amount in basket")
                print("\n", end="")
                print("*************** WARNING ****************")
                print()
            else:
                # Update the qty
                self.__basket[productID]['qty'] = self.__basket[productID]['qty'] - qty
        else:
            print()
            print("*************** WARNING ****************")
            print("\n", end="")
            print("Item \"" + productID + "\" not in basket")
            print("\n", end="")
            print("*************** WARNING ****************")
            print()

        # Calculate and Update the Subtotal
        self.__calculateSubtotal()

        # Calculate and Update the Total
        self.__calculateTotal()

        # Calculate and Update the Tax Amount
        self.__calculateTaxAmount()

        # Calculate the amount of Items in the Basket
        self.__calculateItemsInBasket()

    def checkout(self):

        # Open the file in append mode
        fd = open(self.__CART_FILE, 'a')

        # Iterate over the self.__basket dictionary
        for k,v in self.__basket.items():
            # Add each Cart item to the Cart file using the self.__id and self.__userID unique keys
            # CSV Format: CARTID, USERID, PRODUCT NAME, PRICE, QTY
            fd.write(str(self.__id) + "," + self.__userID + "," + v['name'] + "," + str(v['price']) + "," + str(v['qty']) + "\n")
        # Close cart file
        fd.close()

        # In order to house the details of the transaction, let's save that in a transaction file
        # Open the file in append mode
        transFile = open(self.__TRANSACTION_FILE, 'a')
        # CSV Format: CARTID, USERID, ITEM Quantity, SUBTOTAL, TAX AMOUNT, TAXRATE, TOTAL
        transFile.write(str(self.__id) + "," + self.__userID + "," + str(self.__itemsInBasket) + "," + str(self.__subtotal) + "," + str(format(self.__taxAmount, '.2f')) + "," + str(format(self.__taxRate, '.2%')) + "," + str(self.__total) + "\n")
        transFile.close()

    def __mapProductListToDictionary(self, productList):
        """Returns a mapped dictionary from a list passed in"""
        # initialize an empty dictionary
        dictionary = {}

        # Iterate over the length of the productList list returning the index each iteration \
        #   then look for indexes 0 and 1
        for index in range(len(productList)):
            if index == 0:
                dictionary["name"] = productList[index]
            elif index == 1:
                dictionary["price"] = productList[index]

        # Return the dictionary
        return dictionary

    def __calculateSubtotal(self):
        """Private method used to calculate the subtotal of self"""
        # Reset subtotal to 0.0
        self.__subtotal = 0.0

        # Iterate over each item in basket
        for itemId in self.__basket:
            # Multiply price by quantity and accumulate on self.__subtotal
            self.__subtotal += float(self.__basket[itemId]['price']) * float(self.__basket[itemId]['qty'])

        # Clean up subtotal formatting
        self.__subtotal = format(self.__subtotal, '.2f')

    def __calculateTaxAmount(self):
        try:
            # Calculate Tax amount
            self.__taxAmount = float(self.__total) - float(self.__subtotal)
        except ValueError as err:
            self.__taxAmount = 0.0
        except Exception as err:
            self.__taxAmount = 0.0

    def __calculateTotal(self):
        """Private method used to calculate the total of self"""
        self.__total= format(float(self.__subtotal) + (float(self.__subtotal) * float(self.__taxRate)), '.2f')

    def __calculateItemsInBasket(self):
        """Private method used to calculate amount of items in the basket of self"""
        # Reset Items in basket to 0
        self.__itemsInBasket = 0

        # Iterate over each item in basket
        for itemId in self.__basket:
            # Multiply price by quantity and accumulate on self.__subtotal
            self.__itemsInBasket += int(self.__basket[itemId]['qty'])
