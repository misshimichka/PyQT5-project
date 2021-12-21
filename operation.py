# функция, генерирующая числа для теста/тренировки

from random import *


def operations():
    evals = []

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]
    string1 = f'(2) {bin1} + {bin2} = '
    evals.append(bin(n1 + n2))

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = bin(max(n1, n2))[2:]
    bin2 = bin(min(n1, n2))[2:]
    string2 = f'(2) {bin1} - {bin2} = '
    evals.append(bin(max(n1, n2) - min(n1, n2)))

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]
    string3 = f'(2) {bin1} * {bin2} = '
    evals.append(bin(n1 * n2))

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = oct(n1)[2:]
    bin2 = oct(n2)[2:]
    string4 = f'(8) {bin1} + {bin2} = '
    evals.append(oct(n1 + n2))

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = oct(max(n1, n2))[2:]
    bin2 = oct(min(n1, n2))[2:]
    string5 = f'(8) {bin1} - {bin2} = '
    evals.append(oct(max(n1, n2) - min(n1, n2)))

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = hex(n1)[2:]
    bin2 = hex(n2)[2:]
    string6 = f'(16) {bin1} + {bin2} = '.upper()
    evals.append(hex(n1 + n2))

    n1 = randint(1, 257)
    n2 = randint(1, 257)
    bin1 = hex(max(n1, n2))[2:]
    bin2 = hex(min(n1, n2))[2:]
    string7 = f'(16) {bin1} - {bin2} = '.upper()
    evals.append(hex(max(n1, n2) - min(n1, n2)))

    strings = [string1, string2, string3, string4, string5, string6, string7]

    return [strings, evals]
