lista = [] #COLCHETES
tupla = (1, 2, 3) #CHAVE: NAO PODE SER ALTERADA
setEXEMPLO = {5, 6, 8} #PARENTESES: USAR COMPARAÇÕES

print(tupla)

numeros = [1, 2, 3, 6]
primeiro = set(numeros)
segundo = {1, 2, 4, 5}
print("Sinal  |  : ",primeiro | segundo) #OBTER TODOS SEM REPETIR UM NUMERO
print("Sinal  &  : ",primeiro & segundo) #TRAZER OS NUMEROS QUE ESTAO PRESENTES NOS 2 SETS
print("Sinal  -  : ",primeiro - segundo)
print("Sinal  -  : ",segundo - primeiro)
print("Sinal  ^  : ",primeiro ^ segundo)
