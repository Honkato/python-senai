maior = 0
for i in range(5):
    data = int(input('Digite uma data seu ano de nascimento: '))
    if 2022-data >= 18:
        maior += 1
print(f'DOS 5, {maior} SÃO MAIORES DE IDADE')