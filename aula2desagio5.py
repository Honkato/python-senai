n1 = -1

while True:
    if(n1==-1):
        n1 = float(input('Digite o 1 numero'))

    n2 = float(input('Digite o 2 numero'))
    if (n1 > 0 and n2 > 0):
        break
    else:
        print('As notas precisam ser positivas')

nota = ((n1+n2)/2)

if(nota <= 3):
    condicao='Reprovado'
elif(nota <5):
    condicao='Recuperação'
elif(nota < 7):
    condicao='Regular'
else:
    condicao='Aprovado'
print(f'Média {nota}, Você foi {condicao}')
