# import math
#
#
# def ola(parametronome):
#     print(f"\nOla {parametronome}, '-' nossa que nome lindo, enfim")
#
#
# def soma(n1, n2):
#     result = n1 + n2
#     print(f'\no resultado é: {result}')
#
#
# def subtracao(n1, n2):
#     result = n1 - n2
#     print(f'\no resultado é: {result}')
#
#
# def multiplicacao(n1, n2):
#     result = n1 * n2
#     print(f'\no resultado é: {result}')
#
#
# def divisao(n1, n2):
#     if n2 == 0:
#         return print('\nImpossivel Dividir por 0')
#     result = n1 / n2
#     print(f'\no resltado é: {result}')
#
#
# def potenciacao(n1, n2):
#     resultado = n1 ** n2
#     print("o resultado da potenciação é:", resultado)
#
#
# def raiz(n1, n2):
#     raiz1 = math.sqrt(n1)
#     raiz2 = math.sqrt(n2)
#     print(f'a raiz de {n1} é {raiz1:.2f}'
#           f'\njá a raiz de {n2} é {raiz2:.2f}')
#
#
# def porcentagem(n1, n2):
#     resultado = n1 * (n2 / 100)
#     print(f'\nO {n1} é {resultado}% de{n2}')
#
#
# def operacao(v1, v2):
#     if menu == 1:
#         soma(v1, v2)
#
#     elif menu == 2:
#         subtracao(v1, v2)
#
#     elif menu == 3:
#         multiplicacao(v1, v2)
#
#     elif menu == 4:
#         divisao(v1, v2)
#
#     elif menu == 5:
#         potenciacao(v1, v2)
#
#     elif menu == 6:
#         raiz(v1, v2)
#
#     elif menu == 7:
#         porcentagem(v1, v2)
#
#
# nome = input('Digite seu nome: ')
#
# ola(nome)
#
# # TODO PEÇA PARA O USUARIO DIGITAR 2 VALORES
#
# menu = int
#
# while menu != 0:
#     menu = int(input('''\nQuais das seguintes operações deseja fazer?\n
#                      [1]Adição
#                      [2]Subtração
#                      [3]Multiplicação
#                      [4]Divisão
#                      [5]Potênciação
#                      [6]Radiciação
#                      [7]Porcentagem
#                      [0]Caso Deseje Sair :(\n\n'''))
#     if 0 < menu < 7:
#         s1 = int(input('\nDigite o 1 numero: '))
#         s2 = int(input('\nDigite o 2 numero: '))
#         operacao(s1, s2)
#
#     elif menu == 0:
#         print('\nOK TCHAU ENTAO')
#         break
#
#     else:
#         print('!!!OPÇÃO INVALIDA!!!')
