


while True:
    milhar = input('Digite um numero entre 1000 e 9999: ')
    # ERRO ele vai de qualquer valor se tiver 4 letras
    if len(milhar) == 4:
        break
    else:
        print('POR FAVOR USUARIO NÃO ESTOU AGUENTANDO MAIS ENTRE 1000 E 9999')

# nome é apenas o nome da casa, no final
for i in range(4):
    if i==0:
        nome= 'Milhar: '
    elif i==1:
        nome='Centena: '
    elif i==2:
        nome='Dezena: '
    else:
        nome='Unidade: '
    print(nome +milhar[i])

