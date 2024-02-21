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
### Build Dockerfile
sudo docker build -t rpiscrape .

### Run Docker Image 
sudo docker run rpiscrape
