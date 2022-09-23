lista = []

for x in range(5):
    while True:
        valor = int(input(f'Digite um numero, faltam: {5-x}\n'))
        if not lista.__contains__(valor):
            lista.append(valor)
            break
        else:
            print("POR FAVOR DIGITE UM VALOR NÃO DIGITADO")
    for y in range(len(lista)):
        if valor < lista[y]:
            aux = [valor]
            lista.pop()
            lista = lista[0:y]+aux+lista[y:len(lista)]
            break
    y = 0

print(lista)