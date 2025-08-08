# operadores-relacionais

Operadores Relacionais são símbolos usados em diversas linguagens de programação. Assim como na matemática, eles nos permitem realizar testes comparativos, seja entre valores numéricos ou na comparação de textos."

Os operadores usados em Python divergem um pouco dos padrões matemáticos, mas são similares aos operadores utilizados em outras linguagens de programação.

Breve explicação dos Operadores e suas funcionalidades:

* Igualdade ............ ==
* Diferença ............ !=
* Maior ................ >
* Menor ................ <
* Maior ou Igual ....... >=
* Menor ou Igual ....... <=

Dos operadores apresentados acima, os únicos que divergem do padrão matemático são o "==" e "!=".  
"==" - é utilizado para realizar testes de igualdade entre valores numéricos ou textos. ex 5 == 2 ou "Fábrica" == "Python".  
"!=" - é utilizado para realizar testes de diferença entre valores numéricos ou textos. ex 5 != 2 ou "Fábrica" != "Python".   

Nota: Todos os teste relacionais retornaram ao Python apenas 2 tipos de resultados, sendo eles "True" ou "False". Dessa forma os testes relacionais sempre serão utilizados para verificar se algum tipo de comparação é verdadeira "True" ou Falsa "False".

# estruturas condicionais:

Muitas vezes precisamos que nosso código tome decisões. Para isso usamos as estruturas condicionais. Elas permitem que nosso programa execute blocos de código diferentes dependendo se uma condição é verdadeira ou falsa.

Breve explicação das Estruturas Condicionais e suas funcionalidades:

* se ............ if
* senão ......... else
* senão se ...... elif

As estruturas condicionais tem padrões de montagem e precisam ser respeitados para o perfeito funcionamento do código.
Essas estruturas são classificadas em estruturas simples, composta ou encadeadas/aninhadas.

## Estrutura Condicional Simples: if

A estrutura condicional simples é a mais básica. Ela testa uma única condição e executa um bloco de código apenas se essa condição for True.
Se a condição for False, o bloco de código dentro do if é simplesmente ignorado, e a execução do programa continua após ele.
```
# Estrutura padrão:

if condicao:
    Código a ser executado se a condição for True
```
```
# Exemplo:

if idade >= 18:
    print("Você é maior de idade.")
```
## Estrutura Condicional Composta: if e else

A estrutura condicional composta oferece duas opções: um bloco de código para quando a condição é True e outro bloco para quando ela é False.
Isso garante que sempre haverá uma ação a ser executada, independentemente do resultado da condição.
```
# Estrutura padrão:

if condicao:
    Código a ser executado se a condição for True
else:
    Código a ser executado se a condição for False
```
```
# Exemplo:

if temperatura > 30:
    print("Está muito quente! Beba bastante água.")
else:
    print("A temperatura está agradável.")
```
## Estrutura Condicional Encadeada/Aninhada: if, elif e else

Quando é preciso testar múltiplas condições em sequência, a estrutura encadeada (ou aninhada, dependendo da forma como é construída) é a ideal.
Ela usa if para a primeira condição, elif (uma abreviação de "else if") para condições adicionais, e opcionalmente else para um final, caso nenhuma das condições anteriores seja verdadeira.
O Python avalia as condições na ordem em que são montadas e executa o primeiro bloco cujo if ou elif seja True.
```
# Estrutura padrão:

if primeira_condicao:
    Código se a primeira condição for True
elif segunda_condicao:
    Código se a segunda condição for True (e a primeira for False)
elif terceira_condicao:
    Código se a terceira condição for True (e as anteriores forem False)
else:
    Código se nenhuma das condições acima for True
```
```
# Exemplo:

pontuacao = 75

if pontuacao >= 90:
    print("Excelente! Nota A.")
elif pontuacao >= 70:
    print("Muito bom! Nota B.")
elif pontuacao >= 50:
    print("Aprovado! Nota C.")
else:
    print("Reprovado. Precisa estudar mais.")
```
Nota: Os ":" usados na montagem da estrutura condicional tem a função de mostrar ao código que o bloco de execução está sujeito a condição estabelecida em if, else ou elif.
Esse bloco deve conter um recuo aplicando o uso do botão TAB antes do bloco a ser executado, esse recuo recebe o nome de indentação.

## 01.numero_par.py
## 02.numero_impar.py
## 03.par_impar.py
## 04.nota_final.py
## 05.password.py
## 06.mes_correspondente.py
## 07.melhor_desconto.py
## 08.valor_compra.py
## 09.soma_intervalos.py
## 10.peso_ideal.py
## 11.custo_copias.py
## 12.categoria_jogador.py
## 13.condicao_eleitoral.py

