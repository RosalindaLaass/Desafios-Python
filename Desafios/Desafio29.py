#Para este desafio, crie uma função lambda que aceite um número e retorne "Par" se o número for par e "impar" se o número for ímpar.

verificar_paridade = lambda x: "Par" if x % 2 == 0 else "Ímpar"

numero = int(input("Digite um número: "))

resultado = verificar_paridade(numero)

print("O número", numero, "é", resultado)
