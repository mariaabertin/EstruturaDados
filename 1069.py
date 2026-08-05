while True:
    try:
        N = int(input())

        for _ in range(N):
            expressao = input()

            pilha = []
            diamantes = 0

            for caractere in expressao:
                if caractere == "<":
                    pilha.append(caractere) 
                elif caractere == ">":
                    if len(pilha) > 0:  
                        pilha.pop()  
                        diamantes += 1 
            print(diamantes)

    except EOFError:
        break