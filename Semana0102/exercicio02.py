# 2. Implemente um algoritmo em Python para manipular uma lista de material escolar.

def main():
    #f)	Crie duas estruturas de dicionário:
    #g)	Armazenar 3 itens escolares no primeiro dicionário;
    #h)	Criar o segundo dicionário vazio;
    dicionario1 = {
        "codigo": 0,
        "material": []
    }
    
    dicionario2 = {}

    #i)	Os itens devem ser solicitados ao usuário (usar o comando while);
    #j)	Código do produto (chave do dicionário);
    #k)	Tipo do material (valor do dicionário);
    #l)	Permita que o usuário adicione apenas 5 elementos na lista;
    while (True):
        codigo = int(input("Informe o código que deseja atribuir a esse dicionario: "))
        dicionario1.update({"codigo": codigo})

        cont = 0
        
        while cont < 5:
            item = input("Informe o material que deseja adicionar ('9' para sair): ")
            if item != "9":
                dicionario1["material"].append(item)
            else:
                break

            cont += 1
        break

    #m)	Atualize o primeiro dicionário com o conteúdo do segundo (usar a função update());
    dicionario2.update(dicionario1)

    #n)	Posteriormente imprima todos os elementos da lista (usar o comando for).
    for i in range(len(dicionario2["material"])):
        print(dicionario2["material"][i])

if __name__ == "__main__":
    main()