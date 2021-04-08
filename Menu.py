from Cafés import Cafe
from Participantes import Participante
from Salas import Sala
from tabulate import tabulate
from Gerenciador import *

# Estrutura do menu principal
while True:

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
        while True:
            submenu_cad = str(input("Submenu de cadastro : \n(a)Cadastrar novo participante;"
                                    "\n(b)Cadastrar nova sala de evento;"
                                    "\n(c)Cadastrar nova sala de café;"
                                    "\nou qualquer outra tecla para voltar"
                                    "\nQual das opções deseja escolher? ")).lower().strip()

            if submenu_cad == "a":
                while True:
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
                        break

            elif submenu_cad == "b":
                while True:
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
                        break

            elif submenu_cad == "c":
                while True:
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
                        break

            else:
                print("Voltando ao menu principal...")
                break

    # Estrutura do submenu de consultas
    elif menu_p == "b":
        while True:
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
                break

    # Submenu para a criação de novo evento a partir dos dados salvos
    elif menu_p == "c":
        organizar_evento(dados_p, dados_s, dados_c)
    elif menu_p == "d":
        print("Saindo...")
        break

    else:
        print("Voltando ao menu principal...")
