nome = input('digite seu nome: ')

print(nome.upper())
print(nome.lower())


print(len(nome))
nomeesp = nome.replace(' ', '')
print(len(nomeesp))

nome1 = nome.find(' ')
print(nome1)

print(nome[:nome1])