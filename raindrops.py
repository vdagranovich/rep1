def convert(number):
    res = ''
    if number % 3 == 0 and res != 'Pling':
        res += 'Pling'
        number = number // 3
        convert(number)

    if number % 5 == 0 and res != 'Plang':
        res += 'Plang'
        number = number // 5
        convert(number)

    if number % 7 == 0 and res != 'Plong':
        res += 'Plong'
        number = number // 7
        convert(number)
    else:
        if res == '':
            return str(number)
    return str(res)
    

print(convert(int(input())))
