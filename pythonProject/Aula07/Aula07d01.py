#ler 5 valores de uma lista e falar qual é o maior e o menor

# def pegarNumeros():
lista = [0, 0, 0, 0, 0]

menor = 0
maior = 0

for x in range(5):
        lista[x] = int(input(f'Digite o valor do {x+1}º Valor: '))
        if x != 0:
            #TODO VER SE O NUMERO É MENOR
            if lista[x] < menor:
                menor = lista[x]
                menorPosicao = x

            #TODO VER SE O NUMERO É MAIOR
            elif lista[x] > maior:
                maior = lista[x]
                maiorPosicao = x
        else:
            menor = lista[x]
            menorPosicao = x

            maior = lista[x]
            maiorPosicao = x


# if __name__ == '__main__':

print(f'O MENOR NUMERO DIGITADO FOI {menor}, E FOI O {menorPosicao+1}º NUMERO DIGITADO\n')
print(f'O MAIOR NUMERO DIGITADO FOI {maior}, E FOI O {maiorPosicao+1}º NUMERO DIGITADO')