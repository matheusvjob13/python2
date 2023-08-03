def fatorial(numero):
    if numero < 0:
        return None  # Retornar None para indicar que não é possível calcular o fatorial de números negativos
    elif numero == 0:
        return 1  # O fatorial de 0 é 1 por definição
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Exemplo de uso da função:
numero_teste = 5
resultado_fatorial = fatorial(numero_teste)

if resultado_fatorial is not None:
    print(f"O fatorial de {numero_teste} é {resultado_fatorial}.")
else:
    print("Não é possível calcular o fatorial de um número negativo.")
