"""
Конвертер из CSV в JSON.
"""

import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

# Функция для конвертации CSV в JSON
def task(csv_file: str, json_file: str) -> None:
    """
    Читает данные из CSV файла, преобразует их в JSON формат и сохраняет в указанный файл.

    csv_file: Путь к входному файлу.
    json_file: Путь к выходному файлу.
    """
    # читает строки CSV как словари
    with open(csv_file, 'r') as file:
        read = list(csv.DictReader(file))  # Преобразуем содержимое в список словарей

    # Сериализация данных в JSON
    with open(json_file, 'w') as file:
        json.dump(read, file, indent=4)  


if __name__ == '__main__':

    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="") 
