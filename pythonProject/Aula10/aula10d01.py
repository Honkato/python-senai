def campos():
    dicionario = dict()
    while True:
        questoes = input("DIGITE O NOME DO CAMPO DESEJADO: ")
        if questoes == "":
            print("OK PASSANDO PARA A PROXIMA ETAPA...\n")
            break
        elif dicionario.__contains__(questoes):
            print("\n!!!ESSE CAMPO JA FOI ADICIONADO!!!\n")
        else:
            print("CAMPO ADICIONADO COM SUCESSO\n")
            dicionario[questoes.upper()] = ""
    return dicionario


def registrar(dicionario, counta):
    for h in dicionario:
        while True:
            aux = input("DIGITE O "+h+": ")
            if aux == "":
                print("!!!VOCE NÃO DIGITOU NENHUM VALOR!!!")
                print("   !!!FAVOR DIGITAR NOVAMENTE!!!")
            else:
                dicionario[h] = aux
                break
    dicio2[counta] = dicionario
    return dicionario


def formatacao(formatar):

    if formatar == "":
        formatar = dicio2
        adic = " DIGITADAS:"
    else:
        adic = " ADICIONADAS:"
    formatated = str(formatar)
    print( formatated)
    numeros = {0,1,2,3,4,5,6,7,8,9}
    formatated = formatated.replace("{", "")
    formatated = formatated.replace("', '", "\n")
    formatated = formatated.replace("}", "\n")
    formatated = formatated.replace("'", "")
    formatated = formatated.replace("[", "")
    formatated = formatated.replace("]", "\n")
    formatated = formatated.replace("\n, ", "\n---\n")
    for k in numeros:
        formatated = formatated.replace(f"\n{k}: ", f"\n{k}: \n")
    print("\nINFORMAÇÕES"+adic)
    print(formatated)
    print("===============================")
    input("APERTE ENTER PARA CONTINUAR")
    # REPARAR, ADICIONAR DICIONARIO DENTRO DO DICIONARIO


def inputNum(txt):
    while True:
        print(txt)
        try:
            num = int(input())
            break
        except:
            print("\nOPS VOCE DIGITOU ALGO ERRADO\nTENTE NOVAMENTE\n")
    return num


def menuOpcoes():
    msg = ('''===DIGITE O QUE DESEJA FAZER===
                [1] PESQUISAR CADASTRO INDIVIDUAL
                [2] ADICIONAR CADASTRO
                [3] ALTERAR CADASTRO
                [4] VER TODOS OS CADASTROS
                [0] SAIR''')
    while True:
        op = inputNum(msg)
        if op < 0:
            op = 0
        if op > 4:
            op = 4
        break
    return op


if __name__ == '__main__':
    # informacoes(registrar(campos()))
    # OU
    dicio2 = dict()
    count = 0
    msg = ""
    while True:
        i = menuOpcoes()
        if i == 0:
            print("VOCE ESCOLHEU OPCAO [0]")
            print("OK ENTAO TCHAAAUU")
            break
        elif i == 1:
            print("VOCE ESCOLHEU OPCAO [1]")
            msg = "PESQUISAR CADASTRO, PROCURE O CADASTRO PELO NUMERO DE CADASTRO"
            procurar = inputNum(msg)
        elif i == 2:
            print("VOCE ESCOLHEU OPCAO [2]")
            while True:
                count += 1
                dicio = campos()
                form = registrar(dicio, count)
                formatacao(form)
                continuar = input("DIGITE ALGO PARA CONTINUAR, OU ENTER PARA PARAR: ")
                if continuar == "":
                    break
        elif i == 3:
            print("VOCE ESCOLHEU OPCAO [3]")
            procurar = int(input("ALTERAR CADASTRO, PROCURE O CADASTRO PELO NUMERO DE CADASTRO"))
        else:
            print("VOCE ESCOLHEU OPCAO [4]")
            formatacao("")
