'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Довидович Тимофей Михайлович, Залевский Андрей Сергеевич, Кочурко Василий Вячеславович
Вариант 24:
Импликация Вебера
'''


from typing import Dict, List
import pandas as pd

class KeyValueError(Exception):
    def __init__(self, *args: object) -> None:
        self.__object = args[0]

    def __str__(self) -> str:
        return f"There is no key '{self.__object}' in sets"


def implication_processing(data: Dict[str, List]) -> List[str]:
    # {'values': [{'p': {'a': '0', 'b': '0.3', 'c': '1'}}, 
    #             {'v': {'f': '1', 'd': '0.5', 't': '0'}}, 
    #             {'b': {'a': '0.8', 'b': '0.3', 'c': '0.9'}}], 
    #  'functions': [['p', 'v'], ['v', 'b']]}
    formulas = []
    for functions in data['functions']:
        for function in functions:
            if function not in data['values'].keys():
                raise KeyValueError(function)
        x,y = data['values'][functions[0]],data['values'][functions[1]]
        implication_matrix = implication(x,y)
        print(implication_matrix)
        fuzzy_conjunctions = []
        for item in data['values'].values():
            if item.keys() == x.keys():
                fuzzy_conjunctions.append(fuzzy_conjunction(item,y,implication_matrix))
                print(fuzzy_conjunctions[-1])
        formulas.append(build_formula(fuzzy_conjunctions)) 
    return formulas

def implication(x:Dict = {},y:Dict = {}) -> pd.DataFrame: #implication
    matrix : pd.DataFrame = pd.DataFrame(columns=y.keys(),index=x.keys())
    for x_key in x.keys():
        for y_key in y.keys():
            if float(x[x_key])<1.:
                matrix.loc[x_key][y_key] = 1.
            else:
                matrix.loc[x_key][y_key] = float(y[y_key])
    return matrix

def fuzzy_conjunction(x:Dict = {},y:Dict = {}, implication_matrix:pd.DataFrame = pd.DataFrame) -> pd.DataFrame: # нечеткий вывод
    matrix : pd.DataFrame = pd.DataFrame(columns=y.keys(),index=x.keys())
    for x_key in x.keys():
        for y_key in y.keys():
            if float(x[x_key]) == 1 and implication_matrix.loc[x_key][y_key] == 1:
                matrix.loc[x_key][y_key] = 1
            elif float(x[x_key]) < 1 and implication_matrix.loc[x_key][y_key] == 1:
                matrix.loc[x_key][y_key] = float(x[x_key])
            elif float(x[x_key]) == 1 and implication_matrix.loc[x_key][y_key] < 1:
                matrix.loc[x_key][y_key] = implication_matrix.loc[x_key][y_key]
            else:
                matrix.loc[x_key][y_key] = 0
    return matrix

def build_formula(fuzzy_conjunctions:List[pd.DataFrame]) -> str:
    result_formulas = []
    for formula in fuzzy_conjunctions:
        result_formula = []
        for col in formula:
            result_formula.append(f'({col},{formula[col].max()})')
        result_formulas.append('{'+','.join(result_formula)+'}')
    return result_formulas
      