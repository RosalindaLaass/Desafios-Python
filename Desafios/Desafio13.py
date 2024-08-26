#Para este desafio, crie uma lista de frutas que inclui "maçã" três vezes e outras frutas de sua escolha. Use um loop for para contar quantas vezes
#"maçã" aparece na lista e imprima o resultado.

frutas = ["ameixa", "maçã", "melancia", "laranja", "maçã", "maçã"]

macas = 0

for x in frutas:
    if x == "maçã":
        macas += 1

print(macas)
