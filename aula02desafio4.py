n1 = int(input('digite o 1 num\n'))
n2 = n1
n3 = n1
while True:
    if(n2==n1):
        n2 = int(input(f'digite o 2 num (precisa ser diferente de {n1})\n'))
    elif(n3==n1 or n3==n2):
        n3 = int(input(f'digite o 3 num (precisa ser diferente de {n1} e {n2})\n'))
    else:
        break



if n1 > n2 and n1 > n3:
    print(f'Maior numero é o {n1}')
elif n2 > n1 and n2 > n3:
    print(f'Maior numero é o {n2}')
else:
    print(f'Maior numero é o {n3}')


if n3 < n1 and n3 < n2:
    print(f'Menor numero é o {n3}')
elif n2 < n1 and n2 < n3:
    print(f'Menor numero é o {n2}')
else:
    print(f'Menor numero é o {n1}')