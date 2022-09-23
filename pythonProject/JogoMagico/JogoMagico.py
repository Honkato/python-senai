


def vencedor(velha):
    l1 = velha[0]
    l2 = velha[1]
    l3 = velha[2]
    c1 = [velha[0][0], velha[1][0], velha[2][0]]
    c2 = [velha[0][1], velha[1][1], velha[2][1]]
    c3 = [velha[0][2], velha[1][2], velha[2][2]]
    d1 = [velha[0][0], velha[1][1], velha[2][2]]
    d2 = [velha[0][2], velha[1][1], velha[2][0]]
    tudo = [l1,l2,l3,c1,c2,c3,d1,d2]
    resto = 0

    for x in range(0, len(tudo)):
        print(tudo[x])
        if tudo[x] == [1, 1, 1]:
            print('JOGADOR 1 GANHOU')
            break

        elif tudo[x] == [1, 1, 1]:
            print('JOGADOR 2 GANHOU')
            break

        for y in range(0,3):
            print(tudo[x][y])
            if tudo[x][y] != 1:
                if tudo[x][y] != 0:
                    resto = 1
    if resto == 0:
        print("iiiiiiii deu velha hahaha muito ruim voces")

def jogadorX(velha):
    # marcador = 'X'
    # while marcador != 'p':
    #     marcar = int(input("DIGITE ONDE DESEJA MARCAR"))
    #     if nao marcado:
    #         velha[0][0] = marcador
    #         if marcador == 'X':
    #             marcador = 'O'
    #         else:
    #             marcador = 'p'
    pass

def convert(velha):
    jogo = str(velha)
    jogo = jogo.replace('[', '\n')
    jogo = jogo.replace(']', '')
    jogo = jogo.replace(',', '')
    jogo = jogo.replace('0', '')
    jogo = jogo.replace("'", '')

    print(jogo)


if __name__ == '__main__':
    velhaL1 = [[10, 20, 30],
               [40, 50, 60],
               [70, 80, 90]]
    print(velhaL1[0])
    # velhaL1[0][0] = 1
    # print(velhaL1[0])
    while True:
        jogadorX(velhaL1)
        vencedor(velhaL1)
        convert(velhaL1)
