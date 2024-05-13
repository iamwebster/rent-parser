import json
import os


def save_data(*args):

    cwd = os.getcwd()
    filepath = os.path.join(cwd, 'data.json')

    if not os.path.exists(filepath):
        with open('data.json', 'w') as outfile:
                outfile.write('[')

    for generator_item in args:
        for data in generator_item():
            with open('data.json', 'a', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
                outfile.write(',')
        
    with open('data.json', 'a') as outfile:
        outfile.write(']')
        