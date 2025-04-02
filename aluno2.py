class Aluno:
    def __init__(self, nome: str, disciplina: str, nota: float) -> None: 
        self.nome = nome
        self.disciplina = disciplina
        self.nota = nota

    def exibir_informacoes(self) -> str:
        return(f'NOME DO ALUNO: {self.nome.upper()}\n'
               f'DISCIPLINA: {self.disciplina}\n'
               f'NOTA: {self.nota:.1f}')
    
dados_aluno = Aluno('aluno...', 0, 0) # Preenche os dados da função.
alu = dados_aluno.exibir_informacoes() # Armazena o resultado da função exibir_informacoes.

        