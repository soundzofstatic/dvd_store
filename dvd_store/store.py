import csv

class Store:

    __INVENTORY_FILE = "products.csv"
    
    def __init__(self, name, taxRate):
        self.__Inventory = self.auditInventory()
        self.__name = name
        self.__taxRate = taxRate

    def getName(self):
        return self.__name

    def getTaxRate(self):
        return self.__taxRate

    def getInventory(self):
        return self.__Inventory

    def setName(self, name):
        self.__name = name

    def setTaxRate(self, taxRate):
        self.__taxRate = taxRate

    def displayOptions(self):
        print("Here are your options for the store:")
        print("----------------------------------------")
        Variablenum = 0
        options = ["Inventory", "Cart", "Add", "Remove", "Checkout", "Logout"]
        for option in options:
            Variablenum += 1
            print(str(Variablenum) + " - " + option)

        print("----------------------------------------")

    def displayInventory(self):
        Variablenum = 0
        print("----------------------------------------")
        for Itemlist in self.__Inventory:
            Variablenum += 1
            print(str(Variablenum) + " - " + Itemlist[0] + " - " + Itemlist[1])
        print("----------------------------------------")

    def auditInventory(self):
        Inventory = []
        inventory_list = open(self.__INVENTORY_FILE, 'r')
        for row in inventory_list:
            Inventory.append(row.strip().split(','))
            
        return Inventory
