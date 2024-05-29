import random

# Gerando o número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Definindo o número máximo de tentativas
tentativas_maximas = 10

# Lista para armazenar os usuários que acertaram
vencedores = []

print("Bem-vindo ao jogo de adivinhação! Você tem 10 tentativas para adivinhar o número secreto entre 1 e 100.")

# Loop para permitir que cada usuário tente adivinhar o número
for usuario in range(1, 10):  # 9 usuários
    print(f"Tentativa {usuario} de {tentativas_maximas}:")
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_secreto:
        print("O número secreto é maior.")
    elif palpite > numero_secreto:
        print("O número secreto é menor.")
    else:
        print(f"Parabéns! Você acertou o número secreto: {numero_secreto}")
        vencedores.append(usuario)
        break  # Sai do loop se o usuário acertar

# Verificando se todos os 9 usuários tentaram e nenhum acertou
if len(vencedores) == 0:
    print(f"O número secreto era: {numero_secreto}. Nenhum usuário acertou.")
