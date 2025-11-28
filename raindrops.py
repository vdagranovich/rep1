# n = int(input())
def gett(n, res):
    if n % 3 == 0 and res != 'Pling':
        res += 'Pling'
        n = n // 3
        gett(n, res)

    if n % 5 == 0 and res != 'Plang':
        res += 'Plang'
        n = n // 5
        gett(n, res)

    if n % 7 == 0 and res != 'Plong':
        res += 'Plong'
        n = n // 7
        gett(n, res)
    return res

print(gett(int(input()), ''))
