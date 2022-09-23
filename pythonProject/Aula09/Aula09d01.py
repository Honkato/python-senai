# Desafio 1
# Considere que você possui 2 listas com os seguintes valores:
# lista1 = [28, 34, 55, 41, 9, 71]
# lista2 = [9, 31, 44, 74, 28, 56]
# Determine:
# Os valores “ausentes” na lista 2 em comparação com a lista 1
# Os valores “ausentes” na lista 1 em comparação com a lista 2
# Uma lista composta pelos valores únicos existentes na lista1 e lista2
# Uma nova lista que mostre apenas os valores presentes em ambas as listas

lista1 = [28, 34, 55, 41, 9, 71]
lista2 = [9, 31, 44, 74, 28, 56]

tupla1 = set(lista1)
tupla2 = set(lista2)

print("VALORES DA L1 QUE FALTAM NA L2:      ",tupla1 - tupla2)
print("VALORES DA L2 QUE FALTAM NA L1:      ",tupla2 - tupla1)
print("VALORES UNICOS EM CADA:              ",tupla1 ^ tupla2)
print("APENAS VALORES PRESENTES EM AMBAS:   ",tupla1 & tupla2)