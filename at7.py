def eh_palindromo(palavra):
    palavra = palavra.lower()  # Converter a palavra para minúsculas para evitar problemas de capitalização
    palavra_reversa = palavra[::-1]  # Criar uma versão reversa da palavra usando slicing
    return palavra == palavra_reversa

# Exemplo de uso da função:
palavra_teste = "reconhecer"
if eh_palindromo(palavra_teste):
    print(f"{palavra_teste} é um palíndromo.")
else:
    print(f"{palavra_teste} não é um palíndromo.")
