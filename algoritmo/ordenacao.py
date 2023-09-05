def insertion_sort(lista):
    # O loop externo começa com "i" variando de 1 a "n-1", onde "n" é o tamanho da lista.
    for i in range(1, len(lista)):  # Complexidade O(n-1), que podemos chamar de O(n)
        valor_atual = lista[i]  # Complexidade O(1)
        posicao = i  # Complexidade O(1)

        # O loop interno compara "valor_atual" com os elementos na sublista ordenada à esquerda (índices de 0 a "posicao-1").
        while posicao > 0 and valor_atual.nome < lista[posicao - 1].nome:  # Complexidade O(n) no pior caso
            lista[posicao] = lista[posicao - 1]  # Complexidade O(1)
            posicao -= 1  # Complexidade O(1)

        lista[posicao] = valor_atual  # Complexidade O(1)
