'''
Лабораторная работа №1
по дисциплине ЛОИС
Выполнена студентами группы 121703
Довидович Тимофей Михайлович, Залевский Андрей Сергеевич, Кочурко Василий Вячеславович
Вариант 24:
Импликация Вебера
'''


from parser_ import parsing
from implication_processing import implication_processing


def main():
    for i in range(3):
        data = parsing(i)
        formulas = implication_processing(data)
        for formula in formulas:
            print(formula)
        print()

if __name__ == '__main__':
    main()
