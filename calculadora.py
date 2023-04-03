# -*- coding util-8 -*-
a = int(input("escolha um número:"))
b = int(input("escolha um número:"))
c = input('escolha sua operação matemática: ')

if c == 'multiplicação':
    print(a*b)
elif c == 'subtração' or "menos":
    print(a-b)
elif c == 'adição' or 'soma':
    print(a+b)
elif c == 'divisão' or 'dividir':
    print(a/b)
