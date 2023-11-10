'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Довидович Тимофей Михайлович, Залевский Андрей Сергеевич, Кочурко Василий Вячеславович
Вариант 24:
Импликация Вебера
'''


from file_reader import read_file
import re
from typing import List, Dict
from BND_checker import BND_checker_function, BND_checker_set

class InputError(Exception):
    def __init__(self, *args: object) -> None:
        self.__message = args[0]

    def __str__(self) -> str:
        return self.__message


def is_valid(data: List[str] = []) -> List[str]:
    sets = []
    functions = []
    for item in data:
        if len(item)<7:
            continue
        a = BND_checker_set(item)
        b = BND_checker_function(item)
        if a.is_valid:
            sets.append(item)
        elif b.is_valid:
            functions.append(item)
    if sets == []:
        raise InputError('No sets were defined')
    if functions == []:
        raise InputError('No functions were defined')
    return sets, functions


def parsing(iteration: int = 0) -> Dict[str,List]:
    file_data = read_file(f".\\tests\\{iteration+1}")
    sets, functions = is_valid(file_data)
    data = {
        'values': {},
        'functions': []
    }
    for item in sets:
        key = item[:item.index('=')]
        item = item[item.index('{'):]
        item = item.replace("{","").replace("}","")
        if len(item) == 0:
            values = {}
        else:
            item = item.split('),(')
            item = [x.replace('(','').replace(')','') for x in item]
            values = {key: value for element in item for key,
                      value in [element.split(',')]}
        dict_values = {
            key: values
        }
        data['values'].update(dict_values)
    for item in functions:
        key = item[:item.index('(')]
        item = item[item.index('=(')+2:][:-1]
        key = [x[:x.index(')')+1] for x in item.split('~>')]
        data['functions'].append(key)
    return data
