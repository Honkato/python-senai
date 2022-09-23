#
# lista = ['a','b','b','b','b','b','c']
# print(lista)
#
# lista.append('d')
# print(lista)
#
# lista.insert(0,'0')
# print(lista)
#
# lista.pop()
# print(lista)
#
# lista.remove('b')
# print(lista)
#
# del lista[0]
#
# print(lista)

lista = [1,2,3,4,5,6,999]
lista.sort(reverse=True)
print(lista)

primeiro, *resto, ultimo = lista
print(primeiro)
print(resto)
print(ultimo)

lista1 = [2, 4, 9]
lista2 = lista1
lista3 = lista1[:]
lista2[1] = 20

print(lista1)
print(lista2)
print(lista3)

mais = 0
menos = -1
sinal = -2
# VERIFICA SE O EXISTE '+' OU '-', (CASO SEJA -1 NÃO EXISTE)
if mais== -1:
    mais = menos +1
if menos== -1:
    menos = mais +1

if mais < menos:
    print("mais")
    sinal = mais

if menos < mais:
    print("menos")
    sinal = menos

print("SINAL AKIO: ",sinal)