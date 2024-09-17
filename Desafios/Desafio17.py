#Para este desafio, crie um loop que peça ao usuário para digitar o nome de uma fruta. Se a fruta digitada não for 'abacate', 
#o loop deve continuar pedindo ao usuário para digitar o nome de uma fruta. Se a fruta for
#'abacate', o loop deve terminar e o programa deve imprimir "Parabéns, você acertou a früta!".

fruta = "Abacate"

while True:
    tentativa = input("Digite o nome da fruta secreta: ")

    if tentativa == fruta:
        print("Parabéns você descobriu")
        break
