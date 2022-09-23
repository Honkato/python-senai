
x = int(input("DIGITE UM NUMERO PARA SER MULTIPLICADO\n"))
y = int(input("AGORA DIGITE A QUANTIDADE DE VEZES EM QUE ELE SERA MULTIPLICADO:\n"))

for i in range(y+1):
    print(f'O resultado de {x} * {i} é {x*i}')
