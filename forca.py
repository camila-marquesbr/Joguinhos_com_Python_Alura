def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    #enquanto não enforcou E não acertou
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")

        index = 0
        for letra in palavra_secreta:
            if(chute ==letra):
                print("Encontrei a letra {} na posição".format(letra, index))
            index = index + 1
        print("joando...")




    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()