""" 06. Solicitar ao usuário um número inteiro e exibir o mês correspondente a este 
número, sendo o número 1 o mês de janeiro e 12, o mês de dezembro. Para  valores 
fora da faixa entre 1 e 12, o programa deve informar que não é um mês válido.
"""

print("Nome do mês")

# solicitando número inteiro ao usuário
mes = int(input("Digite um mês: "))

# verificando o nome do mês solicitado pelo usuário
if mes == 1:
   nome_mes = "janeiro"
elif mes == 2:
   nome_mes = "fevereiro"
elif mes == 3:
   nome_mes = "março"
elif mes == 4:
   nome_mes = "abril"
elif mes == 5:
   nome_mes = "maio"
elif mes == 6:
   nome_mes = "junho" 
elif mes == 7:
   nome_mes = "julho"
elif mes == 8:
   nome_mes = "agosto"
elif mes == 9:
   nome_mes = "setembro"
elif mes == 10:
   nome_mes = "outubro"
elif mes == 11:
   nome_mes = "novembro"
elif mes == 12:
   nome_mes = "dezembro"
else:
    nome_mes = "mês inválido"

# apresentando ao usuário o nome do mês
print("mes: ", mes, "=", nome_mes)
