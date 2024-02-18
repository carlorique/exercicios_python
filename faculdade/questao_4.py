# CARLOS HENRIQUE TORRES MARINHO

# 4. Elabore um programa para ler um número Natural (0 a 9) e mostrar o número por extenso.

numeros_extenso = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]

numero = int(input("Digite um número natural (0 a 9): "))
if 0 <= numero and numero <= 9:
    extenso = numeros_extenso[numero]
    print("Número por extenso:", extenso)
else:
    print("Número fora do intervalo válido.")
