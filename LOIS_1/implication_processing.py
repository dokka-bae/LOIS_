from typing import Dict, List
import pandas as pd

class KeyValueError(Exception):
    def __init__(self, *args: object) -> None:
        self.__object = args[0]

    def __str__(self) -> str:
        return f"There is no key '{self.__object}' in sets"


def implication(data: Dict[str, List]) -> List[str]:
    # {'values': [{'p': {'a': '0', 'b': '0.3', 'c': '1'}}, 
    #             {'v': {'f': '1', 'd': '0.5', 't': '0'}}, 
    #             {'b': {'a': '0.8', 'b': '0.3', 'c': '0.9'}}], 
    #  'functions': [['p', 'v'], ['v', 'b']]}
    formulas : List = []
    for functions in data['functions']:
        for function in functions:
            if function not in data['values'].keys():
                raise KeyValueError(function)
        x,y = data['values'][functions[0]],data['values'][functions[1]]
        def_matrix = build_default_matrix(x,y)
        triangle_norm_matrix = build_triangle_matrix(x,y,def_matrix)
        formulas.append(build_formula(triangle_norm_matrix))
    return formulas

def build_default_matrix(x:Dict = {},y:Dict = {}) -> pd.DataFrame:
    matrix : pd.DataFrame = pd.DataFrame(columns=y.keys(),index=x.keys())
    for x_key in x.keys():
        for y_key in y.keys():
            if float(x[x_key])<1.:
                matrix.loc[x_key][y_key] = 1.
            else:
                matrix.loc[x_key][y_key] = float(y[y_key])
    return matrix

def build_triangle_matrix(x:Dict = {},y:Dict = {}, def_matrix:pd.DataFrame = pd.DataFrame) -> pd.DataFrame:
    # if (A = 1 & B = 1)  => 1
    # else if (B = 1 & A < 1) => A
    # else if (B < 1 & A = 1) => B
    # else => 0
    matrix : pd.DataFrame = pd.DataFrame(0,columns=y.keys(),index=x.keys())
    for x_key in x.keys():
        for y_key in y.keys():
            if def_matrix.loc[x_key][y_key] == 1. and float(x[x_key]) == 1. :
                matrix.loc[x_key][y_key] = 1.
            elif float(x[x_key]) == 1. and def_matrix.loc[x_key][y_key] < 1.:
                matrix.loc[x_key][y_key] = def_matrix.loc[x_key][y_key]
            elif float(x[x_key]) < 1. and def_matrix.loc[x_key][y_key] == 1.:
                matrix.loc[x_key][y_key] = float(x[x_key])
    return matrix

def build_formula(triangle_matrix: pd.DataFrame) -> str:
    formula : List = []
    for col in triangle_matrix.columns:
        formula.append(f'({col},{triangle_matrix[col].max()})')
    return '{'+','.join(formula)+'}'
      