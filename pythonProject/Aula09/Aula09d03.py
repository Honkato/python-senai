# Desafio 3
# Crie duas listas, com 5 valores cada uma.
# Verifique se existe algum número que esteja
# presente nas duas listas e exiba a informação pro
# usuário
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

tupla1 = set(lista1)
tupla2 = set(lista2)

existe = list(tupla1 & tupla2)

if existe != []:
    print("OS SEGUINTES NUMEROS: ",existe)
else:
    print("NÃO HÁ VALORES IGUAIS NA LISTA")
