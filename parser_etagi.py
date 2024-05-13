import requests 
from bs4 import BeautifulSoup
from utils import headers 


url = 'https://perm.etagi.com/realty_rent/?price_max=13000&studio[]=true&studio[]=false&rooms[]=1&rooms[]=2&type[]=flat&type[]=obshaga&orderId=priceasc'

with requests.Session() as sess:
    response = sess.get(url, headers=headers)
    if response.status_code >= 400:
        sess.close()
        print('Error! Status code:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        rent_qty = int(soup.find('button', class_='FV26R CbXcz jJShB gzq6t _jBUx GmYmq zPhuj B12u1').text.split()[1])
        rent_all = soup.find_all('div', {'data-testid':'object_card'}, limit=rent_qty)

        def get_rent_data():

            for rent in rent_all:
                link = 'https://perm.etagi.com' + rent.find('a', class_='templates-object-card__slider').get('href')
                price_per_month = rent.find('span', class_='eypL8 uwvkD').text
                price_info = rent.find('div', class_='ci9YC P3xSS').find('span').text
                address_area = rent.find('div', attrs={'displayname': 'cardDistrict'}).find('a').text
                address_number = rent.find('div', class_='EDAsp').text.strip()
                if address_area:
                    full_address = ', '.join([address_area, address_number])
                else:
                    full_address = address_number

                rent_item = {'link': link,
                            'address': full_address,
                            'price_per_month': price_per_month,
                            'price_info': price_info,
                }

                yield rent_item

