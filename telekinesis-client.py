import requests
from bs4 import BeautifulSoup as soup

# username = str(input("Enter the username of the github page: "))
username = 'nastyusb'

g = requests.get("http://" + username + ".github.io")

page_soup = soup(g.text, "html.parser")

containers = page_soup.findAll("div", {"class":"link"})

for container in containers:
    text = container.getText()
    
    print(text)
