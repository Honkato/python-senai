# for x in range(0, 5):
#     print(x)
#
# frase = "Hoje é sexta"
# nomes = ['Gus', 'Tavo']
# for i in frase:
#     print(i)
#
# for h in nomes:
#     print(h)
while True:
    agnt_ja_chego = input ('Agente ja chegou?\n')
    if agnt_ja_chego == 'sim':
        agnt_ja_chego = input('SERIO?\n')
        if agnt_ja_chego == 'SIM':
            break
        else:
            print('ok')