from json import dump, load
from os.path import isfile


# Função para salvar os dados em um json.
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


# Função para a criação de novo evento a partir dos dados salvos
def organizar_evento(dados_p, dados_s, dados_c):
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

