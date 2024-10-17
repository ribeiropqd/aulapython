nome = input('Digite o nome do usuário: ')
idade = int(input('Digite a idade do usuário: '))
altura = float(input('Digite a altura do usuário em metros: '))
peso = float(input('Digite o peso do usuário em quilogramas: '))

imc = peso/(altura**2)

if imc < 18.5:
    classificacao = 'Abaixo do peso.'
elif imc < 24.9:
    classificacao = 'Peso normal.'
elif imc < 29.9:
    classificacao = 'Sobre peso.'
elif imc < 34.9:
    classificacao = 'Obesidade 1º.'
elif imc < 39.9:
    classificacao = 'Obesidade 2º.'
else:
    classificacao = 'Obesidade 3º.'

print(f'Dados')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'Peso: {peso}')
print(f'IMC: {imc:.1f}')
print(f'Classificação: {classificacao}')
