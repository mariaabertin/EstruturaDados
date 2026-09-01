caso = 1

while True:
    N = int(input())

    if N == 0:
        break

    consumo = {}

    totalPessoas = 0
    totalConsumo = 0

    for _ in range(N):
        pessoas, quantidade = map(int, input().split())

        totalPessoas += pessoas
        totalConsumo += quantidade

        consumoPessoa = quantidade // pessoas

        consumo[consumoPessoa] = consumo.get(consumoPessoa, 0) + pessoas

    valores = sorted(consumo.items())

    print(f"Cidade# {caso}:")

    resultado = []

    for consumoMedio, pessoas in valores:
        resultado.append(f"{pessoas}-{consumoMedio}")

    print(" ".join(resultado))

    media = totalConsumo // totalPessoas
    print(f"Consumo médio: {media:.2f} m3.")

    print()

    caso += 1