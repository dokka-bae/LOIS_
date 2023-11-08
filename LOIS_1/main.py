from parser_ import parsing
from implication_processing import implication


def main():
    for i in range(5):
        data = parsing(i)
        formulas = implication(data)
        for formula in formulas:
            print(formula)
        print('\n')

if __name__ == '__main__':
    main()
