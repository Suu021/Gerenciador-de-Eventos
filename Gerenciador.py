from json import dump, load
from os.path import isfile
from Cafés import Cafe
from Participantes import Participante
from Salas import Sala
from tabulate import tabulate


# Função para salvar os dados em um json ou criar um json para salvar os dados caso ainda não exista
def salvar_dados(nomedojson, file):
    with open(nomedojson, "w", encoding="utf-8") as dados:
        return dump(file, dados, indent=2, separators=(",", ": "), ensure_ascii=False)


# Função para carregar os dados para a visualização e consulta.
def carregar_dados(nomedojson):
    if isfile(nomedojson):  # Verifica se o arquivo já existe, se sim, o json será carregado
        with open(nomedojson, "r", encoding="utf-8") as dados:
            return load(dados)
    else:  # Se o json ainda não existe, a função cria e retorna uma lista
        temporario = []
        return temporario


# Função para padronizar os nomes próprios
def formatar_nome(nome):
    lista = []
    nome = nome.strip()
    for word in nome.split():
        if len(word) > 3:
            word = word[0].upper() + word[1:].lower()
            lista.append(word)
        else:
            word = word.lower()
            lista.append(word)
    f_nome = ' '.join(lista)
    return f_nome


# Estrutura do menu principal
sair = False
while not sair:

    dados_p = carregar_dados("Dados dos Participantes.json")
    dados_s = carregar_dados("Dados das salas de evento.json")
    dados_c = carregar_dados("Dados das salas de café.json")
    # Se os jsons ainda não existirem, uma lista para cada um será retornada

    menu_p = str(input("Menu Principal: \n(a)Cadastrar novo participante, sala de evento ou café;"
                       "\n(b)Consultar cadastro de participante, sala de evento ou café;"
                       "\n(c)Organizar novo evento com os dados já cadastrados;"
                       "\n(d)Sair."
                       "\nQual das opções deseja escolher? ")).lower().strip()

    # Estrutura do submenu de cadastro
    if menu_p == "a":
        submenu_cad = str(input("Submenu de cadastro : \n(a)Cadastrar novo participante;"
                                "\n(b)Cadastrar nova sala de evento;"
                                "\n(c)Cadastrar nova sala de café;"
                                "\nou qualquer outra tecla para voltar"
                                "\nQual das opções deseja escolher? ")).lower().strip()

        if submenu_cad == "a":
            voltar = False
            while not voltar:
                cadastro = input(
                    'Deseja cadastrar novo participante? \n(s) para "sim" ou qualquer outra tecla para voltar: '
                ).lower()
                if cadastro == "s":
                    print("Forneça as informações para novo cadastro de participante:")
                    nome = input("Digite o nome: ")
                    f_nome = formatar_nome(nome)
                    sobrenome = input("Digite o sobrenome: ")
                    f_sobrenome = formatar_nome(sobrenome)
                    cad_p = Participante(f_nome, f_sobrenome, " ", " ", " ", " ")
                    dic = cad_p.conversao_dicionario()
                    dados_p.append(dic)
                    salvar_dados("Dados dos Participantes.json", dados_p)
                else:
                    print("Voltando ao menu principal...")
                    voltar = True

        elif submenu_cad == "b":
            voltar = False
            while not voltar:
                cadastro = input(
                    'Deseja cadastrar nova sala de evento?\n(s) para "sim" ou qualquer outra tecla para voltar: '
                ).lower()
                if cadastro == "s":
                    print("Forneça as informações para novo cadastro de sala de evento:")
                    nome = input("Digite o nome da sala: ")
                    f_nome = formatar_nome(nome)
                    lotacao = int(input("Digite a lotação: "))
                    cad_sala = Sala(f_nome, lotacao, [], [])
                    dic = cad_sala.conversao_dicionario()
                    dados_s.append(dic)
                    salvar_dados("Dados das salas de evento.json", dados_s)
                else:
                    print("Voltando ao menu principal...")
                    voltar = True

        elif submenu_cad == "c":
            voltar = False
            while not voltar:
                cadastro = input(
                    'Deseja cadastrar nova sala de café?\n(s) para "sim" ou qualquer outra tecla para voltar: ').lower()
                if cadastro == "s":
                    print("Forneça as informações para novo cadastro de sala do café:")
                    nome = input("Digite o nome da sala de café: ")
                    f_nome = formatar_nome(nome)
                    lotacao = int(input("Digite a lotação: "))
                    cad_cafe = Cafe(f_nome, lotacao, [], [])
                    dic = cad_cafe.conversao_dicionario()
                    dados_c.append(dic)
                    salvar_dados("Dados das salas de café.json", dados_c)
                else:
                    print("Voltando ao menu principal...")
                    voltar = True

        else:
            print("Voltando ao menu principal...")
            voltar = True

    # Estrutura do submenu de consultas
    elif menu_p == "b":
        submenu_con = str(input("Submenu de consulta: \n(a)Consultar participante;"
                                "\n(b)Consultar sala de evento;"
                                "\n(c)Consultar sala de café;"
                                "\nou qualquer outra tecla para voltar ao menu principal."
                                "\nQual das opções deseja escolher? ")).lower().strip()
        if submenu_con == "a":
            nome_p = input("Digite o nome completo do participante: ")
            f_nome_p = formatar_nome(nome_p)
            contador_pesquisa = 0
            for p in dados_p:
                if p["Sala_etapa1"] == " " and p["Sala_etapa2"] == " " and p["Sala_café"] == " ":
                    print("Precisa criar um evento primeiro para obter os dados completos!")
                elif f_nome_p == p["Nome completo"]:
                    print("=-=" * 20)
                    tabela_p = [[p["Nome"], p["Sobrenome"], p["Sala_etapa1"], p["Sala_etapa2"],
                                 p["Café_intervalo1"], p["Café_intervalo2"]]]
                    print(tabulate(tabela_p, headers=["Nome", "Sobrenome", "Sala_etapa1", "Sala_etapa2", "Café_intervalo1", "Café_intervalo2"], tablefmt="grid"))
                    print("=-=" * 20)
                else:
                    contador_pesquisa += 1

            if contador_pesquisa == len(dados_p):
                print("Nome não cadastrado como participante...")

        elif submenu_con == "b":
            nome_s = input("Digite o nome da sala de evento: ")
            f_nome_s = formatar_nome(nome_s)
            contador_pesquisa = 0
            for sala in dados_s:
                if not sala["Participantes - etapa 1"] and not sala["Participantes - etapa 2"]:
                    print("Precisa criar um evento primeiro para obter os dados completos!")
                elif f_nome_s == sala["Nome"]:
                    print("=-=" * 20)
                    tabela_s = [[sala["Nome"], sala["Lotação"], ('\n'.join(map(str, sala["Participantes - etapa 1"]))),
                                 ('\n'.join(map(str, sala["Participantes - etapa 2"])))]]
                    print(tabulate(tabela_s, headers=["Nome", "Lotação", "Participantes - etapa 1", "Participantes - etapa 2"], tablefmt="grid"))
                    print("=-=" * 20)

                else:
                    contador_pesquisa += 1

            if contador_pesquisa == len(dados_s):
                print("Nome não cadastrado como sala de evento...")

        elif submenu_con == "c":
            nome_c = input("Digite o nome da sala de café: ")
            f_nome_c = formatar_nome(nome_c)
            contador_pesquisa = 0
            for sala in dados_c:
                if not sala["Participantes_intervalo1"] and not sala["Participantes_intervalo2"]:
                    print("Precisa criar um evento primeiro para obter os dados completos!")
                elif f_nome_c == sala["Nome"]:
                    print("=-=" * 20)
                    tabela_c = [[sala["Nome"], sala["Lotação"], ('\n'.join(map(str, sala["Participantes_intervalo1"]))),
                                 ('\n'.join(map(str, sala["Participantes_intervalo2"])))]]
                    print(tabulate(tabela_c,
                                   headers=["Nome", "Lotação", "Participantes_intervalo1", "Participantes_intervalo2"],
                                   tablefmt="grid"))
                    print("=-=" * 20)
                else:
                    contador_pesquisa += 1

            if contador_pesquisa == len(dados_c):
                print("Nome não cadastrado como sala de café...")
        else:
            print("Voltando ao menu principal...")

    # Submenu para a criação de novo evento a partir dos dados salvos
    elif menu_p == "c":
        print("=-=" * 20)
        aviso = str(
            input("Esse é o lugar para você criar e organizar um novo evento a partir dos cadastros de salas e de"
                  "\nparticipantes já realizados previamente. Deseja continuar? s/n: ")).lower()
        print("=-=" * 20)
        if aviso == "s":
            # Organização da etapa 1
            lista1 = []  # Lista temporária que vai receber o nome de todos os participantes cadastrados
            participantes_por_sala = len(dados_p) / len(dados_s)  # variável que determina a quantidade de
            # participantes por sala
            for item in dados_p:  # primeiro iterar sobre toda a lista de dicionários dos participantes
                lista1.append(item['Nome completo'])  # para colocar o nome de todos os participantes na lista

            for sala in dados_s:  # agora, iterar sobre toda a lista de dicionários das salas
                if participantes_por_sala <= sala["Lotação"]:
                    for p in lista1[:int(participantes_por_sala)]:
                        sala['Participantes - etapa 1'].append(p)
                        lista1.remove(p)

                    if lista1:  # essa parte apenas acontece caso alguma sala precise ter mais participantes que outras
                        while len(dados_s) > len(lista1) > 0:
                            for sala in dados_s:
                                for p in lista1:
                                    sala['Participantes - etapa 1'].append(p)
                                    lista1.remove(p)

                else:
                    print(
                        "A quantidade de participantes por sala excedeu a lotação. Pra continuar, por favor, crie mais"
                        " uma sala")

            # Organização da etapa 2
            global metade_p
            lista2 = []
            lista3 = []
            # essa parte da função pega a metade dos membros da lista da etapa 1 que vão mudar de sala na etapa 2
            for sala in dados_s:
                metade_p = len(sala['Participantes - etapa 1']) // 2
                for p in sala['Participantes - etapa 1'][:metade_p]:
                    lista2.append(p)
            lista3 = lista2[metade_p:]
            for p in dados_s[0]['Participantes - etapa 1'][:metade_p]:
                lista3.append(p)

            # parte da função que adiciona os itens que foram embaralhados na lista3 para a lista de particiantes da
            # etapa 2
            for sala in dados_s:
                for p in lista3[:metade_p]:
                    sala['Participantes - etapa 2'].append(p)
                    lista3.remove(p)

                # parte da função que mantém a outra metade dos membros da lista da primeira etapa para a segunda:
                for p in sala['Participantes - etapa 1'][metade_p:]:
                    sala['Participantes - etapa 2'].append(p)
            salvar_dados("Dados das salas de evento.json", dados_s)

            # Organização do café primeiro intervalo
            lista4 = []  # Lista temporária que vai receber o nome de todos os participantes cadastrados
            participantes_por_sala = len(dados_p) / len(dados_c)  # variável que determina a quantidade de
            # participantes por sala
            for item in dados_p:  # primeiro iterar sobre toda a lista de dicionários dos participantes
                lista4.append(item['Nome completo'])  # para colocar o nome de todos os participantes na lista

            for sala in dados_c:  # agora, iterar sobre toda a lista de dicionários das salas de café
                if participantes_por_sala <= sala["Lotação"]:
                    for p in lista4[:int(participantes_por_sala)]:
                        sala['Participantes_intervalo1'].append(p)
                        lista4.remove(p)

                    if lista4:  # essa parte apenas acontece caso alguma sala precise ter mais participante que outras
                        while len(dados_c) > len(lista4) > 0:
                            for sala in dados_c:
                                for p in lista4:
                                    sala['Participantes_intervalo1'].append(p)
                                    lista4.remove(p)

                else:
                    print(
                        "A quantidade de participantes por sala excedeu a lotação. Pra continuar, por favor, crie mais"
                        " uma sala")

            # Organização do café segundo intervalo
            lista5 = []
            lista6 = []
            # essa parte da função pega a metade dos membros da lista4 do primeiro intervalo que vão mudar de
            # sala no segundo intervalo
            for sala in dados_c:
                metade_p = len(sala['Participantes_intervalo1']) // 2
                for p in sala['Participantes_intervalo1'][:metade_p]:
                    lista5.append(p)
            lista6 = lista5[metade_p:]
            for p in dados_c[0]['Participantes_intervalo1'][:metade_p]:
                lista6.append(p)

            # parte da função que adiciona os itens que foram embaralhados na lista6 para a lista de
            # particiantes da etapa 2
            for sala in dados_c:
                for p in lista6[:metade_p]:
                    sala['Participantes_intervalo2'].append(p)
                    lista6.remove(p)

                # parte da função que mantém a outra metade dos membros da lista da primeiro intervalo para o
                # segundo
                for p in sala['Participantes_intervalo1'][metade_p:]:
                    sala['Participantes_intervalo2'].append(p)

            salvar_dados("Dados das salas de café.json", dados_c)

            # Passar os novos dados gerados para as informações dos participantes
            for p in dados_p:

                # Procurar em qual sala o participante terá a etapa 1
                for sala in dados_s:
                    if p['Nome completo'] in sala['Participantes - etapa 1']:
                        p['Sala_etapa1'] = sala['Nome']

                    # Procurar em qual sala o participante terá a etapa 2
                    if p['Nome completo'] in sala['Participantes - etapa 2']:
                        p['Sala_etapa2'] = sala['Nome']

                # Procurar em qual sala de café o participante irá em seu primeiro intervalo
                for sala in dados_c:
                    if p['Nome completo'] in sala['Participantes_intervalo1']:
                        p['Café_intervalo1'] = sala['Nome']

                    # Procurar em qual sala de café o participante irá em seu segundo intervalo
                    if p['Nome completo'] in sala['Participantes_intervalo2']:
                        p['Café_intervalo2'] = sala['Nome']

            salvar_dados("Dados dos Participantes.json", dados_p)
            print("Um novo evento foi criado com sucesso!")
            print("=-=" * 20)

        elif aviso == "n":
            print("Voltando ao menu principal...")
        else:
            print("Voltando ao menu principal...")
    elif menu_p == "d":
        sair = True
        print("Saindo...")

    else:
        print("Voltando ao menu principal...")
