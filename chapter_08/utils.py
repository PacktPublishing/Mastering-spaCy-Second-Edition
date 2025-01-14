def create_consecutive_token_sequences(lista):
    sequencias = []
    i = 0
    while i < len(lista):
        inicio = lista[i]
        fim = lista[i]
        while i + 1 < len(lista) and lista[i + 1] == lista[i] + 1:
            fim = lista[i + 1]
            i += 1
        if inicio != fim:
            sequencias.append((inicio, fim))
        else:
            sequencias.append((inicio, inicio))
        i += 1
    return sequencias
