import dvd_store

def main():

    # Locals
    userAction = None
    user = None
    browsingAction = None
    store = dvd_store.Store(0.07)]

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
            print(user) # Print the User state
            userAction = None

    print(user) # Print the User state

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

        if browsingAction == 1:
            store.displayInventory()
            print()
            browsingAction = None
            
        elif browsingAction == 2:
            print("stuff")
            browsingAction = None

        elif browsingAction == 3:
            print("more stuff")
            browsingAction = None

        elif browsingAction == 4:
            print("even more stuff")
            browsingAction = None
            
        else browsingAction == 5:
            print("okay that's enough stuff")
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
