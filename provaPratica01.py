fila = []

while True:
    try:
        codigo = int(input("Digite o código (0 para encerrar): "))

        if codigo == 0:
            break
        elif codigo < 0:
            print("Codigo invalido")
        elif codigo in fila:
            print("Codigo duplicado")
        else:
            fila.append(codigo)
    except ValueError:
        print("Codigo invalido")

if not fila:
    print("Codigos ordenados: ", fila)
    print("Nao ha codigo para pesquisar")
    print("Ordem de processamento: ", fila)
    print("Pilha vazia")
    raise SystemExit

# Ordenar em ordem crescente
codigo_ordenado = fila[:]
for i in range(len(codigo_ordenado)):
    for j in range(0, len(codigo_ordenado) - i - 1):
        if codigo_ordenado[j] > codigo_ordenado[j + 1]:
            codigo_ordenado[j], codigo_ordenado[j + 1] = codigo_ordenado[j + 1], codigo_ordenado[j]

print(f"Codigos ordenados: {codigo_ordenado}")

# Busca binária
codigo_pesquisa = int(input("Codigo para pesquisa: "))
inicio = 0
fim = len(codigo_ordenado) - 1
encontrado = False
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if codigo_ordenado[meio] == codigo_pesquisa:
        encontrado = True
        posicao = meio
        break
    elif codigo_ordenado[meio] < codigo_pesquisa:
        inicio = meio + 1
    else:
        fim = meio - 1

if encontrado:
    print(f"Código encontrado.")
else:
    print("Código não encontrado.")

# Processar a fila na ordem de chegada
ordem_processamento = []
historico = []
while fila:
    codigo_processado = fila.pop(0)
    ordem_processamento.append(codigo_processado)
    historico.append(codigo_processado)

print(f"Ordem de processamento {ordem_processamento}")
print(f"Histórico inverso {historico[::-1]}")