from math import gcd

N = int(input())

for _ in range (N):
    N1, _, D1, operador, N2, _, D2 = input().split()

    N1 = int(N1)
    D1 = int(D1)
    N2 = int(N2)
    D2 = int(D2)

    if operador == '+':
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif operador == '-':
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    elif operador == '*':
        numerador = N1 * N2
        denominador = D1 * D2
    else:
        numerador = N1 * D2
        denominador = D1 * N2

    originalNumerador = numerador
    originalDenominador = denominador

    divisor = gcd(
        abs(numerador), 
        abs(denominador)
    )

    numerador //= divisor
    denominador //= divisor

    if denominador < 0:
        numerador *= -1
        denominador *= -1

    print(f"{originalNumerador}/{originalDenominador} = {numerador}/{denominador}")