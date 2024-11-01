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