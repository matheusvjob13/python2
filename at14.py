import string

def contar_ocorrencias_palavras(texto):
    # Remover pontuações do texto
    texto = texto.translate(str.maketrans('', '', string.punctuation))

    # Converter todas as palavras para letras minúsculas
    palavras = texto.lower().split()

    # Criar um dicionário para armazenar as contagens das palavras
    contagem_palavras = {}

    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    return contagem_palavras

# Exemplo de uso do programa:
texto = input("Digite o texto: ")
ocorrencias_palavras = contar_ocorrencias_palavras(texto)

print("\nOcorrências de cada palavra:")
for palavra, ocorrencias in ocorrencias_palavras.items():
    print(f"{palavra}: {ocorrencias}")
