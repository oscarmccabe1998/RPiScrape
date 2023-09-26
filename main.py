from selenium import webdriver
from bs4 import BeautifulSoup

def main ():
    driver = webdriver.Firefox()
    #This example makes use of Firefox and the geckodriver 
    #initial url to used to get data 
    driver.get('https://thepihut.com/collections/raspberry-pi-store') 
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #find HTML that contains all needed information on the products 
    Products = soup.find_all('div', attrs={'product-item__info product-item__info--with-button product-item--no-padding'})
    for item in Products:
        #for each product found search for the name and price 
        name = item.find('a', attrs={'class':'product-item-meta__title link--hover'}).string
        price = item.find('span', attrs = {'class':'price--convertible'}).string
        #used to get rid of random spaces in returned data 
        price = price.strip()
        #Determin if the product is in stock depending on the type of button returned from the webpage 
        try:
            availability = item.find('span', attrs = {'class':'loader-button__text'}).string
            if availability:
                availability = "in Stock"
        except(AttributeError):
            availability = "Out of Stock"
        print(name)
        print(price)
        print(availability)
        print("")
    driver.quit()

if __name__ == '__main__':
    main()


    