import requests
from bs4 import BeautifulSoup 



def priceTracker():
    url = 'https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

while True:
    print('Currect Price of Nasdaq: ' +priceTracker())
