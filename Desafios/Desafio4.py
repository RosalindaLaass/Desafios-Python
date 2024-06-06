#Neste desafio, quero que você crie um script que solicite ao usuário dois
#números. Em seguida, seu script deve imprimir a soma, a subtração, a
#multiplicação, a divisão (resultado decimal) e a exponenciação (primeiro
#número elevado ao segundo número) desses dois números.

num1 = int(input("Digite um numero: "))
num2 = int(input("Agora outro numero: "))

print(f'{num1 + num2}')
print(f'{num1 - num2}')
print(f'{num1 * num2}')
print(f'{num1 / num2:.1f}')
print(f'{num1 ** num2}')