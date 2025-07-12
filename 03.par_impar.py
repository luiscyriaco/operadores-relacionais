""" 03.Utilizando a estrutura condicional composta, verifique se um número é par ou ímpar e escreva na tela a mensagem correspondente, conforme os exercícios 1 e 2.
"""

print("Verificando se o número é par ou ímpar...")

# solicitando um número inteiro ao usuário
numero = int(input("Digite um número: "))

# verificando se o número é par ou ímpar
if numero % 2 == 0:
    print("O número",numero,"é par.")
else:
    print("O número",numero,"é ímpar.")
