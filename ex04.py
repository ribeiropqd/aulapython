from time import time
nome = input('Digite o nome do usuário: ')
cpf = int(input('Digite o CPF do usário (somente os números): '))
renda = float(input('Digite a renda do usuário: '))
print('\nO usuário: {}, de CPF: {}, tem a renda: {}.\n'.format(nome, cpf, renda))
if renda > 4664.68:
    print(f'A alíquota para uma renda de R$ {renda} é de 27.5%')
elif renda > 3751.06:
    print(f'A alíquota para uma renda de R$ {renda} é de 22.5%')
elif renda > 2826.66:
    print(f'A alíquota para uma renda de R$ {renda} é de 15%')
elif renda > 1903.99:
    print(f'A aliquota para uma renda de R$ {renda} é de 7.5%')
else:
    print(f'A alíquota para uma renda de R$ {renda} é insenta')
