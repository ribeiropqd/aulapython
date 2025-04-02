import os
from aluno2 import Aluno # Importa a classe criada.

ARQUIVO_ALUNOS = "alunos.txt"

alunos = [] # Lista para armazenar os alunos.

def carregar_alunos():
    if os.path.exists(ARQUIVO_ALUNOS): # Verifica se o arquivo existe
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, idade = linha.strip().split(",") # Divide os dados
                alunos.append(Aluno(nome, disciplina = str , nota = float)) # Converte para objeto
    print("Dados carregados com sucesso!")

def salvar_alunos():
    with open(ARQUIVO_ALUNOS, "w", encoding="urf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno.nome},{aluno.disciplina},{aluno.nota}\n") # Escreve no arquivo
    print("Dados salvos!")

def adicionar_aluno():
    nome = str(input("DIGITE O NOME DO ALUNO: "))
    disciplina = str(input("DISCIPLINA: "))
    nota = float(input("DIGITE A NOTA DO ALUNO: "))
    aluno = Aluno(nome, disciplina, nota)
    alunos.append(aluno)
    print(f"NOTA DO ALUNO {nome}, ADICIONADA COM SUCESSO!")

def exibir_alunos(): # Função utilizada para exibir os alunos adicionados a lista.
    if not alunos: # Executa o print, casa não haja aluno com o respectivo nome.
        print("NENHUM ALUNO ENCONTRADO.")
    else:
        print("LISTA DE ALUNOS") # Quando há aluno registrado, será exibido e o programa chamará a função exibir_informacoes.
        for aluno in alunos:
            print(aluno.exibir_informacoes())

def edit_disciplina():
    nome = input("DIGITE O NOME DO ALUNO QUE DESEJA ALTERAR: ")
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            nova_disciplina = input(str("DIGITE A NOVA DISCIPLINA: "))
            print(f"DISCIPLINA DO ALUNO {nome}, ATUALIZADA PARA: {nova_disciplina}.\n")
            return
        print("ALUNO NÃO ENCONTRADO.") # Caso o aluno não esteja registrado.

def editar_nota():
    nome = input(str("DIGITE O NOME DO ALUNO QUE DESEJA ALTERAR: "))
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            edit_aluno = input(float("DIGITE A NOVA NOTA DO ALUNO: ")) # Pede a nova nota ao usuário do aplicativo.
            aluno.nota = edit_aluno # Exibe a nova nota.
            print(f"NOTA DO ALUNO {nome}, ATUALIZADA PARA {edit_aluno}")
            return
        print("ALUNO NÃO ENCONTRADO.")

def excluir_aluno():
    nome = input("DIGITE O NOME DO ALUNO QUE DESEJA EXCLUIR: ")
    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            alunos.remove(aluno)
            print(f"ALUNO {nome} REMOVIDO COM SUCESSO!")

def visualizar_arquivo():
    if os.path.exists(ARQUIVO_ALUNOS):
        with open(ARQUIVO_ALUNOS, "r", encoding="urf-8") as arquivo:
            conteudo = arquivo.read()
            print("\nCONTEÚDO DO ARQUIVO ALUNOS.TXT:\n")
            print(conteudo if conteudo else "O ARQUIVO ESTÁ VAZIO!")
    else:
        print("O ARQUIVO ALUNOS.TXT AINDA NÃO FOI CRIADO")

def menu():
    while True:
        print("REGISTRO DE ALUNOS\n")
        print("1. ADICIONAR ALUNO")
        print("2. EXCLUIR ALUNO")
        print("3. EXIBIR ALUNOS REGISTRADOS")
        print("4. EDITAR DISCIPLINA")
        print("5. EDITAR NOTA")
        print("6. EXIBIR ARQUIVO")
        print("7. SAIR")

        opcao = input("\nESCOLHA A OPÇÃO DESEJADA: \n")
        
        match opcao:
            case '1':
                adicionar_aluno()
            case '2':
                exibir_alunos()
            case '3':
                edit_disciplina()
            case '4':
                editar_nota()
            case '5':
                excluir_aluno()
            case '6':
                visualizar_arquivo()
            case '7':
                exit(print("ENCERRANDO O PROGRAMA, OBRIGADO PELA PREFERÊNCIA!"))
            case _: 
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")

if __name__ == "__main__":
    menu()