from selenium import webdriver
from bs4 import BeautifulSoup
import time


def main ():
    driver = webdriver.Firefox()
    url = "https://thepihut.com/collections/raspberry-pi-store"
    driver.get('https://thepihut.com/collections/raspberry-pi-store')
    #time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    Products = soup.find_all('div', attrs={'product-item__info product-item__info--with-button product-item--no-padding'})
    for item in Products:
        name = item.find('a', attrs={'class':'product-item-meta__title link--hover'}).string
        price = item.find('span', attrs = {'class':'price--convertible'}).string
        price = price.strip()
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


    