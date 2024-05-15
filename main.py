import requests
from parser_cian import get_parser_data
from fake_useragent import UserAgent
from utils import RentDataManager
from pprint import pprint 

ua = UserAgent(platforms='pc')

headers = {
    'User-Agent': ua.random,
}

URL = 'https://perm.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&maxprice=13000&offer_type=flat&region=4927&room1=1&room2=1&room9=1&sort=creation_date_desc&type=4'


def main():
    with requests.Session() as session:
        parser_data = get_parser_data(session=session, url=URL, headers=headers)

        manager = RentDataManager(parser_data)
        result = manager.check_new_data()
        pprint(result)

if __name__ == '__main__':
    main()
