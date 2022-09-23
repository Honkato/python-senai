# Desafio 2
# Crie um set com 5 valores, depois faça uma função que receba esses dados, e
# utilizando o while remova 1 elemento por vez e exiba os itens atuais.
# Todos os itens do set devem ser removidos
def settokaiba(setto):
    while True:
        setto.pop()
        print(setto)
        if setto == set():
            break


if __name__ == '__main__':

    tupla = {1, 2, 3, 4, 5}
    print(tupla)
    setto = set(tupla)
    settokaiba(setto)
