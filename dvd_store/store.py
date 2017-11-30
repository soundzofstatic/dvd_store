import csv

class Store:

    __INVENTORYFILE = "products.csv"
    
    def __init__(self, taxRate):
        self.__Inventory = self.setInventory()
        self.__taxRate = taxRate

    def getTaxRate(self):
        return self.__taxRate


    def setTaxRate(self, taxRate):
        self.__taxRate = taxRate     

    def displayOptions(self):
        print("Here are your options for the store:")
        Variablenum = 0
        options = ["Inventory", "Cart", "Add", "Remove", "Checkout"]
        for option in options:
            Variablenum += 1
            print(str(Variablenum), option)
    
    def getInventory(self):
        return self.__Inventory

    def setInventory(self): #todo - this method name is misleading since setters are typically void functions that do not return anything
        Inventory = []
        inventory_list = open(self.__INVENTORYFILE, 'r')
        for row in inventory_list:
            Inventory.append(row.strip().split(','))
            
        return Inventory

    def displayInventory(self):
        Variablenum = 0
        for Itemlist in self.__Inventory:
            Variablenum += 1
            print(str(Variablenum) + " " + Itemlist[0] + " <> " + Itemlist[1])

        
