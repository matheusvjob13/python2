def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Conversor de temperatura Celsius/Fahrenheit")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

    escolha = int(input("Escolha uma opção (1 ou 2): "))

    if escolha == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")
    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")
    else:
        print("Opção inválida. Escolha 1 ou 2.")

if __name__ == "__main__":
    main()
