import random
from time import sleep

def verifynum(num):
    if num.isnumeric():
        return True
    else:
        return False
def decisao(e):
    if e == 1 :
        # print("Continua...")
        return True
    elif e == 0 :
        print(f'POPOPOPOPOPOPOPOOOO')
        return False

#     Inicio do codigo
tentar = 'a'
while True:

 ran = random.randint(0,5)
 tentar = int(input('0 a 5 digita pls'))
 print('Aguarde um momento to checando')
 sleep(5)
 print('...')
 sleep(20)
 if ran==tentar:
     print('u-u')
 else:
     print(f'nono jo pensei {ran}')

    # if tentar == 1:
    #     ran = random.randint(1, 5)
    #     tentar = input('Tenta a sorte irmao')
    #     print(ran)
    #
    # if verifynum(tentar) == False:
    #     print('!!!Digita direito!!!')
    # else:
    #     print('Boa tarde, gostaria de tentar ler minha mente?')
    #     tentar = input('Digite 1 para tentar e 0 para ser um frangote\n')
    #     tentar = int(tentar)
    #     if decisao(tentar) == False:
    #         break
