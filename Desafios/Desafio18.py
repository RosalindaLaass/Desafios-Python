#Para este desafio, crie uma lista de números de 1 a 10. Use um 'for loop' para iterar sobre a lista. 
#Se o número atual da iteração for par, imprima "O número [número] é par". Se o número for ímpar, imprima "O número [número] é impar".

numeros = [1,2,3,4,5,6,7,8,9,10]

for numeros in numeros:
    if numeros%2 == 0:
        print("O número",numeros,"é par")

    else:
        print("O número",numeros,"é impar")