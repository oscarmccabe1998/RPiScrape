# Scraping Logic 
## Found in the scraping directory 
cd scraping
# Usage 
## Virtual Environment
### Create a virtual environment
python3 -m venv .
### Start Virtual Environment
source bin/activate
### install dependancies
pip3 install -r req.txt
## Get geckodriver
- [Link to geckodriver](https://github.com/mozilla/geckodriver/releases)
- [Instructions to add geckodriver](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu)
## Run the script 
python3 main.py

## Docker Usage 
### Build Dockerfile's
### Create Docker Network
sudo docker network create rpi-scrape-network
#### Build Database Image
sudo docker build -t rpidatabase database/
#### Run Database Image
sudo docker run -d --name rpi-scrape --network rpi-scrape-network -p 3306:3306 rpidatabase
Once this is done use the docker inspect command to get the ip address on the network and update the DatabaseLogic.py script
#### Build WebScraperImage
sudo docker build -t rpiscrape scraping/
#### Run Scraper Image  
sudo docker run rpiscrape --name python-scraper --network rpi-scrape-network

