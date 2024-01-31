#Faça um programa que crie uma matriz M (com valores 
#informados do usuário) e mostre a matriz com o dobro 
#dos valores lidos (2*M).

import random

def ler_matriz():
    while True:
            try:
                linhas = int(input("Digite o número de linhas da matriz: "))
                colunas = int(input("Digite o número de colunas da matriz: "))
                if linhas <=0 or colunas <=0:
                    raise ValueError("O número de linhas e colunas precisa ser positivo.")
                break
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")


    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            while True:
                try:
                    valor = float(input(f"Digite o valor para a posição [{i+1},{j+1}]: "))
                    break
                except ValueError as e:
                    print(f"Erro: {e}. Tente novamente.")
            linha.append(valor)
        matriz.append(linha)

    return matriz

def dobrar_valores(matriz):
    matriz_dobrada = [[valor*2 for valor in linha] for linha in matriz]
    return matriz_dobrada

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

#Chamada de funções
matriz_usuario = ler_matriz()
matriz_dobrada = dobrar_valores(matriz_usuario)

#Imprimir a matriz original
print("\nMatriz Original:")
imprimir_matriz(matriz_usuario)

# Imprimir a matriz dobrada
print("\nMatriz Dobrada (2*M):")
imprimir_matriz(matriz_dobrada)