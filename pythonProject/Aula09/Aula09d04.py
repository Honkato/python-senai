# Considere a frase:
# “Esse é um teste para medir meus conhecimentos em python”
# Construa um dicionário que armazenará a quantidade de vezes que
# cada letra aparece na frase.

fraseD = "Esse é um teste para medir meus conhecimentos em python"
fraseD = fraseD.lower()
print(fraseD)
dicio = {}
valor = {}
valor["letra"] = 0
for i in fraseD:
    dicio[i] = ''
    if i.__contains__(dicio[i]):
        # valor[i] = SOMA AGORA PRA CADA UM
        print(valor[i])
    valor.values()
print(dicio)