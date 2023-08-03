import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s). O número secreto era {numero_secreto}.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

# Iniciar o jogo
jogo_adivinhacao()
