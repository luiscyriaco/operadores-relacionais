""" 09. Dados seis números inteiros representando dois intervalos de tempo (horas, minutos, segundos), 
fazer um programa para calcular a soma desses intervalos.
"""

# imprimindo  título do programa
print("Somando dois horários")
print("-"*20)
print("Primeira Hora\n")

# solicitando hora, minuto e segundo do primeiro horário ao usuário
hora_a = int(input("Hora..... "))
minuto_a = int(input("Minuto..... "))
segundo_a = int(input("Segundo..... "))

print("\nSegunda Hora\n")

# solicitando hora, minuto e segundo do segundo horário ao usuário
hora_b = int(input("Hora..... "))
minuto_b= int(input("Minuto..... "))
segundo_b = int(input("Segundo..... "))
 
# somando os dois horários
horas = hora_a + hora_b
minutos = minuto_a + minuto_b
segundos = segundo_a + segundo_b

# corrigindo, se necessário valores maiores que 59 para valores válidos
if segundos > 59:
  minutos = minutos + (segundos // 60)
  segundos = segundos % 60

if minutos > 59:
   horas = horas + (minutos // 60)
   minutos = minutos % 60

if horas > 23:
   dias = (horas // 24)
   horas = horas % 24

# apresentando a soma dos intervalos ao usuário
print(f"\nHora A.............: {hora_a:02d}:{minuto_a:02d}:{segundo_a:02d}")
print(f"Hora B.............: {hora_b:02d}:{minuto_b:02d}:{segundo_b:02d}")
print(f"\nSoma..: {dias:02d} dia(s) e {horas:02d}:{minutos:02d}:{segundos:02d}")
