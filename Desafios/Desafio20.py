#Para este desafio, crie uma lista com 5 nomes de países e as capitais desses países. Peça ao usuário para digitar o nome de um país. 
#Se o país estiver na lista, imprima "A capital de [país] é [capital]". Se o país não estiver na lista, imprima 
#"Desculpe, não temos informações sobre a capital desse país".

capitais = {
    "Brasil": "Brasília",
    "Chile": "Santiago",
    "Colômbia": "Bogotá",
    "Cuba": "Havana",
    "Peru": "Lima"
}

pais = input("Digite o nome de um país: ")

if pais in capitais:
    print(f"A capital de {pais} é {capitais[pais]}")
    
else:
    print("Desculpe, não temos informações sobre a capital desse país")
