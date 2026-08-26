n = int(input())

for case in range(n):
    text = input()

    frequency = {}

    for character in text:
        code = ord(character)

        if code not in frequency:
            frequency[code] = 0

        frequency[code] += 1

    characteres = list(frequency.keys())
    characteres.sort(
        key=lambda code: (frequency[code], -code)
    )

    for code in characteres:
        print(code, frequency[code])

    if case < n-1:
        print()