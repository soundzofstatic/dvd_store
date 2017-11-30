import uuid
import time
from datetime import datetime
from .cart import Cart

class User:

    __userFile = "users.csv"
    __userHistory = "usersHistory.csv"

    def __init__(self, membershipID = "", firstName = "", lastName = "", phoneNumber = ""):
        # Preset the fields for the object to blank, since we don't know if the user is registering or Signing-in
        self.__firstName = ""
        self.__lastName = ""
        self.__phoneNumber = ""
        self.__cart = Cart()
        self.__authenticated = False
        self.__authorized = False
        self.__statusCode = 0

        # Check if user is unregistered, AKA instantiated User object without any arguments
        if (membershipID == ""):
            # Unregistered, generate a membershipID and initialize additional fields
            self.__id = uuid.uuid4()

        else:
            # Set the submitted membershipID
            self.__id = membershipID

            # Check if the user is in our "database", if he does return their data
            userRecord = self.__checkUserExists()

            # User does not exist, set the appropriate status code
            if not userRecord:
                self.__statusCode = 1
                self.__authorized = False

            # User exist, map to object fields
            else:
                self.__firstName = userRecord[1]
                self.__lastName = userRecord[2]
                self.__phoneNumber = userRecord[3]
                self.__authorized = True

            # Create a history Record for this login attempt
            self. __logHistory()

    def __str__(self):
        if self.__authorized == True:
            return "User ID " + str(self.__id) + " belonging to " + self.__firstName + " " + self.__lastName + " (" + self.__phoneNumber + ") is now logged in"
        else:
            return self.__statusCodeMessage(self.__statusCode)

    def getID(self):
        return self.__id

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getPhoneNumber(self):
        return self.__phoneNumber

    def getAuthorized(self):
        return self.__authorized

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def registerUser(self):
        # Open File to Write to
        usersFile = open(self.__userFile, 'a')

        # Write to the File
        usersFile.write(str(self.__id) + "," + self.__firstName + "," + self.__lastName + "," + self.__phoneNumber + "\n")

        # Close the File
        usersFile.close()

        # Set the user to Authorized
        self.__authorized = True

    def __statusCodeMessage(self, statusCode):
        if statusCode == 0:
            return "User not found"
        elif statusCode == 1:
            return "User does not Exist"
        elif statusCode == 2:
            return "User Successfully signed in"

    def __checkUserExists(self):
        try:
            # Open file
            usersFile = open(self.__userFile, 'r')

            # iterate over file reading each line
            for line in usersFile:

                # Remove the '\n' char and split the line by comma's into a list
                record = line.strip().split(",")

                # Compare if record[0], the files membershipID record is equal to the objects id field
                if record[0] == self.__id:
                    return record

            # If you made it this far, nothing was matched therefore return False
            return False

        except FileNotFoundError as err:

            # Returns empty list if failed
            return False

        except Exception as err:

            # Returns empty list if failed
            return False

            # Scan each file in CSV for a matching UUID

    def __logHistory(self):
        # Open File to Write to
        historyFile = open(self.__userHistory, 'a')

        # Write to the File
        historyFile.write(
            str(self.__id) + ",Login Attempt," + str(self.__authorized) + "," + str(datetime.now()) + "," + str(
                int(round(time.time() * 1000))) + "\n")

        # Close the File
        historyFile.close()
