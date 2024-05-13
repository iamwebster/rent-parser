from save import save_data
from parser_cian import get_rent_data, rent_qty


rent_generator = get_rent_data(rent_qty)

if __name__ == '__main__':
    save_data(rent_generator)
