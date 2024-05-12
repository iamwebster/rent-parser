import requests 
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent(platforms='pc')

headers = {
    'User-Agent': ua.random,
}

with requests.Session() as sess:
    url = 'https://perm.cian.ru/snyat-kvartiru-nedorogo/'
    response = sess.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    qty_rent = int(soup.find('div', attrs={'data-name': 'SummaryHeader'}).text.split()[1])
    rent_all = soup.find_all('div', attrs={'data-testid': 'offer-card'}, limit=qty_rent)
    
    for rent in rent_all:
        link_data = rent.find('a', class_='_93444fe79c--link--VtWj6')
        link = link_data.get('href')
        title = link_data.find('span', attrs={'data-mark': 'OfferTitle'}).find('span').text
        address = rent.find('div', class_='_93444fe79c--labels--L8WyJ').text
        price_per_month = rent.find('span', attrs={"data-mark": "MainPrice"}).text
        price_info = rent.find('p', attrs={'data-mark': 'PriceInfo'}).text
        print(link)
        print(title)
        print(address)
        print(price_per_month)
        print(price_info)
        print('\n')

