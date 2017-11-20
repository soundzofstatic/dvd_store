import uuid;

class Cart:

    def __init__(self):

        self.__id = uuid.uuid4()

    def __str__(self):
        return "This cart ID is " + str(self.__id)