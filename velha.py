import random, sys

def verifica_jogo(pos,simbolo):
    global primeiro,segundo,terceiro,quarto,quinto,sexto,setimo,oitavo,nono,jogada_valida
    
    if pos == "1" and primeiro == "_" :
        primeiro = simbolo
        jogada_valida = True
    elif pos == "2" and segundo == "_" :            
        segundo = simbolo
        jogada_valida = True
    elif pos == "3" and terceiro == "_" :
        terceiro =simbolo
        jogada_valida = True
    elif pos == "4" and quarto == "_" :        
        quarto =simbolo
        jogada_valida = True
    elif pos == "5" and quinto == "_" :    
        quinto =simbolo
        jogada_valida = True
    elif pos == "6" and sexto == "_" :   
        sexto =simbolo
        jogada_valida = True
    elif pos == "7" and setimo == " " :   
        setimo =simbolo      
        jogada_valida = True
    elif pos == "8" and oitavo == " " :
        oitavo=simbolo
        jogada_valida = True
    elif pos == "9" and nono == " " :
        nono =simbolo
        jogada_valida = True

def verifica_vencedor(jogador,simbolo):
    resultado = False
    if primeiro == quarto == setimo == simbolo:
        print ("O jogador",jogador,"ganhou!!!")
        resultado = True
    if terceiro == sexto == nono == simbolo:
        print ("O jogador",jogador,"ganhou!!!")
        resultado = True
    if primeiro == segundo ==  terceiro == simbolo:
        print ("O jogador",jogador,"ganhou!!!")
        resultado = True
    if setimo == oitavo == nono == simbolo:
        print ("O jogador",jogador,"ganhou!!!")
        resultado = True
    if primeiro == quinto == nono == simbolo:
        print ("O jogador",jogador,"ganhou!!!")
        resultado = True
    if terceiro == quinto == setimo == simbolo:
        print ("O jogador",jogador," ganhou!!!")
        resultado = True
    if segundo == quinto == oitavo == simbolo:
        print ("O jogador",jogador,"ganhou!!!")
        resultado = True
    if resultado:
        return jogador

def velha():
    global primeiro,segundo,terceiro,quarto,quinto,sexto,setimo,oitavo,nono,jogada_valida
    jogo = True
    while jogo == True:       

        primeiro = segundo = terceiro = quarto = quinto = sexto = "_" 
        setimo = oitavo = nono = " "
        def imprime_jogo_da_velha():
        #Imprime as variveis correspondentes ao espaco do jogo da velha.
            print (primeiro,"|",segundo,"|",terceiro)
            print (quarto,"|",quinto,"|",sexto)
            print (setimo,"|",oitavo,"|",nono)
            return

        print("\n\n Se chegou nessa fase algo bom você não fez, resolva essa velha e seja feliz outra vez... \n \t Convide um amigo e trace uma estratégia, se for bom o suficiente será uma Vitória-Régia. (Era só pra rimar, rsrs) \n \t\t DICA: CUIDADO COM A VELHAAAAA! \n\n")
        nome_jogador1 = input("Informe o nome do primeiro jogador: ").upper()
        nome_jogador2 = input("Informe o nome do segundo jogador: ").upper()

        print("Pra jogar informe o numero correspondente ao local desejado. Consulte a tabela abaixo")
        print("        _|_|_            1|2|3")
        print("        _|_|_            4|5|6")
        print("         | |             7|8|9")


        resultado = False
        numero_de_jogadas = 0
        while resultado == False:

            jogada_valida = False
            while jogada_valida == False and resultado == False:
                print("Por favor,", nome_jogador1," escolha uma posicao valida: ")
                posicao = input()

                verifica_jogo(posicao,"X")
                if jogada_valida == True: 
                    imprime_jogo_da_velha()
                if(verifica_vencedor(nome_jogador1,"X") == nome_jogador1):
                    return True


            numero_de_jogadas+=1   
            if numero_de_jogadas == 9 and resultado ==False:
                print ("Deu velha")
                resultado = 2
                return False

            jogada_valida = False
            while jogada_valida == False and resultado == False:
                print ("Por favor,", nome_jogador2," escolha uma posicao valida: ")
                #Recebe a posicao jogada
                posicao = input()
                verifica_jogo(posicao,"O")
                if jogada_valida == True: 
                    imprime_jogo_da_velha()
                if(verifica_vencedor(nome_jogador2,"O") == nome_jogador2):
                    return False
            
            numero_de_jogadas+=1

velha()