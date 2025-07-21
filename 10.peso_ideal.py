""" Elaborar um programa que verifique se o paciente está acima de seu peso ideal de acordo 
com a condição a seguir:
Para homens: (72.7*altura) - 58
Para mulheress: (62.1*altura) - 44.7
"""

# imprimindo título do programa
print("Peso ideal")
print("-"*20)

# solicitando ao usuário sexo, peso e altura 
sexo = input("Sexo [F/M].. ")
altura = float(input("Altura..... "))
peso =  float(input("Peso....... "))

# verificando sexo do usuário
if sexo == "F":
   peso_ideal = (62.1 * altura) - 44.7
else:
   peso_ideal = (72.7 * altura) - 58.0

# apresentando ao usuário seu peso idealF
print(f"Peso ideal. {peso_ideal:.2f}")
if peso == peso_ideal:
   print("Você está no peso ideal.")
elif peso > peso_ideal:
   print("Você está acima do peso ideal.")
else:
   print("Você está abaixo do peso ideal.")
