lista = [0, 0, 0, 0, 0]

for x in range(len(lista)):
    while True:
        valor = (input(f'Digite um numero, faltam: {len(lista)-x}\n'))
        if not lista.__contains__(valor):
            lista[x] = valor
            break
        else:
            print("POR FAVOR DIGITE UM VALOR NÃO DIGITADO")


print(sorted(lista, key=int))