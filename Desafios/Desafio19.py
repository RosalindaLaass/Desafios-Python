#Para este desafio, crie uma lista com os nomes de três cidades. Peça ao usuário para digitar o nome de uma cidade. 
#Se a cidade estiver na lista, imprima "A cidade está na lista de cidades". Se a cidade não estiver na tupla, imprima "A cidade não está na lista de cidades".
#Obs. Você não pode utilizar list[ ]

cidades = ("Santa Leopoldina", "São Mateus", "Nanuque")

verificaCidade = input("Digite o nome da cidade: ")

if verificaCidade in cidades:
    print("A cidade está na lista de cidades")
else:
    print("A cidade não está na lista de cidades")
