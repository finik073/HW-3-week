#1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
#   В списке нужно создать не менее 4-х словарей
#2. Запишите содержимое списка словарей в файл в формате csv

import csv

users = [
            {'name': 'Mark', 'age': 25, "job": 'teacher'},
            {'name': 'Leo', 'age': 29, "job": 'ceo'},
            {'name': 'Dan', 'age': 34, "job": 'developer'},
            {'name': 'Robert', 'age': 31, "job": 'manager'},
            {'name': 'Baron', 'age': 30, "job": 'worker'}
        ]

def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as empty_file:
        fields = ['name', 'age', 'job']
        export = csv.DictWriter(empty_file, fields, delimiter=';')
        export.writeheader()
        for user in users:
            export.writerow(user)


if __name__ == "__main__":
    main()
