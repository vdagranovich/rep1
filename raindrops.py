def convert(n, res):
    if n % 3 == 0 and res != 'Pling':
        res += 'Pling'
        n = n // 3
        convert(n, res)

    if n % 5 == 0 and res != 'Plang':
        res += 'Plang'
        n = n // 5
        convert(n, res)

    if n % 7 == 0 and res != 'Plong':
        res += 'Plong'
        n = n // 7
        convert(n, res)
    return res

print(convert(int(input()), ''))
