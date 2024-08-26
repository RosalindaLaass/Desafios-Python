#Para este desafio, crie uma lista de frutas e outra de vegetais. Use um "for loop" aninhado (Nested for loop) para imprimir todas as combinações
#possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo.

frutas = ["maçã", "morango", "manga", "uva", "abacaxi"]
vegetais = ["cenoura", "beterraba", "abobrinha", "jiló", "brócolis"]

for x in frutas:
  for y in vegetais:
    print (x,y)
