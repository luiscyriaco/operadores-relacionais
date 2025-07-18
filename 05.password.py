""" 05. Escrever um programa que teste se a senha informada é igual a "AC12". 
Se sim, exibir a mensagem "Senha correta" e, se não, exibir "Senha incorreta. """

print("Acesso ao sistema")

# solicitando a senha ao usuário
senha = input("Digite sua senha: ")

# validando senha do usuário
if senha == "AC12":
    print("Senha correta.")
else:
    print("Senha incorreta.")
