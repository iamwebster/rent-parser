import parser_cian, parser_etagi
from pprint import pprint 
from save import save_data


if __name__ == '__main__':
    save_data(parser_cian.get_rent_data, parser_etagi.get_rent_data)
