import dvd_store

def main():

    # Locals
    userAction = None
    user = None
    browsingAction = None
    store = dvd_store.Store("OOP DVD Store", 0.07)
    cart = None
    sessionAction = None

    print("Welcome to the " + store.getName() + ".")
    print()

    while sessionAction == None:

        # Prompt User to Login or Register
        while userAction == None:
            userAction = validateUserAction(input("Would you like to \"login\" or \"register\" for a membership account? To Exit, type \"exit\".\n").lower())
            print()

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
                print()

            elif userAction == "exit":
                userAction = "exit"
                continue

            # Check that userAction is still not equal to None
            if userAction != None:
                # Check User Authorization
                if user.getAuthorized() == False:
                    userAction = None

        if userAction != "exit":
            # By this point user should pertain to a valid user, check to see that they are a valid user
            if(user.getAuthorized()):
                print("Hello " + user.getFirstName() + ",")  # Print a personalized greeting
                print()
                # Create a Cart for this User
                cart = dvd_store.Cart(user.getID(), store.getTaxRate())
        else:
            # User chose to exit without logging in or registering, thus skip the browsing
            browsingAction = 6
            sessionAction = "exit"


        # Iterate over Browsing Options
        while browsingAction == None:

            # Call on store.displayOptions()
            store.displayOptions()
            print()

            try:
                # Prompt the user for their choice
                browsingAction = validateBrowsingAction(int(input("Choose the option number of the action you would like to do.\n")))
                print()  # Empty line for readability

            except ValueError as err:
                warning(err)
                browsingAction = None
            except Exception as err:
                warning(err)
                browsingAction = None

            if browsingAction == 1: # List
                print("Here is the list of our inventory ")
                store.displayInventory()
                print()
                browsingAction = None

            elif browsingAction == 2: # Cart
                print("Here is the current contents of your cart: ")
                cart.showBasketList()
                print()
                browsingAction = None

            elif browsingAction == 3: # Add
                productID = None
                productQty = None
                stock = store.getInventory()

                # Show the inventory
                store.displayInventory()

                while productID == None:
                    try:
                        productID = int(input("Which product number would you like to add to the cart?\n")) - 1
                        print()
                    except ValueError as err:
                        warning(err)

                    # Check if the ProductID is within the stock
                    if not checkProductInList(productID, stock):
                        productID = None

                while productQty == None:
                    try:
                        productQty = int(input("What quantity?\n"))
                        print()
                    except ValueError as err:
                        warning(err)

                # Add the item to the Cart
                cart.addItem(productID, productQty, stock[productID], stock)

                print() # Empty line for readability

                # Display the current contents of the Cart so the user can see the changes they have made
                cart.showBasketList()

                browsingAction = None

            elif browsingAction == 4: # Remove
                productID = None
                productQty = None

                # Display the current contents of the Cart
                cart.showBasketList()

                while productID == None:
                    try:
                        productID = int(input("Which product number would you like to REMOVE from the cart?\n")) - 1
                        print()
                    except ValueError as err:
                        warning(err)

                    # Check if the ProductID is within the store.getInventory()
                    if not checkProductInList(productID, store.getInventory()):
                        productID = None

                while productQty == None:
                    try:
                        productQty = int(input("What quantity?\n"))
                        print()
                    except ValueError as err:
                        warning(err)

                # Remove from Cart
                cart.removeItem(productID, productQty)

                print()  # Empty line for readability

                # Display the current contents of the Cart so the user can see the changes they have made
                cart.showBasketList()

                browsingAction = None

            elif browsingAction == 5: # Checkout
                print("Your subtotal is: $ ", cart.getSubtotal())
                print("Your total including the tax rate is: $ ", cart.getTotal())
                print()
                cart.checkout()

                # Ask the user if they would like to logout or start a new cart
                logoutPrompt = validateLogoutAction(input("Type \"exit\" to logout and start a new session, or \"new cart\" to start a new cart\n").lower())
                print()

                if(logoutPrompt == "exit"):
                    browsingAction = 6

                elif logoutPrompt == "new cart":
                    # Override cart with a new Cart Object
                    cart = dvd_store.Cart(user.getID(), store.getTaxRate())
                    browsingAction = None

            # User has selected to log out
            elif browsingAction == 6:
                browsingAction = 6

            else:
                warning("Please provide an option between 1 and 6")
                browsingAction = None

        print("Have a wonderful day. Goodbye.")
        print()
        print()

        # Reset the cart and user object as well as the userAction and browsingAction
        # since the session may continue
        cart = None
        user = None
        userAction = None
        browsingAction = None



# Function used to validate UserActions
def validateUserAction(action):
    try:
        # Test for int
        action = int(action)
        # Test for float
        action = float(action)
        return None
    except ValueError:
        if action == "login":
            return action
        elif action == "register":
            return action
        elif action == "exit":
            return action
        else:
            return None

# Function used to validate logoutPrompt
def validateLogoutAction(action):
    try:
        # Test for int
        action = int(action)
        # Test for float
        action = float(action)
        return None
    except ValueError:
        # Continue, verified as string
        if action == "exit":
            return action
        elif action == "new cart":
            return action
        else:
            return None

def checkProductInList(productID, inventory):
    try:
        # Test for int
        int(productID)
        # Test for float
        float(productID)
        # Run Check
        if (productID - 1) > len(inventory):
            warning("Product ID is not in inventory")
            return False
        else:
            return True
    except ValueError:
        return False
    except Exception:
        return False

def warning(message):
    print()
    print("*************** WARNING ****************")
    print("\n", end="")
    print(message)
    print("\n", end="")
    print("*************** WARNING ****************")
    print()

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
    elif action == 6: #"logout"
        return action
    else:
        return None
    
main()
