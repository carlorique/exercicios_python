# CARLOS HENRIQUE TORRES MARINHO

# 3. Desenvolva um algoritmo para identificar letras, números, pontuações “?”, “!”, “.”, “;” e “,”. Caso não se
# encaixe em nenhum desses, informe que é um “Caractere especial”.

particularidade = input("Digite qualquer coisa: ")

for particularidade in particularidade:
    if particularidade.isalpha():
        print("é uma letra.")
    elif particularidade.isdigit():
        print("é um número.")
    elif particularidade in ['?', '!', '.', ';', ',']:
        print(" é uma pontuação.")
    else:
        print("é um caractere especial.")

 