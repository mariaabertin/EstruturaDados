from collections import deque
while True:
    n = int(input())

    if n == 0:
        break
    elif n > 50:
        print("O número precisa ser menor que 50")
        break
    else:
        fila = deque(range(1, n + 1))

        descartadas = []

        while len(fila) > 1:
            descartadas.append(str(fila.popleft()))

            fila.append(fila.popleft())

        print("Discarted cards:", ", ".join(descartadas))
        print("Remaining cards:", fila[0])