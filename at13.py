def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho_lista = len(lista_ordenada)

    if tamanho_lista % 2 == 0:
        indice_meio = tamanho_lista // 2
        mediana = (lista_ordenada[indice_meio - 1] + lista_ordenada[indice_meio]) / 2
    else:
        indice_meio = tamanho_lista // 2
        mediana = lista_ordenada[indice_meio]

    return mediana

# Exemplo de uso da função:
numeros = [10, 20, 30, 40, 50]
mediana_resultante = calcular_mediana(numeros)
print("A mediana dos números é:", mediana_resultante)
