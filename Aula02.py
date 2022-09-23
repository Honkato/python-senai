# minhaVariavel = 0
# nome = 'Joao'
#
# minhaVariavel = 5 + 10
#
# # nome = nome + 'Santos'
# # nome += 'Santos'
#
# print(f'O valor da variavel é {minhaVariavel} e o nome é {nome + " Santos"}')
# nome += " Santos"
# # print(f'O valor da variavel é {minhaVariavel} e o nome é {nome + " Santos"}')
#
# entrada = int(input("Digite um numero\n"))
#
# print(f'O valor é {minhaVariavel + entrada}')
#
# sobrenome = input("Digite o sobrenome\n")
#
# print(f'O valor é {nome + " " + sobrenome}')

# TODO               IF
def decisao(e):
    if e == 1 :
        # print("Continua...")
        return True
    elif e == 0 :
        print(f'Encerrou o programa')
        return False
    # else:
    #     print(f'insira apenas 1 ou 0')

def parimpar(par):
    if par % 2 == 0:
        print(f'O numero é par')
    else:
        print(f'O numero é impar')

def validarNumero(num):
    if num.isnumeric():
        return True
    else:
        return False

# # validar se digitou um numero
# if escolha.isnumeric():
#     escolha = int(escolha)
#     Decisao(escolha)
# else:
#     print(f'Você não digitou um numero')
#
# # decisão


#TODO asdasd
armazem = 0
while True:
    escolha = input('Digite um valor diferente de 0 para continuar\n')  # when string   .upper().strip()
    if validarNumero(escolha) == False:
        print('Voce não Digitou um numero')
    else:
        escolha = int(escolha)
        if decisao(escolha) == False:
            break
        if armazem != 0:
            escolha += armazem
            print(f'A soma dos dois numeros é igual a {escolha}')
            escolha = 0
        armazem = escolha
        parimpar(escolha)


        # escolha2 = input('Agora, digite um segundo valor diferente de 0 para continuar\n')
        # escolha2 = int(escolha2)
        # parimpar(escolha2)
        # if decisao(escolha2) == False:
        #     break
        # print(escolha+escolha2)