def calcular_media(lista):
    if not lista:
        return 0  # Retorna 0 se a lista estiver vazia para evitar divisão por zero
    soma = sum(lista)
    media = soma / len(lista)
    return media

# Exemplo de uso da função:
numeros = [10, 20, 30, 40, 50]
media_resultante = calcular_media(numeros)
print("A média dos números é:", media_resultante)
