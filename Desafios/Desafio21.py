#Para este desafio, crie dois conjuntos, cada um contendo 5 nomes de seus amigos. Alguns nomes devem estar presentes em ambos os conjuntos.
#Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado.

amigos_um = {'Apoema', "Noemy", "Carol", "Nicoly", "Ferrete"}
amigos_dois = {'Apoema', "Luca", "Noemy", "Gustavo", "Felipe"}

amigos_comuns = amigos_um.intersection(amigos_dois)

print("Nomes que aparecem em ambos os conjuntos:", amigos_comuns)
