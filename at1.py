def calcular_soma():
    soma = 0
    for numero in range(1, 101):
        soma += numero
    return soma

resultado = calcular_soma()
print("A soma dos números de 1 a 100 é:", resultado)
