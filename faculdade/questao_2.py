# CARLOS HENRIQUE TORRES MARINHO

# 2. O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
# uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / (altura)2
# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
# com a tabela abaixo:

# IMC Condição
# <18.5 | Abaixo do Peso
# >=18.5 e <=25 | Peso Normal
# >25 e <=30 | Acima do Peso
# >30 | Obeso

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o tamanho da sua altura: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Abaixo do peso")
elif (imc >= 18.5) and (imc <= 25):
    print("Peso normal")
elif (imc > 30) and (imc<= 30):
    print("Acima do peso")
elif imc > 30:
    print("Obeso")
else:
    print("")

print(f"Seu IMC: {imc:.2f}")