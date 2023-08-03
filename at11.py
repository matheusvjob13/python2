def encontrar_maior_menor_numero(sequencia):
    if not sequencia:
        return None, None  # Retornar None para maior e menor se a sequência estiver vazia

    maior_numero = menor_numero = sequencia[0]

    for numero in sequencia:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

    return maior_numero, menor_numero

# Obter a entrada do usuário
sequencia_numeros = []
while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        sequencia_numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

maior, menor = encontrar_maior_menor_numero(sequencia_numeros)
if maior and menor:
    print("Maior número:", maior)
    print("Menor número:", menor)
else:
    print("A sequência está vazia.")
