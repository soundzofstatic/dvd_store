import csv

class Store:

    __INVENTORY_FILE = "products.csv"
    
    def __init__(self, taxRate):
        self.__Inventory = self.auditInventory()
        self.__taxRate = taxRate

    def getTaxRate(self):
        return self.__taxRate

    def getInventory(self):
        return self.__Inventory

    def setTaxRate(self, taxRate):
        self.__taxRate = taxRate     

    def displayOptions(self):
        print("Here are your options for the store:")
        Variablenum = 0
        options = ["Inventory", "Cart", "Add", "Remove", "Checkout"]
        for option in options:
            Variablenum += 1
            print(str(Variablenum), option)

    def displayInventory(self):
        Variablenum = 0
        for Itemlist in self.__Inventory:
            Variablenum += 1
            print(str(Variablenum) + " " + Itemlist[0] + " <> " + Itemlist[1])

    def auditInventory(self):
        Inventory = []
        inventory_list = open(self.__INVENTORY_FILE, 'r')
        for row in inventory_list:
            Inventory.append(row.strip().split(','))
            
        return Inventory
