<b>SEMANAS 01 e 02</b>

1.	Implemente um algoritmo em Python para manipular sua lista de filmes favoritos.
Especificação:

    a)	Crie uma lista vazia em Python;</br>
    b)	Adicione o nome de 5 filmes na lista de favoritos;</br>
    c)	O usuário deverá solicitar o nome de cada filme (usar o comando while);</br>
    d)	Posteriormente imprima todos os filmes e sua posição na lista;</br>
    e)	Para imprimir a lista utilizar o comando for e conjunto da função enumerate().

2.	Implemente um algoritmo em Python para manipular uma lista de material escolar.
Especificação:

    f)	Crie duas estruturas de dicionário:</br>
    g)	Armazenar 3 itens escolares no primeiro dicionário;</br>
    h)	Criar o segundo dicionário vazio;</br>
    i)	Os itens devem ser solicitados ao usuário (usar o comando while);</br>
    j)	Código do produto (chave do dicionário);</br>
    k)	Tipo do material (valor do dicionário);</br>
    l)	Permita que o usuário adicione apenas 5 elementos na lista;</br>
    m)	Atualize o primeiro dicionário com o conteúdo do segundo (usar a função update());</br>
    n)	Posteriormente imprima todos os elementos da lista (usar o comando for).

3.	Implemente um algoritmo em Python para manipular o sistema de cadastro de um aluno.
Especificação:

    o)	Utilize uma estrutura lista para adicionar os dados dos alunos (nome, sobrenome e e-mail);</br>
    p)	Crie uma estrutura dicionário para armazenar os dados de cada aluno associado a uma chave (matrícula);</br>
    q)	Cadastre cinco alunos no sistema;</br>
    r)	Imprima os dados de todos dos alunos e sua matrícula.

        Exemplos de entrada:
        •	Adicione um valor para matrícula: 123456;
        •	Adicione um valor para nome: Maria;
        •	Adicione um valor para sobrenome: Silva;
        •	Adicione um valor para e-mail: maria.silva@gmail.com;

    s) Adicionar outro aluno? (s/n)

<b>SEMANA 03</b>

1. Autenticação Multifator

    Esta atividade consiste em explorar os principais fundamentos dos mecanismos de autenticação, que são os primeiros passos para uma autenticação multifator. O propósito desta atividade é apresentar as vantagens de utilizar uma autenticação multifator. Observar que é possível combinar diferentes técnicas de autenticação. Dessa forma, se o adversário (hacker) comprometer uma única técnica, ele não compromete todo o sistema de autenticação. Para que você compreenda a importância de combinar diferentes técnicas de autenticação reduzindo a probabilidade de o sistema ser comprometido, você será desafiado a implementar uma autenticação multifator para o banco de Tóquio. Nesta atividade, será implementado uma autenticação de dois fatores em Python, adicionando mais um nível de segurança no processo de autenticação do banco.

    Descrição da atividade: Esta atividade será realizada em três etapas. A primeira etapa consiste em utilizar o mecanismo de autenticação do Firebase no Python. Na segunda etapa você deverá implementar em Python as rotinas para realizar envio de e-mail realizando autenticação via Gmail, onde será utilizado o protocolo SMTP. A terceira etapa propõe um desafio, implementar uma autenticação multifator para o banco de Tóquio. Para alcançar este objetivo você deverá integrar os conhecimentos das etapas 1 e 2.

    Especificação Etapa 1 – Firebase: O Firebase é uma plataforma de desenvolvimento Web que possui diversos recursos, em específico vamos utilizar o mecanismo de autenticação, este será integrado com o Python. Para orientar você nesta jornada está sendo fornecido o “Roteiro de Atividade Prática 1” e o código em Python “firebase.txt”.

    Especificação Etapa 2 – Autenticação Gmail: Esta atividade consiste em demostrar como é possível enviar e-mail em Python utilizando a autenticação do Gmail, iremos utilizar o protocolo SMTP. A proposta desta atividade é fornecer base para implementação de um segundo fator de autenticação, atividade que será desenvolvida na etapa 3.  Para orientar você na segunda etapa está sendo fornecido o “Roteiro de Atividade Prática 2” e o código em Python “email.txt”.

    Especificação Etapa 3 - Desafio Autenticação Multifator para o banco de Tóquio: Esta atividade consiste em propor um mecanismo de autenticação multifator baseado nos conhecimentos adquiridos na prática 1 e prática 2. Você deve implementar um programa em Python que deve conter as seguintes funcionalidades:

    a.	Criar um menu para interagir com o usuário (cadastrar e-mail, enviar confirmação e-mail e autenticar e-mail);</br>
    b.	Cadastrar o usuário no Firebase;</br>
    c.	Autenticar o usuário no Firebase;</br>

        •	Antes de autenticar o usuário deve estar com o e-mail obrigatoriamente verificado;
        •	Caso o e-mail não esteja verificado não realizar a autenticação;
        •	Quando o e-mail já estiver verificado, autenticar o usuário no Firebase.

    d.	Após autenticar no Firebase vamos criar uma segunda autenticação.</br>

        •	Gerar um número aleatório em Python;
        •	Não mostrar o número aleatório gerado no Python;
        •	Este número deverá ser enviado por e-mail, utilizando o SMTP;
        •	Efetuar a leitura de um número do teclado;
        •	O usuário deve fornecer como entrada o número que foi enviado por e-mail;
        •	Verificar se o número fornecido pelo usuário é igual ao número que foi gerado aleatoriamente;
        •	Quando o número for igual apresentar uma mensagem que o usuário foi autenticado.

