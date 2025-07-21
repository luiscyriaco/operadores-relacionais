""" 13. Escrever um programa que solicite a idade do usuário e exiba sua condição eleitoral:
# Entre 16 e 17 anos: voto opcional.
# Entre 18 e 70 anos: voto obrigatório.
# Acima de 70 anos: voto opcional.
"""

# imprmindo título do programa
print("Situação eleitoral\n")   

# solicitando a idade do usuário
idade = int(input("Insira sua idade: "))

# definindo a situação eleitoral
situacao = "Indefinida"

if idade >= 16:
    if idade <= 17:
      situacao = "Voto opcional"
    elif idade <= 70:
        situacao = "Voto obrigatório"
    else:
         situacao <- "Voto opcional"

# imprimindo a situação eleitoral do usuário
print(f"\nSituação.: {situacao}")
