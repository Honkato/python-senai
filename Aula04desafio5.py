

while True:
    numero = input('Digite o seu numero de telefone (XX)XXXXX-XXXX\n')
    # if numero.find("-") >0 :
    numero = numero.replace("-", "")
    numero = numero.replace(" ", "")
    numero = numero.replace("(", "")
    numero = numero.replace(")", "")
    # '19 955551234'
    print(len(numero))
    quant = len(numero)


    if 7 < quant < 12:
        if (quant == 10):
            DDD = numero[:2]
            numero = numero[2:]
            quant = len(numero)
        if(quant == 8):
            numero = '9' + numero
        print('O seu DDD é: ',DDD)
        print('E seu número é: ',numero)
        break
    else:
        print('Por favor digite novamente')