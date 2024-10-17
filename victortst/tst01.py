idade = int(input('Digite a sua idade: '))
if idade <= 18:
    falta = 18 - idade
    print(f'Infelizmente você é menor de idade, ainda faltam: {falta} anos, para você poder assistir filmes nessa faixa etária.')
else:
    print(f'Você possui {idade} anos de idade, e pode assistir a essa faixa etária.')
