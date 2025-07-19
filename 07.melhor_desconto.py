""" Uma livraria está fazendo uma promoção para pagamento à vista em que o comprador 
pode escolher entre dois critérios de desconto:
 a) Critério A: R$ 0,25 por livro + R$ 7,50 fixo
 b) Critério B: R$ 0,50 por livro + R$ 2,50 fixo
Fazer um programa em que o usuário digite a quantidade de livros que deseja comprar 
e o programa diga qual é a melhor opção de desconto.
"""

print("Melhor desconto na livraria")

# solicitando a quantidade de livros ao usuário
qtd_livros = int(input("Quantidade de livros: "))

# calculando as possibilidades de desconto
desconto_a = 7.5 + (qtd_livros * 0.25)
desconto_b = 2.5 + (qtd_livros * 0.5)

# validando a melhor opção de desconto e apresentando ao usuário
if desconto_a == desconto_b:
  print(f"Critérios A e B oferecem o mesmo desconto de R$ {desconto_a:.2f}")
elif desconto_a > desconto_b:
   print(f"Critério A é a melhor opção com desconto de R$ {desconto_a:.2f}")
else:
    print(f"Critério B é a melhor opção com desconto de R$ {desconto_b:.2f}")
