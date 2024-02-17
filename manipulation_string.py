nome = "carlos"

print(nome.upper()) #MAIUSCULO
print(nome.lower()) #minusculo
print(nome.title(), "\n-----------------------") #Inicial maiusculo

#--------------------------------------------

texto = "   Olá mundo!   " + "."
print(texto)
print(texto.strip() + ".")  # Imprime o conteúdo da variável 'texto' com espaços em branco removidos do início e do fim, e adiciona um ponto no final: "Olá mundo!."
print(texto.rstrip() + ".")  # Imprime o conteúdo da variável 'texto' com espaços em branco removidos do final, e adiciona um ponto no final: "Olá mundo!."
print(texto.lstrip() + ".","\n-----------------------")  # Imprime o conteúdo da variável 'texto' com espaços em branco removidos do início, e adiciona um ponto no final: "Olá mundo!."

#--------------------------------------------

menu = "Python"  # Define a variável 'menu' como "Python".

# Imprime 'menu' entre barras e cerquilhas.
print("####" + menu + "####")

# Imprime 'menu' centralizado em uma largura de 14 caracteres.
print(menu.center(14))

# Imprime 'menu' centralizado em uma largura de 14 caracteres, preenchendo os espaços com cerquilhas.
print(menu.center(14, "#"))

# Imprime cada letra de 'menu' separada por um hífen.
for letra in menu:
    print(letra, end="-")
print()

# Imprime 'menu' com cada letra separada por um hífen.
print("-".join(menu), "\n-----------------------")

#--------------------------------------------

nome = "Carlos Henrique Torres Marinho"

# Imprime o primeiro caractere da string 'nome'.
print(nome[0])  # Saída: C

# Imprime os caracteres até o nono (exclusivo).
print(nome[:9])  # Saída: Carlos He

# Imprime os caracteres a partir do décimo.
print(nome[10:])  # Saída: nrique Torres Marinho

# Imprime os caracteres do décimo ao décimo sexto (exclusivo).
print(nome[10:16])  # Saída: nrique

# Imprime os caracteres do décimo ao décimo sexto (exclusivo), pulando de dois em dois.
print(nome[10:16:2])  # Saída: nqe

# Imprime toda a string 'nome'.
print(nome[:])  # Saída: Carlos Henrique Torres Marinho

# Imprime a string 'nome' invertida.
print(nome[::-1])  # Saída: ohniraM serroT euqirneH solraC
