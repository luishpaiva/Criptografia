# 1. Implemente um algoritmo em Python para manipular sua lista de filmes favoritos.

def main():
    #a)	Crie uma lista vazia em Python;
    lista = []

    #b)	Adicione o nome de 5 filmes na lista de favoritos;
    lista.append("The Godfather")
    lista.append("The Shawshank Redemption")
    lista.append("Schindler's List")
    lista.append("Casablanca")
    lista.append("Citizen Kane")

    #c)	O usuário deverá solicitar o nome de cada filme (usar o comando while);
    while (True):
        opcao = int(input("Informe a posição que deseja consultar ('9' para sair): "))
        if opcao in (0, 1, 2, 3, 4):
            print(lista[opcao] + "\n")
        elif opcao == 9:
            break
        else:
            print("Opção escolhida não é válida!!!\n")

    #d)	Posteriormente imprima todos os filmes e sua posição na lista;
    #e)	Para imprimir a lista utilizar o comando for e conjunto da função enumerate().
    for posicao, filme in enumerate(lista):
        print(posicao, filme)

if __name__ == "__main__":
    main()