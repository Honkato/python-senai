# cadastro = {'nome': 'Joâo','idade': 21}

# cadastro = dict(nome='João', idade=21)
# # cadastro = dict(nome='Maria', idade=19)
# cadastro['nome'] = 'Maria'
# print(cadastro)
# print(cadastro['idade'])
# print(cadastro['nome'])
# from pprint import pprint

# lista = []
# for i in range(2):
#     nome = input('Digite um nome: ')
#     idade = int(input('Digite a idade'))
#     cadastro = dict(nome=nome, idade=idade)
#
#     print(cadastro.keys())
#     print(cadastro.values())
#     print(cadastro.items())
#     for chave, valor in cadastro.items():
#         print(f'{chave} - {valor}')

# listaFrutas = []
# dicionario = {'palavra':'Abacaxi', 'definicao':'FRUTA CITRICA TÍPICA DO BRASIL'}
# listaFrutas.append(dicionario)
# dicionario = {'palavra':'Melancia', 'definicao':'FRUTA ACUOSA'}
# listaFrutas.append(dicionario)
# fruta = dict()
frutas = {'abacaxi'   :   'marelo',
    'abacate'   :   'tem uma barriguinha',
    'melancia'  :   'acuosa'
    }
frutas['laranja'] = 'laranja'
for i in frutas:
    print(i, end=" | ")

while True:
    verd = True
    digite = input('\nDIGITE UMA FRUTA PARA PROCURAR A DEFINIÇÃO: ')
    if frutas.__contains__(digite):
        print(frutas[digite])
    else:
        nome = digite
        digite = input('A fruta digitada não existe, deseja cadastrar?\n')
        if digite.lower() == 'sim':
            digite = input('DIGITE A DESCRIÇÃO: ')
            frutas[nome] = digite
            digite = nome
        else:
            print('tabomentao')
    if verd:
        for i in frutas:
            if digite == frutas:
                print(f'Fruta: {digite}\nDescrição: {i}')
