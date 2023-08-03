def converter_para_maiusculas(lista_strings):
    lista_maiusculas = [palavra.upper() for palavra in lista_strings]
    return lista_maiusculas

# Exemplo de uso da função:
lista_strings = ["python", "linguagem", "programação"]
lista_maiusculas = converter_para_maiusculas(lista_strings)
print("Lista original:", lista_strings)
print("Lista em maiúsculas:", lista_maiusculas)

