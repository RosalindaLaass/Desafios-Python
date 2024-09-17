#Para este desafio, crie uma função que calcule a potência de um número.
#A função deve aceitar dois argumentos: a base e o expoente. No entanto, se o expoente não for 
#fornecido ao chamar a função, ele deve assumir o valor padrão de 2.

def calcula_potencia(base, expoente=2):
    potencia = base ** expoente
    return potencia

base = int(input("Digite a base: "))
expoente_input = input("Digite o expoente (pressione Enter para usar o valor padrão 2): ")

if expoente_input:
    expoente = int(expoente_input)
else:
    expoente = 2

resultado = calcula_potencia(base, expoente)

print("A potência é", resultado)
