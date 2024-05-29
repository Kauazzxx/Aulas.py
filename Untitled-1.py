def verificar_pode_doar_sangue():
    # Solicitar informações do usuário
    idade = int(input("Qual é a sua idade? "))
    peso = float(input("Qual é o seu peso em kg? "))
    ja_doou_sangue = input("Você já doou sangue antes? (sim/não) ").lower()

    # Verificar se atende aos requisitos de idade, peso e histórico de doação
    if 16 >= idade <= 69 and peso >= 50 and ja_doou_sangue == "não":
        print("Você atende aos requisitos para doação de sangue. Obrigado por considerar a doação!")
    else:
        print("Desculpe, você não atende aos requisitos para doação de sangue.")

# Chamar a função para verificar se pode doar sangue
verificar_pode_doar_sangue()

