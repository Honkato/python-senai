cidade = input('Digite o nome da cidade')
if cidade.lower().find('santo') != -1:
    print(f'A Cidade {cidade} tem Santo no nome')
else:
    print(f'A Cidade {cidade} NAO tem Santo no nome')