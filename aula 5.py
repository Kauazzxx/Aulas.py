import string  # Importa o módulo string

# Função para converter uma letra em um número
def letra_para_numero(letra):
    alfabeto = string.ascii_lowercase  # Obter o alfabeto em minúsculas
    letra = letra.lower()  # Garante que a letra esteja em minúsculas
    if letra in alfabeto:
        return alfabeto.index(letra) + 1  # Adiciona 1 porque os índices começam em 0
    else:
        return None  # Retorna None se a letra não estiver no alfabeto

# Função para formar uma sequência de números a partir de uma palavra
def digite_numero(palavra):
    numeros = []
    for letra in palavra:
        numero = letra_para_numero(letra)
        if numero is not None:
            numeros.append(numero)
    return numeros

# Teste
palavra = input("Digite uma palavra: ")
numeros_formados = digite_numero(palavra)
if numeros_formados:
    print("Os números formados são:", ' '.join(map(str, numeros_formados)))
else:
    print("Por favor, insira uma palavra contendo apenas letras do alfabeto.")