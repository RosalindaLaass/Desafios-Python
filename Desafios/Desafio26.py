#Para este desafio, crie duas funções. A primeira função deve aceitar um número e retornar o dobro desse número. 
#A segunda função deve aceitar um número e retornar o quadrado desse número. Em seguida, chame a primeira 
#função dentro da segunda para retornar o quadrado do dobro de um número.

def dobro(numero):
    return 2 * numero

def quadrado(numero):
    dobro_numero = dobro(numero)
    return dobro_numero ** 2

numero = int(input("Digite um número: "))

resultado = quadrado(numero)
print("O quadrado do dobro de", numero, "é", resultado)
