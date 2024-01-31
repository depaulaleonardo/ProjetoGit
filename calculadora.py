"""
Calculadora com while
"""

while True:
        numero_1 = input ('Digite o primeiro valor: ')
        numero_2 = input ('Digite o segundo valor: ')
        operador = input('Digite o operador desejado (+-/*): ')

        numeros_validos = None
        num_1_float = 0
        num_2_float = 0

        try:
                num_1_float = float(numero_1)
                num_2_float = float(numero_2)
                numeros_validos = True
        except:
                numeros_validos = None
        
        if numeros_validos is None:
                print ('Um ou ambos os números digitados são inválidos')
                continue

        operadores_permitidos = '+-/*'

        if operador not in operadores_permitidos:
                print ('Operador inválido.')
                continue

        if len(operador) > 1:
                print('Digite apenas um operador.')
                continue
        
        print('Realizando sua conta. Confira o resultado abaixo: ')

        if operador == '+':
               soma = num_1_float + num_2_float
               print('A soma dos valores é igual a: ', soma)
        elif operador == '-':
               subtracao = num_1_float - num_2_float
               print('A subtração dos valores é igual a: ', subtracao)
        elif operador == '*':
               multiplicacao = num_1_float * num_2_float
               print('A multiplicação dos valores é igual a: ', multiplicacao)
        elif operador == '/':
                divisao = num_1_float / num_2_float
                print('A divisão dos valores é igual a: ', divisao)
        else:
               print('Nunca deveria chegar aqui.')

        sair = input ('Quer sair ? [s]im: ').lower().startswith('s')
        # lower = converte para minúsculo
        if sair is True:
           break