import pyrebase
import random
from firebase import firebase_config
from emailusuario import enviar_email
import json


# a. Criar um menu para interagir com o usuário (cadastrar e-mail, enviar confirmação e-mail e autenticar email);
def menu():
    print("1. Cadastrar usuário\n"
          "2. Verificar e-mail\n"
          "3. Autenticar usuário\n"
          "4. Sair\n")


def credenciais():
    usuario = input("Digite seu e-mail: ")
    senha = input("Digite sua senha, com pelo menos 6 caracteres: ")
    return usuario, senha


while True:
    menu()
    opcao = input("Informe o número da opção desejada: ")

    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()

    # b. Cadastrar o usuário no Firebase;
    if opcao == "1":
        user, password = credenciais()

        status_create = auth.create_user_with_email_and_password(user, password)

        print("Status da criação: ", status_create)
        print("Usuário cadastrado: ", user)
        print("Retornando ao menu principal...\n")
        continue

    # c. Autenticar o usuário no Firebase;
    elif opcao == "2":
        mensagem_erro = ""

        # ◦ Antes de autenticar o usuário deve estar com o e-mail obrigatoriamente verificado;
        user, password = credenciais()

        try:
            status_signin = auth.sign_in_with_email_and_password(user, password)

        # ◦ Caso o email não esteja verificado não realizar a autenticação;
        except Exception as erro:
            mensagem_erro = json.loads(erro.args[1])["error"]["message"]
            print("\nErro: {0}.".format(mensagem_erro))
            print("Não foi possível autenticar o usuário. Por gentileza, tente novamente!\n")
            break

        # ◦ Quando o email já estiver verificado, autenticar o usuário no Firebase;
        else:
            print("Status da verificação: ", status_signin)
            print("Retornando ao menu principal...\n")
            continue

    # d. Após autenticar no Firebase vamos criar uma segunda autenticação;
    elif opcao == "3":
        user, password = credenciais()

        try:
            status_signin = auth.sign_in_with_email_and_password(user, password)

        # ◦ Caso o email não esteja verificado não realizar a autenticação;
        except Exception as erro:
            mensagem_erro = json.loads(erro.args[1])["error"]["message"]
            print("\nErro: {0}.".format(mensagem_erro))
            print("Não foi possível autenticar o usuário. Por gentileza, tente novamente!\n")
            break

        # ◦ Quando o email já estiver verificado, autenticar o usuário no Firebase;
        else:

            # ◦ Gerar um número aleatório em Python;
            # ◦ Não mostrar o número aleatório gerado no Python;
            # ◦ Este número deverá ser enviado por email, utilizando o SMTP;
            aleatorio = random.randint(0, 99999)

            enviar_email(
                "luisinhohpaiva@gmail.com",
                user,
                "Envio do número de confirmação",
                "O seu número de verificação é {0}.".format(aleatorio)
            )

            # ◦ Efetuar a leitura de um número do teclado;
            # ◦ O usuário deve fornecer como entrada o número que foi enviado por e-mail;
            teclado = int(input("Informe o número recebido no seu email: "))

            # ◦ Verificar se o número fornecido pelo usuário é igual ao número que foi gerado aleatoriamente;
            # ◦ Quando o número for igual apresentar uma mensagem que o usuário foi autenticado.
            if aleatorio == teclado:
                print("O seu usuário foi autenticado!")
                break
            else:
                print("Ops! Parece que você digitou o número errado. Tente novamente!")
                break

    elif opcao == "4":
        break
    else:
        print("Não foi digitada uma opcao válida. Por gentileza, escolha um número do menu!")