<b>SEMANA 04</b>

1. Atividade Somativa Permissão Arquivos Pelo Python:

    a) Crie um programa em Python para armazenar a data e horário que o arquivo foi executado;</br>
    b) A informação da data e horário deve ser armazenada em um arquivo denominado “permissao.txt”;</br>
    c) Sempre que o arquivo for executado você deve verificar se este arquivo existe;</br>
    d) Caso o arquivo exista você deve modificar a permissão deste arquivo para leitura, escrita e execução do proprietário;</br>
    e) Obtenha as informações de data e hora do sistema e armazene em uma variável
    f) Abra o arquivo para escrita;</br>
    g) Grave as informações das variáveis no arquivo “permissão.txt”;</br>
    h) Modifique as permissões do arquivo “permissão.txt” apenas para escrita.

<b>SEMANA 05</b>

1. Funções Hash Criptográficas
   
    A atividade formativa proposta para esta semana visa explorar os conceitos de funções hash criptográficas. O propósito da atividade é utilizar, de maneira prática, algoritmos de funções hash criptográficas para garantir a integridade da informação.

2. Cenário:
   
    No banco de Tóquio informações sigilosas acabaram sendo expostas, em alguns dos sistemas internos a senha trafegava em aberto (sem criptografia), não há garantia que os dados não foram modificados. Visando garantir a integridade dos dados no novo servidor, deverá ser utilizado funções hash criptográficas que deverão ser aplicadas sobre todos os dados sensíveis. Deste modo, será reforçado este mecanismo de segurança.

3. Especificação da Atividade:
   
    Nesta atividade você deverá desenvolver um sistema de autenticação do banco de Tóquio. O programa deve ser escrito na linguagem Python, implementar duas funcionalidades: cadastrar e autenticar o usuário. O programa deve atender os seguintes requisitos:

   3.1. Fornecer um menu para o usuário: cadastrar ou autenticar;
   3.2. Cadastrar o usuário;

        a) Solicitar as informações do usuário pelo console;</br>
        b) As informações do usuário deve conter o nome, login e senha;</br>
        c) Armazenar a senha utilizando o algoritmo de função hash MD5;</br>
        d) As informações do usuário devem ser gravadas em um arquivo ".txt".

   3.3. Autenticar o usuário;

        a) Solicitar as informações do login e senha do usuário pelo console;</br>
        b) Efetuar a leitura do arquivo .txt onde estão foram salvas as informações dos usuários;</br>
        c) Verificar se o login está cadastrado;</br>
        d) Validar se o login foi cadastrado;</br>
        e) Para condição onde o login não foi cadastrado, fornecer a mensagem: “Autenticação inválida!!”;</br>
        f) Ao localizar o login do usuário aplicar a função hash MD5 sobre a senha fornecida pelo usuário;</br>
        g) Verificar se a senha fornecida é igual a senha armazenada no arquivo “.txt”;</br>
        h) Para condição da senha serem diferentes, fornecer a mensagem: “Autenticação Inválida!!”;</br>
        i) Caso a senha esteja correta, apresentar uma mensagem de “bem-vindo” contendo o nome do usuário.

<b>SEMANA 06</b>

1. Criptografia simétrica e assimétrica
   
    A atividade formativa proposta para esta semana visa trabalhar com os principais algoritmos de criptografia simétrica e assimétrica. O propósito dessa aula é utilizar de maneira prática os algoritmos de criptografia, conhecendo os parâmetros, vantagens e limitações de cada um dos algoritmos.

2. Cenário:
   
    Como a segurança dos sistemas computacionais no banco de Tóquio foi comprometida é necessário a substituir todas as chaves públicas e privadas do sistema, vamos adicionar algoritmos de criptografia mais robustos. Para isso seu desafio é desenvolver um programa que utilize a criptografia de chave pública e simétrica.

3. Especificação da Atividade:
   
    Nesta atividade você deverá cifrar uma mensagem utilizando os algoritmos de criptografia RSA e AES. O algoritmo RSA deve ser usado para chave pública e privada considerando diferentes tamanhos (1024, 2048, 4096 e 8192 bits) para o algoritmo AES utilizar a chave de 16 bytes. Por meio deste experimento você conseguirá notar que o desempenho dos algoritmos de criptografia com chave pública e privada está diretamente relacionado ao tamanho da chave.

4. Dicas:
   
    Na realização dos experimentos, para te auxiliar, está sendo fornecido a implementação dos algoritmos de criptografia RSA e AES, implementados na linguagem de programação Python. Para executar os algoritmos é necessário instalar a biblioteca “pycryptodome”. Se você deseja realizar a atividade no GoogleColab, deverá executar o comando seguir:

        !pip install pycryptodome