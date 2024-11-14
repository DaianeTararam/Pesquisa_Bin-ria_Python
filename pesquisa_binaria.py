def busca_binaria(lista, item):
    menor = 0
    maior = len(lista) - 1

    while menor <= maior:
        meio = (menor + maior) // 2
        tentativa = lista[meio]
        if tentativa == item:
            return meio;
        if tentativa > item:
            maior = meio - 1
        else:
            menor = meio + 1
    return None


lista_numeros = [1,3,5,8,10,11] 
print ("Número encontrado: ")
print (busca_binaria(lista_numeros, 10))

lista_nomes = ["Aline", "Bruna", "César", "João", "Ronaldo", "Sandra"]
print ("Nome encontrado: ")
posicao_nome = busca_binaria(lista_nomes, "Bruna")
print("O nome está posicionado na " + str(posicao_nome +1) + "° casa.")
##print (busca_binaria(lista_numeros, 12))