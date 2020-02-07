import requests
from bs4 import BeautifulSoup

url = 'http://ofxaddons.com/categories'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for a in soup.find_all("div", class_="repo-name"):
    print(a)