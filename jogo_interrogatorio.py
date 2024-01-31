"""
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime. As perguntas são:
 - "Telefonou para a vítima?"
 - "Esteve no local do crime?"
 - "Mora perto da vítima?"
 - “Tinha dívidas com a vítima?"
 - "Já trabalhou com a vítima?“
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como
"Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente"
"""
lista = ['Telefonou para a vítima?',
         'Esteve no local do crime?',
         'Mora perto da vítima?',
         'Tinha dívidas com a vítima?',
         'Já trabalhou com a vítima?']

def realizar_perguntas():
    try:
        while True:
            try: 
                respostas_positivas = 0
                for pergunta in lista: 
                    while True:
                        resposta = input (pergunta + "(sim / não): ").lower()

                        if resposta == "sim" or resposta == "não":
                            break
                        else:
                            print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

                if resposta == "sim":
                    respostas_positivas += 1
    
                if respostas_positivas ==2:
                    print("Suspeita")

                elif respostas_positivas <=4:
                    print("Cúmplice")

                elif respostas_positivas == 5:
                    print('Assassino')
                else:
                    print("Inocente") 
        
            except ValueError as ve:
                print("Erro: A nota deve ser um valor numérico. Tente novamente"
              f"{ve}. Tente novamente")
                
    except KeyboardInterrupt:
        print("\nEncerrando o programa.")

# Chamando a função para realizar as perguntas
realizar_perguntas()