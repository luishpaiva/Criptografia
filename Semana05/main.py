import hashlib
import os
import stat


# 1. Fornecer um menu para o usuário: cadastrar ou autenticar
def menu():
    print("1. Cadastrar\n"
          "2. Autenticar\n"
          "3. Sair")


# 2. Cadastrar o usuário;
def cadastrar_usuario():
    # a. Solicitar as informações do usuário pelo console;
    # b. As informações do usuário deve conter o nome, 'login' e senha;
    nome_fcu = input("\nInforme o seu nome: ")
    login_fcu = input("Informe um login (nome de usuário): ")
    senha_fcu = input("Informe uma senha: ")
    # c. Armazenar a senha utilizando o algoritmo de função hash MD5;
    senha_hash_fcu = hashlib.md5(senha_fcu.encode())
    return nome_fcu, login_fcu, senha_hash_fcu


def salvar_credenciais(nome_fsc: str, login_fsc: str, senha_hash_fsc):
    #   d. As informações do usuário devem ser gravadas em um arquivo ".txt";
    if os.path.isfile("usuarios.txt"):
        os.chmod("usuarios.txt", stat.S_IRWXU)
    arquivo = open("usuarios.txt", "a")
    arquivo.write("Nome: {}, Login: {}, Hash: {}".format(nome_fsc, login_fsc, senha_hash_fsc.hexdigest()))
    arquivo.write("\n")
    arquivo.close()
    os.chmod("usuarios.txt", stat.S_IRUSR)


# 3. Autenticar usuário
def autenticar_usuario():
    # a. Solicitar as informações do ‘login’ e senha do usuário pelo console;
    login_fau = input("\nInforme o seu login (nome de usuário): ")
    senha_fau = input("Informe a sua senha: ")

    # b. Efetuar a leitura do arquivo.txt onde estão foram salvas as informações dos usuários;
    if os.path.isfile("usuarios.txt"):
        arquivo = open("usuarios.txt", "r")
        conteudo = arquivo.read()

        # c. Verificar se o 'login' está cadastrado;
        # d. Validar se o 'login' foi cadastrado;
        # e. Para condição onde o 'login' não foi cadastrado, fornecer a mensagem: “Autenticação Inválida!!”;
        if login_fau not in conteudo:
            print("Autenticação inválida!!!\n")

        # f. Ao localizar o 'login' do usuário aplicar a função hash MD5 sobre a senha fornecida pelo usuário;
        # g. Verificar se a senha fornecida é igual à senha armazenada no arquivo “.txt”;
        # h. Para a condição de as senhas serem diferentes, fornecer a mensagem: “Autenticação Inválida!!”;
        else:
            print("\nLogin cadastrado no sistema! Realizando a autenticação...\n")
            senha_fau_hash = str(hashlib.md5(senha_fau.encode()).hexdigest())

            if senha_fau_hash not in conteudo:
                print("Autenticação inválida!!!\n")

            else:
                print("Autenticação completa! Usuário autenticado.\n")


while True:
    menu()
    opcao = input("Informe a opção desejada (1 a 3): ")

    if opcao == "1":
        nome, login, senha_hash = cadastrar_usuario()
        salvar_credenciais(nome, login, senha_hash)
        print("\nUsuário cadastrado! Retornando ao menu principal...\n")
        continue

    elif opcao == "2":
        autenticar_usuario()
        continue

    elif opcao == "3":
        print("\nSaindo da aplicação...")
        break

    else:
        print("\nOpção inválida! Informe uma opção válida.\n")
