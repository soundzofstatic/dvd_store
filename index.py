import dvd_store

def main():

    # Locals
    userAction = None
    user = None
    browsingAction = None
    store = dvd_store.Store(0.07)
    cart = None

    # Prompt User to Login or Register
    while userAction == None:
        userAction = validateUserAction(input("Would you like to \"login\" or \"register\" for a membership account?\n").lower())

        if userAction == "register":
            # Instantiate a new User
            user = dvd_store.User()

            # Set the Users Attributes
            user.setFirstName(input("What is your First Name?\n").strip())
            user.setLastName(input("What is your Last Name?\n").strip())
            user.setPhoneNumber(input("What is your Phone Number?\n").strip())

            # Register the User
            user.registerUser()

        elif userAction == "login":
            # Instantiate a new User
            user = dvd_store.User(input("What is your membership ID?\n").strip())

        # Check User Authorization
        if user.getAuthorized() == False:
            userAction = None

    print(user) # Print the User state
    # By this point user should pertain to a valid user, check to see that they are a valid user
    if(user.getAuthorized()):
        # Create a Cart for this User
        cart = dvd_store.Cart(user.getID(), store.getTaxRate())

    # Iterate over Browsing Options
    while browsingAction == None:

        # Call on store.displayOptions()
        store.displayOptions()
        print()
        
        try:
            # Prompt the user for their choice
            browsingAction = validateBrowsingAction(int(input("Provide the option number of the action you would like to do.")))

        except ValueError as err:
            browsingAction = None

        if browsingAction == 1: # List
            print("Here is the list of our inventory ")
            store.displayInventory()
            print()
            browsingAction = None
            
        elif browsingAction == 2: # Cart
            print("stuff")
            browsingAction = None

        elif browsingAction == 3: # Add

            productID = None
            productQty = None
            stock = store.getInventory()

            while productID == None:
                try:
                    productID = int(input("Which product number would you like to add to the cart? ")) - 1
                except ValueError as err:
                    print(err)

            while productQty == None:
                try:
                    productQty = int(input("What quantity?"))
                except ValueError as err:
                    print(err)

            # Add the item to the Cart
            cart.addItem(productID, productQty, stock[productID], stock)

            # todo - print feedback that the item was actually added to the store
            print(cart) # todo - For now print the cart for temporary feedback

            browsingAction = None

        elif browsingAction == 4: # Remove
            productID = None
            productQty = None
            stock = store.getInventory()

            # todo - display the contents of the Cart, same as the method used within a "cart" browsingAction

            while productID == None:
                try:
                    productID = int(input("Which product number would you like to REMOVE from the cart? ")) - 1
                except ValueError as err:
                    print(err)

            while productQty == None:
                try:
                    productQty = int(input("What quantity?"))
                except ValueError as err:
                    print(err)

            # Remove from Cart
            cart.removeItem(productID, productQty)

            # todo - print feedback that the item was actually removed from the store
            print(cart)  # todo - For now print the cart for temporary feedback

            browsingAction = None
            
        elif browsingAction == 5: # Checkout
            print("okay that's enough stuff")
            browsingAction = None

        else:
            browsingAction = None

# Function used to validate UserActions
def validateUserAction(action):
    if action == "login":
        return action
    elif action == "register":
        return action
    else:
        return None

# Function used to validate BrowsingActions
def validateBrowsingAction(action):
    if action == 1: #"list"
        return action
    elif action == 2: #"cart"
        return action
    elif action == 3: #"add"
        return action
    elif action == 4: #"remove"
        return action
    elif action == 5: #"checkout"
        return action
    else:
        return None
    
main()