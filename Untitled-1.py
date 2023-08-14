print ("JOGO DA FORCA")

palavra = "pedro"
setuppalavra=['_','_','_','_','_']
morto = False
vidas = 3

print(setuppalavra)

while(not morto):
    decida = input("Escolha a opção: '1 - digitar letra' ou '2- chutar palavra ")
    if(decida == "1"):
        chute= input("Digite uma letra: ")
        chute= chute.strip()
        posicao=0
        for letra in palavra:
            if(letra == chute):
                setuppalavra[posicao]=chute
                print("A letra '{}' está na posição '{}'".format(chute,posicao))
                print(setuppalavra)
                
            elif(posicao==4):
                vidas = vidas-1
                print("ERROU: {} vidas".format(vidas))
                break
            posicao = posicao+1
    
    if(vidas == 0):
        morto = True
        print("Faleceu")

    if(decida=="2"):
        chute= input("A palavra é: ")
        if(palavra == chute):
            print("ACERTOUUU")
            break
        else:
            print("MORREU")
            morto = True
print("FIM DE JOGO")

    
