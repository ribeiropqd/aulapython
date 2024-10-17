a = int(input('Digite o tamanho do primeiro lado do triângulo: '))
b = int(input('Digite o tamanho do segundo lado do triângulo: '))
c = int(input('Digite o tamanho do terceiro lado do triângulo: '))

print('Você escolheu as seguintes medidas: \nPrimeiro lado: {}\nSegundo lado: {}\nTerceiro lado: {}'.format(a, b, c))

if (a==b and b==c):
    print('Seu triângulo é equilátero!')
elif (a!=b and b!=c and c!=a):
    print('Seu trângulo é escaleno!')
else:
    print('Seu triângulo é isósceles!')
