import json

"""
Скрипт обрабатывает JSON-файл, содержащий список словарей. 
Вычисляет произведение всех значений в каждом словаре, затем возвращает сумму этих произведений.
"""

def task(file_path: str) -> float:

    # Открываем и читаем JSON-файл
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Хранилище произведений значений из каждого словаря
    products = []

    # Перебираем каждый словарь из списка
    for dictionary in data:
        # Получаем только значения словаря
        values = dictionary.values()
        
        # Вычисляем произведение значений в текущем словаре
        product = 1
        for value in values:
            product *= value
        products.append(product)

    return round(sum(products), 3)

if __name__ == '__main__':
    print(task('input.json'))
