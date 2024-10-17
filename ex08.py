import random #Biblioteca random
while True:
    print('DIGITE 1 OU 2 A SEGUIR, PARA EXECUTAR OU FECHAR O PROGRAMA.')
    print('''1 - rola o dado \n 2- sair''')
    usuario = int(input('O que você deseja: '))
    if usuario == 1:
        numero = random.randint (0,15)
        print('O número sorteado foi:\033[91m {} \033[0m\n'.format(numero))
    else:
        break

