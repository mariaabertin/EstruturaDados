from bisect import bisect_left

caso = 1

while True:
    N, Q = map(int, input().split())

    if N == 0 and Q == 0:
        break

    marmore = []

    for _ in range(N):
        marmore.append(int(input()))

    marmore.sort()

    print(f"CASE# {caso}:")

    for _ in range(Q):
        numero = int(input())

        posicao = bisect_left(marmore, numero)

        if posicao < N and marmore[posicao] == numero:
            print(f"{numero} found at {posicao+1}")
        else:
            print(f"{numero} not found")

    caso += 1