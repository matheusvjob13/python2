def imprimir_numeros_naturais(n):
    if n < 0:
        print("Por favor, insira um número inteiro positivo.")
        return

    print("Números naturais de 0 até", n, "em ordem crescente:")
    for i in range(n + 1):
        print(i)

# Obter a entrada do usuário
try:
    numero_inteiro = int(input("Digite um número inteiro positivo: "))
    imprimir_numeros_naturais(numero_inteiro)
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro positivo.")
