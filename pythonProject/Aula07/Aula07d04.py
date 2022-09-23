lista = []
valor = 1
x = 0
cinco = "não "

print("\nOLÁ, TUDO BEM? POR FAVOR DIGITE QUANTOS NUMEROS QUISER, SE QUISER PARAR DIGITE 0\n")

while valor != 0:
    if valor < 0:
        break
    y = 0
    while True:
        valor = int(input(f'Digite um numero, você digitou: {x} numeros\n'))
        if lista.__contains__(valor):
            print("POR FAVOR DIGITE UM VALOR NÃO DIGITADO")
        elif valor == 0:
            break
        else:
            lista.append(valor)
            x = x + 1

            for y in range(len(lista)):
                if valor < lista[y]:
                    aux = [valor]
                    lista.pop()
                    lista = lista[0:y]+aux+lista[y:len(lista)]
                    break

if lista.__contains__(5):
    cinco = ""
lista.sort(reverse=True)
print(f"\nForam digitados {x} numeros")
print(f"\nOs numeros digitador foram {lista}")
print(f"\nO numero 5 {cinco}apareceu")

