import csv

class Store:

    __INVENTORYFILE = "products.csv"
    
    def __init__(self, taxRate):
        self.__Inventory = self.setInventory()
        
        self.__taxRate = taxRate
        print(self.__storeInventory)

    def getTaxRate(self):
        return self.__taxRate


    def setTaxRate(self, taxRate):
        self.__taxRate = taxRate     


    
    def getInventory(self):
        return self.__storeInventory



    def setInventory(self):

        Inventory = []
        
      
        inventory_list = open(self.__INVENTORYFILE, 'r')
        
        for row in inventory_list:
            Inventory.append(row.strip().split(','))

            
        return Inventory
