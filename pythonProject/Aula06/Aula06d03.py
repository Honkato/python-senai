soma =0
for i in range(6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
print(soma)