def exemplo_lista(lista, indice, nova_cor):
    lista[indice] = nova_cor
    print(lista[indice])

lista = ["laranja", "azul", "verde", "preto"]
for i in range(len(lista)):
    lista[i] = 1+i
    print(lista)