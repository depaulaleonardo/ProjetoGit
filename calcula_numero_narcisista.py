#Um número narcisista (ou número de Armstrong)
#é um número positivo que é a soma de seus próprios dígitos,
#elevado à potência do número de dígitos em uma determinada base.
#Neste desafio nos restringiremos ao decimal (base 10).

#Por exemplo, pegue 153 (3 dígitos), que é narcisista:
#    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic( value ):
    num_digits = len(str(value))
    result = sum(int(digit) ** num_digits for digit in str(value))
    return result == value 

#Exemplo:
number = 153
result = narcissistic(number)
print(f"Número: {number}")
print(f"O resultado do número narcisista é: {result}")