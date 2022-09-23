x = int(input('DIGITE UM NUMERO MAIOR QUE 10( SE O NUMERO FOR MENOR, 50 SERA O SETADO COMO PADRÃO)\n'))

if x < 10:
    x=50
for x in range(0,x, 2):
    print(1* x)