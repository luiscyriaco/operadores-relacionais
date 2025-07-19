""" 08. Considerar a situção em que um cliente faz uma determinada compra em uma loja. 
Ao realizar o pagamento, são oferecidas as seguintes condições para pagamento:
- Pagamento à vista: 15% de desconto sobre o valor total da compra.
- Pagamento com cheque pré-datado para 30 dias: 10% de desconto sobre o valor total da compra.
- Pagamento parcelado em 3 vezes: 5% de desconto sobre o valor total da compra.
- Pagamento parcelado em 6 vezes: não tem desconto.
- Pagamento parcelado em 12 vezes: 8% de acréscimo sobre o valor total da compra.
De acordo com o valor total da compra, verificar a opção de pagamento do cliente, 
calcular também o valor das parcelas. Apresentar ao usuário uma mensagem com o valor total da 
compra a, o valor final da compra, a diferença entre os dois, identificar como desconto se a 
diferença for positiva, como juros se for negativa, mostrar, também, a quantidade e o valor das parcelas.
"""

# apresentando ao usuário as opções de pagamento da compra
print("     PAGAMENTO DE COMPRA")
print("-" * 30)
print("     Formas de Pagamento\n")
print("    1. Pagamento a vista")
print("    2. Cheque pré 30 dias")
print("    3. Parcelado em  3x")
print("    4. Parcelado em  6x")
print("    5. Parcelado em 12x")
print("-" * 30)
print("     Dados da Compra\n")

# solicitando o valor total da compra e a forma de pagamento ao usuário
valor_total = float(input("Valor total ....... R$ "))
forma_pgto = int(input("Forma de pagamento: .. "))

# Verifica se a forma de pagamento está entre 1 e 5
# Se não estiver, ajusta para 1
if forma_pgto < 1 or forma_pgto > 5:
  forma_pgto = 1

# validando valor líquido e quantidade de parcelas segundo a forma de pagamento
if forma_pgto == 1:
   valor_liquido = valor_total * 0.85
   qtd_parcelas = 0
elif forma_pgto == 2:
    valor_liquido = valor_total * 0.9
    qtd_parcelas = 0
elif forma_pgto == 3:
   valor_liquido = valor_total * 0.95
   qtd_parcelas = 3
elif forma_pgto == 4:
   valor_liquido = valor_total
   qtd_parcelas = 6
elif forma_pgto == 5:
   valor_liquido = valor_total * 1.08
   qtd_parcelas = 12

# apresentando valor total, valor líquido, valor diferença, quantidade parcelas e valor parcelas ao usuário
print("-" * 30)
print("     Dados do pagamento\n")
print(f"Valor total...... R$ {valor_total:.2f}")
print(f"Valor líquido.... R$ {valor_liquido:.2f}")

# calculando a diferença entre o valor total e o valor líquido
diferenca = valor_total - valor_liquido

# apresentando juros ou desconto ao usuário
if diferenca != 0.0:
    if diferenca < 0.0:
        diferenca = diferenca * -1
        print(f"Diferença.... R$ {diferenca:.2f} de juros")
    else:
        print(f"Diferença.... R$ {diferenca:.2f} de desconto")

# calculando valor das parcelas, apresentando ao usuário quantidade de parcelas e seus valores
if qtd_parcelas > 0:
   valor_parcela = valor_liquido / qtd_parcelas
   print(f"{qtd_parcelas} parcelas de R$ {valor_parcela:.2f}\n")
         
