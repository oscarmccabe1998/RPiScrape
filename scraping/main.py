from selenium import webdriver
from bs4 import BeautifulSoup
from DataBaseLogic import initDBLogic, ReadFromDB, UpdateProduct

class ProductInfo:
    def __init__(self, item, preSavedItems):
        self.item = item
        #Search through item for name and price
        self.name = self.item.find('a', attrs={'class':'product-item-meta__title link--hover'}).string
        self.price = self.item.find('span', attrs = {'class':'price--convertible'}).string
        self.price = self.price.strip()
        self.availability = self.getProductAvailability('span', {'class':'loader-button__text'})
        self.printRes()
        present = False
        for iter in preSavedItems:
            if self.name == iter[0]:
                present = True
        if present == True:
            print("Update")
            UpdateProduct(self)
        else:
            initDBLogic(self)
           

    #Checks if an item is available through expected error when item is not available 
    #if the tag has text within it then it is available, otherwise it's out of stock 
    def getProductAvailability(self, HTMLClass, Attrs):
        try:
            initialAttemp = self.item.find(HTMLClass, attrs=Attrs).string
            return "Available"
        except(AttributeError):
            return "Out of Stock"
    
    def printRes(self):
        print(self.name)
        print(self.price)
        print(self.availability)
        print("")

def main ():
    preSavedItems = ReadFromDB()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    #This example makes use of Firefox and the geckodriver 
    #initial url to used to get data 
    targetURL = 'https://thepihut.com/collections/raspberry-pi-store'
    driver.get(targetURL)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #find HTML that contains all needed information on the products 
    Products = soup.find_all('div', attrs={'product-item__info product-item__info--with-button product-item--no-padding'})
    for item in Products:
        currentItem = ProductInfo(item, preSavedItems.preSavedItems)
    #driver.quit()

if __name__ == '__main__':
    main()


    