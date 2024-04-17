import json


FILENAME = "input.json"


def task() -> int:
    with open(FILENAME, "r", encoding='utf-8') as file_1:
        file_2 = json.load(file_1)# TODO Десериализуйте содержимое JSON файла
    list_values = []
    for item in file_2:
        list_values.append(item["contains_improvement_appeals"])


    return sum(list_values)

      # TODO Просуммируйте все значения по ключу contains_improvement_appeals



if __name__ == '__main__':
    print(task())
