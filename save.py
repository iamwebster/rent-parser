from parser_cian import rent_qty
import json


def save_data(data):
    with open('data.json', 'w') as outfile:
        outfile.write('[')

    for data_count in range(rent_qty):
        with open('data.json', 'a', encoding='utf-8') as outfile:
            json.dump(next(data), outfile, indent=4, ensure_ascii=False)
            if data_count + 1 != rent_qty:
                outfile.write(',')

    with open('data.json', 'a') as outfile:
        outfile.write(']')
