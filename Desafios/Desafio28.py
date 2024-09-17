#Para este desafio, crie uma função lambda que aceite dois números e retorne a multiplicação desses números.

multiplicacao = lambda x, y: x * y

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = multiplicacao(numero1, numero2)
print("A multiplicação de", numero1, "e", numero2, "é", resultado)
