import json 
import os

class RentDataManager:
    '''
    - Принимает список со словарями объявлений об аренде.
    - Если подобных данных еще нету в системе, то сохраняет данные в json-формате.
    '''
    def __init__(self, parser_data: list) -> None:
        self.parser_data = parser_data

        filepath = os.path.join(os.getcwd(), 'data.json')
        if not os.path.exists(filepath):
            self.save_data(parser_data)

    def save_data(self, new_data: list) -> None:
        '''Сохраняет список с объявлениями об аренде в json-формате.'''
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

    def get_old_data(self) -> list:
        '''Метод для загрузки предыдущих данных об аренде из json файла.'''
        with open('data.json') as file:
            old_data = json.load(file)
            return old_data
            
    def check_new_data(self) -> dict:
        '''Метод для получения информации о новых объявлениях об аренде.'''
        new_items = []
        for item in self.parser_data:
            if item not in self.get_old_data():
                new_items.append(item)

        result_data = {}
        if new_items:
            self.save_data(self.parser_data)
            result_data['Статус'] = 'Данные перезаписаны'
            result_data['Новых записей'] = len(new_items)
            result_data['Новые записи'] = new_items

        else:
            result_data['Статус'] = 'Нету новых объявлений'

        result_data['Всего записей'] = len(self.parser_data)

        return result_data
        