numero_inteiro = int(input('Insira um número inteiro: '))
numero = numero_inteiro // 3
resto = numero_inteiro % 3
if resto == 0:
    print('O número', numero_inteiro, 'é divisível por 3')
else:
    print('O número', numero_inteiro, 'não é divisível por 3')