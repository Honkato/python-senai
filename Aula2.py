import math


def potenciacao(n1, n2):
    resultado = n1 ** n2
    print("o resultado da potenciação é:", resultado)


def raiz(n1, n2):
    raiz1 = math.sqrt(n1)
    raiz2 = math.sqrt(n2)
    print(f'a raiz de {n1} é {raiz1:.2f}'
          f'\njá a raiz de {n2} é {raiz2:.2f}')


def porcentagem(n1, n2):
    resultado = n1 * (n2/100)
    print(f'\nO {n1} é {resultado}% de{n2}')


opcao = 1

while opcao == opcao:

    opcao = int(input('''Escolha uma opção:
                    [1] Potência
                    [2] Raiz
                    [3] Porcentagem
                    [0] Sair\n'''))

    if 0 < opcao > 4:
        print("\n!!!POR FAVOR DIGITE UMA OPÇÃO VÁLIDA!!!")

    elif opcao == 0:
        print("\nMEU CORAÇÃO NAO SEI PORQUE BATE TAO TRISTE QUANDO DESPEDE. :(")
        break

    else:
        numero = int(input("\nDigite um numero:"))
        numero2 = int(input("\nDigite o segundo numero:"))

        if opcao == 1:
            potenciacao(numero, numero2)

        elif opcao == 2:
            raiz(numero, numero2)

        elif opcao == 3:
            porcentagem(numero, numero2)
