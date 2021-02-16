from Participantes import Participante
from Salas import Sala
from Cafés import Café
import json


def salvar_dados(dado):
    with open("Dados do Gerenciador.json", "w") as dados:
        json.dump(dado)


def consultar_dados(dado):
    with open("Dados do Gerenciador.json", "r") as dados:
        return

def remover_dados(dado):
    with open("Dados do Gerenciador.json", "r") as dados:
        return

#while not "d":


menu_p = input("Menu Principal: \n(a)Cadastrar novo participante, sala de evento ou café;"
                 "\n(b)Consultar cadastro de participante, sala de evento ou café;"
                 "\n(c)Remover cadastro de novo participante, sala de evento ou café;"
                 "\n(d)Sair."
                 "\n Qual das opções deseja escolher? ").lower()

if menu_p is "a":
    submenu_cad = input("Submenu de cadastro : \n(A)Cadastrar novo participante;"
    "\n(B)Cadastrar nova sala de evento;"
    "\n(C)Cadastrar nova sala de café;"
    "\n(D)Voltar ao menu principal."
    "\n Qual das opções deseja escolher? ").upper()

    if submenu_cad is "A":
        print("Forneça as informações para novo cadastro de participante:")
        nome = input("Digite seu nome: ").split()
        sobrenome = input("Digite seu sobrenome: ").split()
        cad_partic = Participante(nome, sobrenome)
        salvar = salvar_dados(cad_partic)

    elif submenu_cad is "B":
        senha_adm = input("Digite a senha de administrador: ")
        if senha_adm == "s?(:x<bF":
            print("Forneça as informações para novo cadastro de sala:")
            nome = input("Digite o nome da sala: ").split()
            lotação = int(input("Digite a lotação: ")).split()
            cad_sala = Sala(nome, lotação)
            salvar = salvar_dados(cad_sala)
        else:
            print("Você não tem permissão para cadastrar nova sala de evento...")


    elif submenu_cad is "C":
        print("Forneça as informações para novo cadastro de sala do café:")
        nome = input("Digite o nome da sala de café: ").split()
        lotação = int(input("Digite a lotação: ")).split()
        cad_café = Café(nome, lotação)
        salvar = salvar_dados(cad_café)

    elif submenu_cad is "D":
        submenu_cad = menu_p

    else:
        print("Opção inválida!")

elif menu_p is "b":
    submenu_con = input("Submenu de consulta: \n(A)Consultar participante;"
    "\n(B)Consultar sala de evento;"
    "\n(C)Consultar sala de café;"
    "\n(D)Voltar ao menu principal."
    "\n Qual das opções deseja escolher? ").upper()

elif menu_p is "c":
    submenu_con = input("Submenu de remoção: \n(A)Remover participante;"
    "\n(B)Remover sala de evento;"
    "\n(C)Remover sala de café;"
    "\n(D)Voltar ao menu principal."
    "\n Qual das opções deseja escolher? ").upper()

else:
    print("Opção inválida!")