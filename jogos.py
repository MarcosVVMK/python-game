import forca
import advinhacao

print("*********************************")
print("*** Escolha o jogo que deseja ***")
print("*********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual Jogo?"))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Advinhação")
    advinhacao.jogar()