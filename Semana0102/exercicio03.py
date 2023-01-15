# 3. Implemente um algoritmo em Python para manipular o sistema de cadastro de um aluno.

def main():
    #o)	Utilize uma estrutura lista para adicionar os dados dos alunos (nome, sobrenome e e-mail);
    #p)	Crie uma estrutura dicionário para armazenar os dados de cada aluno associado a uma chave (matrícula);
    #q)	Cadastre cinco alunos no sistema;
    for i in range(5):

        dados = ["", "", ""]

        globals()[f"aluno_{i}"] = {
            "matricula": 0,
            "dados": dados
        }
        
        matricula = input("Informe a matrícula do aluno: ")
        dados[0] = input("Informe o nome do aluno: ")
        dados[1] = input("Informe o sobrenome do aluno: ")
        dados[2] = input("Informe o e-mail do aluno: ")

        globals()[f"aluno_{i}"].update({"matricula": matricula, "dados": dados})

    #r)	Imprima os dados de todos dos alunos e sua matrícula.
    for j in range(5):
        print(globals()[f"aluno_{j}\n"])

    # Exemplo de entrada:
    # •	Adicione um valor para matrícula: 123456;
    # •	Adicione um valor para nome: Maria;
    # •	Adicione um valor para sobrenome: Silva;
    # •	Adicione um valor para e-mail: maria.silva@gmail.com;

if __name__ == "__main__":
    main()