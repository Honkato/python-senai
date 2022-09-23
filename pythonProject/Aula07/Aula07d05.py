listaPI = []
listaPar = []
listaImp = []

valor = 1

print("DIGITE QUANTOS NUMEROS QUISER, SE QUISER PARAR DIGITE 0")
while True:
    valor = int(input("Digite um numero: "))
    if valor == 0:
        break
    listaPI.append(valor)
    if not valor % 2:
        listaPar.append(valor)
    else:
        listaImp.append(valor)

print("Lista dos numeros Pares e impares: ",listaPI)
print("Lista dos numeros Pares: ",listaPar)
print("Lista dos numeros Impares: ",listaImp)
