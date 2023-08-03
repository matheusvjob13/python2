def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None  # Retornar None para maior e menor se a lista estiver vazia

    maior_palavra = menor_palavra = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        elif len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    return maior_palavra, menor_palavra

numero_palavras = int(input("Digite o número de palavras na lista: "))
lista_palavras = []
for i in range(numero_palavras):
    palavra = input(f"Digite a palavra {i + 1}: ")
    lista_palavras.append(palavra)

maior, menor = encontrar_maior_menor_palavra(lista_palavras)
if maior and menor:
    print("Maior palavra:", maior)
    print("Menor palavra:", menor)
else:
    print("A lista está vazia.")
