""" 04. Em uma escola, as notas de cada prova variam de 0 a 100. Para o cálculo 
da média do semestre, o aluno precisa fazer três provas. Fazer um programa que 
solicite o valor de cada prova, calcule a média aritmética delas e mostre se ele 
foi aprovado ou reprovado. Para ser aprovado, a média deve ser igual ou maior do que 50.

Média = (Prova1 + Prova2 + Prova3) / 3.
"""

print("Aprovado ou Reprovado...")
# solicitando as notas das provas ao usuário
p1 = float(input("Digite a nota da Prova 1: "))
p2 = float(input("Digite a nota da Prova 2: "))     
p3 = float(input("Digite a nota da Prova 3: "))
 
# calculando a média
media = (p1 + p2 + p3) / 3

# verificando se o aluno foi aprovado ou reprovado
print("A média é:", media)
if media >= 50:
    print("Aprovado")
else:
    print("Reprovado")
