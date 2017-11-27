import dvd_store

def main():

    # Locals
    userAction = None
    user = None
    browsingAction = None
    store = dvd_store.Store(0.07)

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
        #store.displayOptions()

        try:
            # Prompt the user for their choice
            browsingAction = validateBrowsingAction(int(input("Provide the option number of the action you would like to do.")))

        except ValueError as err:
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
    if action == 0: #"list"
        return action
    elif action == 1: #"cart"
        return action
    elif action == 2: #"add"
        return action
    elif action == 3: #"remove"
        return action
    elif action == 4: #"checkout"
        return action
    else:
        return None

main()