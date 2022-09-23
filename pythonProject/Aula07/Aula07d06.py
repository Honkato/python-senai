import random
lista = []
maximo = int(input("Quantos jogos voce quer?"))
x = 0
print(f"\nOOK ENTAO SERÃO {x}\n")
while maximo > x:
    alea = random.randint(1, 60)
    if lista.__contains__(alea):
        alea = random.randint(1, 60)
    else:
        lista.append(alea)
    if len(lista) == 6:
        print(lista)
        lista.clear()
        x = x + 1
