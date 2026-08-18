while True:
    try:
        n = int(input())
    except EOFError:
        break

    numero = []

    for _ in range(n):
        numero.append(input().strip())

    numero.sort()

    economia = 0

    for i in range(1, n):
        anterior = numero[i - 1]
        atual = numero[i]

        J = 0 

        while J < len(atual) and atual[J] == anterior[J]:
            J += 1

        economia += J

    print(economia)