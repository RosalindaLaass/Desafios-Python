#Para este desafio, crie uma função lambda que eleve um número ao quadrado. Em seguida, use essa fúnção 
#para calcular o quadrado de todos os números em uma lista usando um loop for.

quadrado = lambda x: x ** 2

numeros = [1, 2, 3, 4, 5]

quadrados = [quadrado(num) for num in numeros]

print("Os quadrados dos números são:", quadrados)
