velocidade = int(input('Digite a velocidade do veículo em KM/H: '))
if velocidade >= 80:
    acima = velocidade - 80
    multa = 100 + (15*acima)
    print(f'Velocidade acima!, multa de R$ {multa}')
else:
    print(f'Velocidade de {velocidade}KM/H, é permitida na via.')
