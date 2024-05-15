from bs4 import BeautifulSoup

def get_parser_data(session, url: str, headers: dict) -> list:
    response = session.get(url, headers=headers)
    if response.status_code >= 400:
        return f'Error! Status code: {response.status_code}'
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        rent_qty = int(soup.find('div', attrs={'data-name': 'SummaryHeader'}).text.split()[1])
        rent_all = soup.find_all('div', attrs={'data-testid': 'offer-card'}, limit=rent_qty)

        result = []
        for rent in rent_all:
            link_data = rent.find('a', class_='_93444fe79c--link--VtWj6')
            link = link_data.get('href')
            title = link_data.find('span', attrs={'data-mark': 'OfferTitle'}).find('span').text
            address = rent.find('div', class_='_93444fe79c--labels--L8WyJ').text
            price_per_month = rent.find('span', attrs={"data-mark": "MainPrice"}).text
            price_info = rent.find('p', attrs={'data-mark': 'PriceInfo'}).text
            time_created = rent.find('div', class_='_93444fe79c--absolute--yut0v').text 

            rent_item = {
                'link': link,
                'title': title,
                'address': address,
                'price_per_month': price_per_month,
                'price_info': price_info,
                'time_created': time_created,
            }

            result.append(rent_item)

        return result
