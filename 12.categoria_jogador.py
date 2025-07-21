""" 12. Escrever um programa que informe a categoria de um jogador de futebol, considerando sua idade:
Infanil: até 13 anos
Juvenil: até 17 anos
Sênior: acima de 17 anos
"""
# imprimindo título do programa
print("Categoria esportiva\n")

# solicitando idade do jogador
idade = int(input("Idade do(a) atleta: "))

# verificando categoria do jogador segundo a idade
if idade <= 13:
  categoria = "infantil"
elif idade <= 17:
  categoria = "juvenil"
else:
  categoria = "sênior"

# apresentando categoria do jogador
print(f"\nCategoria.........: {categoria}")
