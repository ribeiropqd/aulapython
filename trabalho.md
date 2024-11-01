# Trabalho de Paradigmas de Programação em Python
Olá, tudo bem? Meu nome é Victor Ribeiro, sou aluno de Análise e desenvolvimento de sistemas (ADS), e este é o projeto da aula de Paradigmas de programação em Python. A seguir você terá mais informações sobre o projeto.

## Objetivo

O objetivo deste projeto é utilizar e práticar **paradigmas de programação** em Python, com foco em **Programação Estruturada** e **Orientação a Objetos (POO)**. 

## Projeto

### 1. Classe `Produto`

No caso deste projeto tive que implementar uma classe chamada `Produto` com as seguintes características:

- **Atributos**:
  - `nome`: nome do produto.
  - `preco`: preço do produto.
  - `quantidade`: quantidade disponível do produto.

Os métodos utilizados foram:

- **Métodos**:
  - `__init__(self, nome, preco, quantidade)`: inicializa o produto com o nome, preço e quantidade fornecidos.
  - `exibir_informacoes(self)`: exibe as informações do produto (nome, preço e quantidade).
  - `atualizar_preco(self, novo_preco)`: atualiza o preço do produto.
  - `atualizar_quantidade(self, nova_quantidade)`: atualiza a quantidade do produto.

- **Algoritmo**:

Arquivo: produtos.py

```python
class Produto: # É a classe que foi criada para o programa.
    def __init__(self, nome: str, preco: float, quantidade: int) -> None: # São os atributos e métodos utilizados no programa.
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    def exibir_informacoes(self) -> str: #Função utilizada para mostrar os dados ao usuários.
        print('\033[7;32;40m=' * 10, 'LOJA DO VICTOR', '='*10, '\033[0;0m')
        return (f'NOME DO PRODUTO: {self.nome.upper()}\n' # Exibe o nome do produto, o .upper() foi adicionado por conta da estética do programa, deixando as letras em CAPSLOCK.
                f'PRECO: R${self.preco:.2f}\n' # Exibe o valor do produto.
                f'QUANTIDADE DE PRODUTOS: {self.quantidade}') # Exibe a quantidade do produto.


dados_pdt = Produto('produto...', 0, 0) #Preenche os dados da função.
pdt = dados_pdt.exibir_informacoes() #Armazena o resultado da função exibir_informacoes.

```

Arquivo: victor.py

```python
from produtos import Produto # Importa a classe criada.

produtos = [] #Lista para armazenar os produtos.

def adicionar_produto(): # Função utilizada para adicionar produtos ao programa.
    nome = input('DIGITE O NOME DO PRODUTO: ') # Pergunta ao usuário o nome do produto que deseja adicionar.
    preco = float(input('DIGITE O PREÇO DO PRODUTO: ')) # Pergunta o valor do produto.
    quantidade = int(input('DIGITE A QUANTIDADE DO PRODUTO: ')) # Pergunta a quantidade de produtos que estão sendo adicionados.
    produto = Produto(nome, preco, quantidade)
    produtos.append(produto)
    print(f'\033[32mPRODUTO "{nome}" FOI ADICIONADO COM SUCESSO!\n\033[0;0m')

def exibir_produtos(): # Função utilizada para exbir os produtos que já foram adicionados e estão armazenados no programa.
    if not produtos: # Executa o print, caso não tenha nenhum produto armazenado.
        print('NENHUM PRODUTO CADASTRADO.')
    else:
        print('LISTA DE PRODUTOS:\n') # Quando há produtos armazenados, eles serão exibidos e o programa chamará a função exibir_informacoes.
        for produto in produtos:
            print(produto.exibir_informacoes())


def atualizar_preco(): # Função que quando chamada serve para atualizar o valor dos produtos que já estão armazenados.
    nome = input('DIGITE O NOME DO PRODUTO PARA ATUALIZAR O PREÇO: ')
    for produto in produtos: # Caso o produto esteja armazenado, ele chamará a função e o usuário poderá fazer a alteração do preço.
        if produto.nome.lower() == nome.lower(): # Minimiza a string para que não haja conflito de caracteres, caso um esteja maísculo e o outro minusculo, vice-versa.
            novo_preco = float(input('DIGITE O NOVO PREÇO: R$ ')) # Pergunta ao usuário o novo preço do produto.
            produto.preco = novo_preco # Exibe o novo preço.
            print(f'PREÇO DO PRODUTO {nome} ATUALIZADO PARA R${novo_preco}')


def atualizar_quantidade(): # Função que quando chamada serve para atualizar a quantidade de produtos que já foram armazenados.
    nome = input('DIGITE O NOME DO PRODUTO PARA ATUALIZAR A QUANTIDADE: ')
    for produto in produtos:
        if produto.nome.lower() == nome.lower(): # Faz o cálculo da nova quantidade de produtos.
            nova_quantidade = int(input('DIGITE A NOVA QUANTIDADE: ')) # Recebe o resultado final do cálculo e exibe a nova quantidade.
            print(f'QUANTIDADE DO PRODUTO {nome} ATUALIZADA PARA: {nova_quantidade}. \n')
            return
        print('\033[31mPRODUTO NÃO ENCONTRADO\033[0;0m') # Caso não haja produto armazenado, ele irá avisar.

def menu(): # Função utlizada para exibir opções de escolha ao usúario.
    while True:
        print('\n\033[32m* MENU DE OPÇÕES *\033[0;0m')
        print('1. ADICIONAR PRODUTO')
        print('2. EXIBIR PRODUTOS')
        print('3. ATUALIZAR PREÇO')
        print('4. ATUALIZAR QUANTIDADE')
        print('5. SAIR')

        opcao = input('\nESCOLHA UMA OPÇÃO: ')

        match opcao:
            case '1':
                adicionar_produto()
            case '2':
                exibir_produtos()
            case '3':
                atualizar_preco()
            case '4':
                atualizar_quantidade()
            case '5':
                exit(print('\n\033[7;34m ENCERRANDO O PROGRAMA, MUITO OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE... \033[0;0m'))
            case _:
                print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[0;0m')



if __name__ == "__main__":
    menu()

```

### 2. Menu Interativo

Criei um arquivo separado que funciona como o **menu principal** manipulando os objetos da classe `Produto`. O menu oferece as seguintes opções:

1. **Adicionar Produto**: Cria uma nova instância da classe `Produto` com os dados inseridos pelo usuário.
2. **Exibir Produtos**: Mostra uma lista de todos os produtos cadastrados com suas informações detalhadas.
3. **Atualizar Preço**: Permite ao usuário escolher um produto pelo nome e atualizar seu preço.
4. **Atualizar Quantidade**: Permite ao usuário escolher um produto pelo nome e atualizar sua quantidade.
5. **Sair**: Encerra o programa.

### 3. Estrutura do Programa

- Utilizando **Programação Estruturada** para o menu, criei algumas funções separadas para cada operação (Ex: adicionar produto, exibir produtos, atualizar preço, atualizar quantidade).
- Utilizei **Orientação a Objetos** para manipular os produtos, garantindo a encapsulação dos dados e a reutilização de métodos da classe `Produto`.

### 4. Regras e Validações

- O programa trata entradas inválidas (por exemplo: ao tentar atualizar um produto inexistente ou inserir valores inválidos para preço ou quantidade, o programa não executa, ou consta como inválido).
- Utilizei laços e condicionais para criar o fluxo do menu, garantindo que o usuário possa realizar operações repetidamente até escolher a opção "Sair" e ainda gerando uma mensagem de aviso/agradecimento.