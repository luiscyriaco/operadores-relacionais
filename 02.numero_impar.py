""" 02. Utilizando a estrutura condicional simples, verifique se um número é ímpar 
e, caso seja, escreva na tela "o número é ímpar".
"""

print("Verificando se o número é ímpar...")

# solicitando um número inteiro ao usuário
numero = int(input("Digite um número: "))

# verificando se o número é ímpar
if numero % 2 != 0:
    print("O número",numero,"é ímpar")
