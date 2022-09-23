dicionario = dict()
listaFrutas = []
dicionario[1] = {'abacaxi':'FRUTA CITRICA TÍPICA DO BRASIL'}
dicionario[1]['laranja'] = 'laranja'
dicionario[1]['maça'] = 'vermelinha hhhmmm'
dicionario[1]['livro'] = 'acho que não é fruta mas tem gente q devora'
dicionario[1]['caviar'] = 'nunca vi nem comi so ouço falar'
dicionario[2] = {'Suzanoo':'mangekyo'}
# print(dicionario[1].values())
# print(dicionario)
# digite = input('DIGITE UMA FRUT A PROCURAR')
# if dicionario[1].__contains__(digite):
#     print('sim')
#
#     print(f'{digite} : {dicionario[1][digite]}')
# print("\n\nTESTATIVA AKKII",dicionario.get(1))
novoDici = str(dicionario)

novoDici = novoDici.replace("{", "")
novoDici = novoDici.replace("}", "")
novoDici = novoDici.replace(", '", "\n   ")
novoDici = novoDici.replace("'", "")
novoDici = novoDici.replace(", ", "\n")
# novoDici = novoDici.replace("1", "Maranhão")

print(novoDici)
print('\nSELECIONE UMA FRUTA DE NOSSA SELEÇÃO: ')
for i in dicionario[1]:
    if i != 'caviar':
        print(i, end=", ")
    else:
        print(i)
