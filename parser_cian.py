import requests 
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from utils import headers


url = 'https://perm.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&maxprice=13000&offer_type=flat&region=4927&room1=1&room2=1&room9=1&type=4'

with requests.Session() as sess:
    # url = 'https://perm.cian.ru/snyat-kvartiru-nedorogo/'
    response = sess.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    rent_qty = int(soup.find('div', attrs={'data-name': 'SummaryHeader'}).text.split()[1])
    rent_all = soup.find_all('div', attrs={'data-testid': 'offer-card'}, limit=rent_qty)
    

    def get_rent_data(rent_qty):
        yield {'rent_quantity': rent_qty}

        for rent in rent_all:
            link_data = rent.find('a', class_='_93444fe79c--link--VtWj6')
            link = link_data.get('href')
            title = link_data.find('span', attrs={'data-mark': 'OfferTitle'}).find('span').text
            address = rent.find('div', class_='_93444fe79c--labels--L8WyJ').text
            price_per_month = rent.find('span', attrs={"data-mark": "MainPrice"}).text
            price_info = rent.find('p', attrs={'data-mark': 'PriceInfo'}).text
            time_created = rent.find('div', class_='_93444fe79c--absolute--yut0v').text 


            rent_item = {'link': link,
                    'title': title,
                    'address': address,
                    'price_per_month': price_per_month,
                    'price_info': price_info,
                    'time_created': time_created,
            }

            yield rent_item
        