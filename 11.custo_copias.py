""" 11. Escrever um programa que resolva o seguinte problema: uma fotocópia custa 
R$ 0,25 por folha, mas acima de 100 folhas esse valor cai para R$ 0,20 por unidade. 
Dado o total de cópias, informe o valor a ser pago.
"""

# imprimindo o título do programa
print("Preço das cópias")

# solicitando ao usuário a quantidade de cópias
copias = int(input("Quantidade de cópias: "))

# apresentando o valor unitário ao usuário de acordo com a quantidade de cópias
if copias > 100:
 custo = copias * 0.2
 print("Custo unitário......: R$ o,20")
else:
   custo = copias * 0.25
   print("Custo unitário......: R$ 0,25")

# apresentando  o total das cópias ao usuário
print(f"Total a pagar.......: R$ {custo:.2f}")
