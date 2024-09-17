#Para este desafio, crie uma função lambda que aceite um número e retorne o cubo desse número.

cubo = lambda x: x ** 3

numero = int(input("Digite um número: "))

resultado = cubo(numero)
print("O cubo de", numero, "é", resultado)
