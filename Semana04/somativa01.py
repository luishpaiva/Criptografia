"""
Pontifícia Universidade Católica do Paraná
Escola Politécnica
Disciplina: Segurança da Tecnologia da Informação (11100010564_20222_02)
Professor-tutor: Edson Kageyama
Autores: Luís Henrique Paiva; Vanessa Scoz Braga
Atividade Somativa 01 - 23/10/2022
"""

import pyrebase
import json
import random
import smtplib
import stat
import os
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


firebase_config = {
    "apiKey": "AIzaSyA0P8HQ71g8_WatR9V5keqOou13HDTCSo0",
    "authDomain": "somativa01.firebaseapp.com",
    "projectId": "somativa01",
    "databaseURL": "https://" + "somativa01.appspot.com" + ".firebaseio.com",
    "storageBucket": "somativa01.appspot.com",
    "messagingSenderId": "107368145423",
    "appId": "1:107368145423:web:9e7567b194c4e16d47f97a",
    "measurementId": "G-GG5QSQ7MH0"
}


def credenciais():
    usuario = input("Digite seu e-mail: ")
    senha = input("Digite sua senha, com pelo menos 6 caracteres: ")
    return usuario, senha


def data_hora():
    data_us = datetime.datetime.now()
    data_br = data_us.strftime("%d/%m/%Y")
    hora = data_us.strftime("%H:%M:%S")
    return data_br, hora


def controle_acesso(usuario: str):
    if os.path.isfile("acesso.txt"):
        os.chmod("acesso.txt", stat.S_IRWXU)

    data, hora = data_hora()

    arquivo = open("acesso.txt", "a")
    arquivo.write(f"E-mail: {usuario}, Data: {data}, Hora: {hora}")
    arquivo.write("\n")
    arquivo.close()

    os.chmod("acesso.txt", stat.S_IRUSR)


def enviar_email(para: str, assunto: str, corpo: str):
    server = "smtp.gmail.com"
    port = 587
    emissor = "luisinhohpaiva@gmail.com"
    senha = "njdnbyzjunyycydu"

    mail_from = emissor
    mail_to = para
    mail_subject = assunto
    mail_body = corpo

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = mail_to
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText(mail_body, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(emissor, senha)
    connection.send_message(mensagem)
    connection.quit()


firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


while True:
    print("1. Cadastrar usuário\n"
          "2. Verificar e-mail\n"
          "3. Autenticar usuário\n"
          "4. Sair\n")

    opcao = input("Selecione a opção desejada (1 a 4): ")

    if opcao == "1":
        user, password = credenciais()
        status = auth.create_user_with_email_and_password(user, password)
        print("E-mail cadastrado: ", user)
        print("Retornando ao menu principal...\n")
        continue

    elif opcao == "2":
        user, password = credenciais()

        try:
            status_signin = auth.sign_in_with_email_and_password(user, password)

        except Exception as erro:
            mensagem_erro = json.loads(erro.args[1])["error"]["message"]
            print("\nErro: {0}.".format(mensagem_erro))
            print("Não foi possível verificar o e-mail informado. Por gentileza, tente novamente!\n")
            print("Retornando ao menu principal...\n")
            continue

        else:
            for item, (chave, valor) in enumerate(status_signin.items()):
                print(item, "-", chave, "-", valor)

            print("\nE-mail verificado: ", user)
            print("Retornando ao menu principal...\n")
            continue

    elif opcao == "3":
        user, password = credenciais()

        try:
            status_signin = auth.sign_in_with_email_and_password(user, password)

        except Exception as erro:
            mensagem_erro = json.loads(erro.args[1])["error"]["message"]
            print("\nErro: {0}.".format(mensagem_erro))
            print("Não foi possível autenticar o usuário. Por gentileza, tente novamente!\n")
            continue

        else:
            print("Iniciando segundo fator de autenticação...\n")

            aleatorio = random.randint(99999, 999999)

            enviar_email(
                user,
                "Envio do número de confirmação",
                "O seu número de verificação é {0}.".format(aleatorio)
            )

            teclado = int(input("Informe o número recebido no seu email: "))

            if aleatorio == teclado:
                print("O seu usuário foi autenticado!")
                print("Iniciando o controle de acesso...\n")
                controle_acesso(user)

                print("Atualizando o arquivo de controle de acesso... Por gentileza, aguarde.\n")
                time.sleep(2)
                print("Retornando ao menu principal...\n")

            else:
                print("Ops! Parece que você digitou o número errado. Tente novamente!\n")
                continue

    elif opcao == "4":
        print("Fechando a aplicação...")
        break

    else:
        print("Não foi digitada uma opção válida! Por gentileza, escolha um número do menu.\n")
