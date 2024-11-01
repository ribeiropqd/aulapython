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
