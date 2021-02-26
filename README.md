# <h1>Gerenciador de Eventos</h1> 

 <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/><img src="https://img.shields.io/static/v1?label=python&message=3.7&color=blue&style=for-the-badge&logo=PYTHON"/><img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=RED&style=for-the-badge"/>

Status do Projeto: :warning: em desenvolvimento

### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Layout da Aplicação](#Layout-da-aplicação-dash)

:small_blue_diamond: [Pré-requisitos](#Pré-requisitos)

:small_blue_diamond: [Instruções para a compilação e uso](#Instruções-para-a-compilação-e-uso)

## Descrição do projeto 

<p align="justify">
Aplicação criada para cumprir um desafio de programação, que consiste em criar um software que crie e gerencie um evento de treinamento 
que aconteceria em duas etapas, onde as pessoas são divididas em salas com lotação variável, incluindo dois intervalos 
para um café.

A diferença de pessoas em cada sala deve ser de no máximo 1 pessoa. Para estimular a troca de conhecimentos, metade das pessoas precisam trocar de sala entre as duas etapas do treinamento.
Ao consultar uma pessoa cadastrada no treinamento, o sistema deve retornar à sala em que a pessoa ficará em cada etapa e o espaço onde ela realizará cada intervalo de café.
Ao consultar uma sala cadastrada ou um espaço de café, o sistema deve retornar uma lista das pessoas que estarão naquela sala ou espaço em cada etapa do evento.

</p>

## Funcionalidades

:heavy_check_mark: Cadastro de pessoas, com nome e sobrenome;  

:heavy_check_mark: Cadastro de salas de evento, com nome e lotação;

:heavy_check_mark: Cadastro de salas de café, com nome e lotação; 

:heavy_check_mark: Consulta de todos os dados de cadastros;  

:heavy_check_mark: A criação automática do evento conforme os dados cadastrados;

:heavy_check_mark: Persistência dos dados, salvos em arquivos json.


## Layout da Aplicação :dash:

Em breve...

## Pré-requisitos

A aplicação usa apenas bibliotecas nativas do python: os.path, json, unittest.

## Instruções para a compilação e uso

<h3>Compilação:</h3>

1º Instalar o "auto-py-to-exe" com o comando "pip install auto-py-to-exe" no terminal do seu sistema operacional. Qualquer dúvida, você pode consultar as informações disponíveis no site oficial: <a href="https://pypi.org/project/auto-py-to-exe/">auto-py-to-exe</a>

2º Clonar o repositório da aplicação para o seu PC, disponível em <a href="https://github.com/Suu021/Gerenciador-de-Eventos">Gerenciador de eventos</a>. 

3º Executar o "auto-py-to-exe" e colocar como "Script Location" o diretório do arquivo "Gerenciador.py", na opção "Onefile" escolha "One Directory", na opção "Console Window" escolha "Console Based", na opção "Additional Files" coloque os diretórios dos arquivos "Cafés.py", "Participantes.py" e "Salas.py". Na opção "Settings", em "Output Directory" você pode escolher o diretório aonde será salva a compilação da aplicação.

![img.png](img.png)


<h3>Uso:</h3>

1º Entrar no diretório aonde escolheu salvar a compilação da aplicação e execute o "Gerenciador de eventos.exe"

2º Fazer o cadastro de todos os participantes, salas de evento e espaços de café.

3º Ir na opção "Organizar novo evento com os dados já cadastrados", para que a aplicação cumpra com a função proposta de sua criação.

4º Consultar os dados cadastrados e os dados gerados com a aplicação.

5º Quando fechar o executável os dados serão salvos em arquivos json.

## JSON :floppy_disk:

Em breve...

## Licença 

The [MIT License]() (MIT)

Copyright :copyright: 2021 - Gerenciador de eventos