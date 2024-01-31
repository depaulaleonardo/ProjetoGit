#Faça um programa que crie uma matriz aleatoriamente. 
#O tamanho da matriz deve ser informado pelo usuário

import random

def ler_linha():
    while True:
            try:
                linhas = int(input(f"Digite o valor da linha. "))
                if linhas <=0:
                    raise ValueError("O valor de linhas precisa ser positivo.")
                break
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")


    return linhas

def ler_coluna():
    while True:
            try:
                colunas = int(input(f"Digite o valor da coluna. "))
                if colunas <0:
                    raise ValueError("O valor de colunas precisa ser positivo.")
                break
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")


    return colunas


def criar_matriz(linhas, colunas):
    matriz = [[random.randint(1, 100) for _ in range(colunas)] for _ in range(linhas)]
    return matriz


# Chamar as funções
num_linhas = ler_linha()
num_colunas = ler_coluna()

matriz_aleatoria = criar_matriz(num_linhas, num_colunas)

# Imprimir a matriz aleatória
print("Matriz Aleatória:")
for linha in matriz_aleatoria:
    print(linha)
