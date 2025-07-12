""" 01. Utilizando a estrututa condicional simples, verifique se um número é par e, caso seja,
escreva na tela "o número é par"
"""

print("Verificando se o número é par...")

# solicitando um número inteiro ao usuário
numero = int(input("Digite um número: "))

# verificando se o número é par
if numero % 2 == 0:
    print("O número",numero,"é par")
