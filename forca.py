import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("bd_palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    aux = random.randrange(0, len(palavras))

    palavra_secreta = palavras[aux].upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    print("Fim do jogo")
    if not acertou:
        print("A palavra era: ", palavra_secreta)
    else:
        print("Você acertou a palavra secreta!")


if __name__ == "__main__":
    jogar()
