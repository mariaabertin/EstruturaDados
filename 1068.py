while True:
    try:
        expressao = input()

        pilha = []
        correta = True

        for caractere in expressao:
            if caractere == "(":
                pilha.append(caractere) #append é a fixação da informação
            elif caractere == ")":
                if len(pilha) == 0: #len é contagem
                    correta = False
                    break
                pilha.pop()

        if correta and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break
