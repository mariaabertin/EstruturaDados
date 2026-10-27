fila = []
historico = []

while True:
    try:
        chamado = int(input("Digite o código (-1 para encerrar a entrada): "))

        if chamado == -1:
            break
        elif chamado < 0:
            print("Chamado invalido")
        elif chamado in fila:
            print("Chamado duplicado")
        else:
            fila.append(chamado)
    except ValueError:
        print("Chamado invalido")

while True:
    try:
        print("\nEscolha uma operação:")
        print("1 - Processar próximo chamado")
        print("2 - Consultar código com busca binária")
        print("3 - Desfazer último processamento")
        print("4 - Exibir fila atual")
        print("5 - Exibir histórico")
        print("0 - Encerrar programa")

        escolha = int(input("Opção: "))

        if escolha == 0:
            print("Programa encerrado.")
            break

        elif escolha == 1:
            if not fila:
                print("Fila vazia.")
            else:
                chamado_processado = fila.pop(0)
                historico.append(chamado_processado)
                print(f"Chamado processado: {chamado_processado}")

        elif escolha == 2:
            if not fila:
                print("Nao ha codigo para pesquisar")
            else:
                copia_ordenada = fila[:]
                for i in range(len(copia_ordenada)):
                    for j in range(0, len(copia_ordenada) - i - 1):
                        if copia_ordenada[j] > copia_ordenada[j + 1]:
                            copia_ordenada[j], copia_ordenada[j + 1] = copia_ordenada[j + 1], copia_ordenada[j]

                codigo_pesquisa = int(input("Digite o código para pesquisa: "))
                inicio = 0
                fim = len(copia_ordenada) - 1
                encontrado = False

                while inicio <= fim:
                    meio = (inicio + fim) // 2
                    if copia_ordenada[meio] == codigo_pesquisa:
                        encontrado = True
                        break
                    elif copia_ordenada[meio] < codigo_pesquisa:
                        inicio = meio + 1
                    else:
                        fim = meio - 1

                if encontrado:
                    print("Código encontrado.")
                else:
                    print("Código não encontrado.")

        elif escolha == 3:
            if not historico:
                print("Nao ha processamento para desfazer")
            else:
                ultimo = historico.pop()
                fila.insert(0, ultimo)
                print(f"Último processamento desfeito: {ultimo}")

        elif escolha == 4:
            print(f"Fila atual: {fila}")

        elif escolha == 5:
            print(f"Histórico: {historico}")

        else:
            print("Opção inválida")

    except ValueError:
        print("Opção inválida")
