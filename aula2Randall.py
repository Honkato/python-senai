import random

#TODO SORTEAR UM NUMERO
# ADICIONAR O NUMERO NUMA LISTA/ARRAY
# VERIFICAR SE ELE É REPETIDO, SE SIM, SORTEAR OUTRO

lista = []

for i in range(0, 6): #colocar um while para sortear ATE que se tenha 6, e o valor nao seja repetido while len(lista) < 6: codigo...
        aleatorio = random.randint(1, 60)
        n1 = aleatorio
        if n1 in lista: #retirar para colocar o while
            aleatorio = random.randint(1, 60)
            n1 = aleatorio
            lista.append(n1)
        else:
            lista.append(n1)

print(lista)

# print(r1,r2, r3, r4, r5, r6,'\n Esses são seus numeros da sorte')
#
# while True:
#     # input('Aperte enter para continuar')
#
sortear = random.randint(1, 60)
#
#     print(sortear)
#
#     if sortear == r1:
#         print('VOCE ACERTOU')
#         r1 = 61
#     if sortear == r2:
#         print('VOCE ACERTOU')
#         r2 = 61
#     if sortear == r3:
#         print('VOCE ACERTOU')
#         r3 = 61
#     if sortear == r4:
#         print('VOCE ACERTOU')
#         r4 = 61
#     if sortear == r5:
#         print('VOCE ACERTOU')
#         r5 = 61
# if sortear == lista.__getitem__(6):
#     print('VOCE ACERTOU')
#     lista[6]= 61
#

     # if lista [61, 61, 61, 61, 61, 61]:
     #    print('PARA bENS VOCE GANHOU')
     #    break